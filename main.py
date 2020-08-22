import hashlib
import os
import tailer


class LineManager:
    lines = ['a', 'b', 'c', 'd', 'e']

    def addLine(self, line: str):
        # Split the line into segments
        split_line = line.split(' ')

        # Ignore lines that aren't Steam related
        if split_line[0] != '[steam]':
            return

        # Ignore Server Status
        if split_line[9] == '/server-status':
            return

        # Ignore Steam Client
        if split_line[9] == '/client/steam_client_win32':
            return

        # Append the file path to our list
        self.lines.append(split_line[9])

        # Ensure there are only ever 5 elements in the list
        if len(self.lines) > 5:
            self.lines.pop(0)

    def isListSame(self):
        # Since sets are unique, if all the elements are the same, then there should only be one element in the set.
        if len(set(self.lines)) == 1:
            # Get Corrupted File
            line = self.lines[0]

            # Reset the List
            self.regenList()

            # Return the Corrupted File
            return [True, line]
        return [False, '']

    def regenList(self):
        self.lines = ['a', 'b', 'c', 'd', 'e']

    def printList(self):
        for line in self.lines:
            print(line)


def deleteFile(path):
    # Create our hash string
    hash_string = 'steam' + path + 'bytes=0-1048575'

    # Hash our string
    string_hash = hashlib.md5(hash_string.encode()).hexdigest()

    # Create Absolute Path
    path = '/cache/data/cache/' + string_hash[-2:] + '/' + string_hash[-4:-2] + '/' + string_hash

    # Delete File
    if os.path.isfile(path):
        os.remove(path)


if __name__ == '__main__':
    # Create the Line Manager
    line_manager = LineManager()

    # Listen to Access Log
    for tail_line in tailer.follow(open('/cache/logs/access.log')):

        # Add Line
        line_manager.addLine(tail_line)

        # Check if there is a corrupted file in the cache
        list_is_same = line_manager.isListSame()

        # Delete File
        if list_is_same[0]:
            print(list_is_same[1] + " is corrupted. Purging from cache.")
            deleteFile(list_is_same[1])
