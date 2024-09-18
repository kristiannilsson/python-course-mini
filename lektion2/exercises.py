def count_lines_in_file(file_path):
    with open(file_path) as f:
        lines = f.readlines()
        print(lines)
        print(len(lines))


count_lines_in_file("poem.txt")
