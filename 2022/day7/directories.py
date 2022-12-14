

def run():
    with open('input') as infile:
        lines = [line.strip() for line in infile]

    dir_struct = DirectoryTreeNode(None)
    current_dir = dir_struct
    for line in lines:
        line_split = line.split()
        if line == "$ cd /":
            while current_dir.parent is not None:
                current_dir = current_dir.parent
        elif line == "$ cd ..":
            current_dir = current_dir.parent
        elif line == "$ ls":
            pass
        elif line_split[0].isnumeric():
            current_dir.files[line_split[1]] = int(line_split[0])
        elif line_split[0] == "dir":
            if current_dir.subdirectories.get(line_split[1]) is None:
                current_dir.subdirectories[line_split[1]] = DirectoryTreeNode(current_dir)
        elif line_split[0] == "$" and line_split[1] == "cd":
            current_dir = current_dir.subdirectories[line_split[2]]

    traverse_sizes(dir_struct)
    space_to_delete = dir_struct.size - 40000000
    print(find_minimal_directory(dir_struct, space_to_delete).size)


def traverse_sizes(directory):
    total_size = sum(directory.files.values())
    for subdirectory in directory.subdirectories.items():
        if subdirectory[1].size is None:
            traverse_sizes(subdirectory[1])
        total_size += subdirectory[1].size
    if total_size < 100000:
        print(total_size)
    directory.size = total_size


def find_minimal_directory(directory, space_to_delete):
    if directory.size < space_to_delete:
        return None
    minimal_directory = directory
    for subdirectory in directory.subdirectories.items():
        sub_minimal = find_minimal_directory(subdirectory[1], space_to_delete)
        if sub_minimal is not None and sub_minimal.size < minimal_directory.size:
            minimal_directory = sub_minimal
    return minimal_directory


class DirectoryTreeNode:
    def __init__(self, parent):
        self.parent = parent
        self.subdirectories = {}
        self.files = {}
        self.size = None


if __name__ == '__main__':
    run()
