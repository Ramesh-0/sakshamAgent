def change_line(file_path, line_no, new_text):

    with open(file_path, "r") as f:
        lines = f.readlines()

    if line_no <= len(lines):

        lines[line_no - 1] = new_text + "\n"

    with open(file_path, "w") as f:
        f.writelines(lines)

    print("Line updated")