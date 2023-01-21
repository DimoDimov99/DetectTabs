# TODO add Docstrings
# TODO add README.md
# TODO make git repo


import sys
from colors import Colors
from utils import PROGRAM_NAME, help, clear

file_with_removed_tabs = []


def read_file(filename):
    try:
        with open(filename, "r", encoding="utf8") as file:
            return file.readlines()
    except FileNotFoundError:
        sys.exit(f"{Colors.FAIL}File [{filename}] was not found!")


def detect_if_python_file(filename):
    if filename.endswith(".py"):
        return True
    else:
        return False


def save_to_file(filename, data):
    with open(filename, "w", encoding="utf8") as file:
        for line in data:
            file.write(line)


def detect_for_tabs(filename, short=False):
    clear()
    tab_usage_counter = 0
    lines = read_file(filename)
    lines = [line.replace("\n", "") for line in lines]
    for line_num, line in enumerate(lines):
        if "\t" in line:
            tab_usage_counter += 1
            if not short:
                print(f"{Colors.FAIL}{line_num + 1}: {line} [TAB USAGE FOUND]")
            else:
                print(f"{Colors.FAIL}[TAB USAGE FOUND] found on line: {line_num + 1}")
        if not short and "\t" not in line:
            print(f"{Colors.OKGREEN}{line_num + 1}: {line}")
    print(f"{Colors.DEFAULT}-------------------[SUMMARY]----------------------")
    if tab_usage_counter > 0:
        print(f"{Colors.FAIL}[Total TAB usages detected] [{tab_usage_counter}]")
    else:
        print(f"{Colors.OKGREEN}[No TAB usage detected]")


def detect_and_replace_tabs(filename, tab_equal_spaces=8):
    clear()
    tabs_found = False
    lines = read_file(filename)
    for line_num, line in enumerate(lines):
        if "\t" in line:
            tabs_found = True
            print(f"{Colors.FAIL}Tab found on line {line_num + 1}")
            print(f"{Colors.WARNING}Replacing...")
            t = line.replace("\t", " " * tab_equal_spaces)
            file_with_removed_tabs.append(t)
        else:
            file_with_removed_tabs.append(line)
    if not tabs_found:
        sys.exit(
            f"{Colors.WARNING}No TAB usage found in file <{filename}>\nFile not generated!"
        )
    print(
        f"{Colors.OKGREEN}Replacing finished! [{filename}_tabs_removed] file created!"
    )
    save_to_file(f"{filename}_tabs_removed", file_with_removed_tabs)


def main():
    if (
        len(sys.argv) == 4
        and sys.argv[2].isnumeric()
        and sys.argv[3].lower() == "replace"
    ):
        detect_and_replace_tabs(sys.argv[1], tab_equal_spaces=int(sys.argv[2]))
    elif (
        len(sys.argv) == 3
        and detect_if_python_file(sys.argv[1])
        and sys.argv[2].lower() == "replace"
    ):
        detect_and_replace_tabs(sys.argv[1], tab_equal_spaces=4)
    elif len(sys.argv) == 3 and sys.argv[2].lower() == "replace":
        detect_and_replace_tabs(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[2].lower() == "check":
        detect_for_tabs(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[2].lower() == "check-short":
        detect_for_tabs(sys.argv[1], True)
    elif len(sys.argv) == 2 and sys.argv[1].lower() == "help":
        help()
    else:
        sys.exit(
            f"{Colors.FAIL}Usage: python3 {PROGRAM_NAME} <file> <OPTINAL: space number> <check/check-short/replace>\nFor more information run 'python3 {PROGRAM_NAME} help'"
        )


if __name__ == "__main__":
    main()
