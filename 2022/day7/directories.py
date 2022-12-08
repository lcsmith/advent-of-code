import os
import sys


def run_day7():
    with open(os.path.join(sys.path[0], "day7\\input"), "r") as infile:
        lines = infile.readlines()

    dir_struct = DirectoryTreeNode(None)
    current_dir = dir_struct
    for line in lines:
        line_split = line.split()
        if line == "$ cd /\n":
            while current_dir.parent is not None:
                current_dir = current_dir.parent
        elif line == "$ cd ..\n":
            current_dir = current_dir.parent
        elif line == "$ ls\n":
            pass
        elif line_split[0].isnumeric():
            current_dir.files[line_split[1]] = int(line_split[0])
        elif line_split[0] == "dir":
            if current_dir.subdirectories.get(line_split[1]) is None:
                current_dir.subdirectories[line_split[1]] = DirectoryTreeNode(current_dir)
        elif line_split[0] == "$" and line_split[1] == "cd":
            current_dir = current_dir.subdirectories[line_split[2]]

    traverse_sizes(dir_struct)


def traverse_sizes(directory):
    total_size = sum(directory.files.values())
    for subdirectory in directory.subdirectories.items():
        if subdirectory[1].size is None:
            traverse_sizes(subdirectory[1])
        total_size += subdirectory[1].size
    if total_size < 100000:
        print(total_size)
    directory.size = total_size


class DirectoryTreeNode:
    def __init__(self, parent):
        self.parent = parent
        self.subdirectories = {}
        self.files = {}
        self.size = None
