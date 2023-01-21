from colors import Colors
import os
import platform

PROGRAM_NAME = "detect_tabs.py"
ARGS_EXPLANATION = {
    "replace": "replace all TAB usage in file with spaces and generate new file",
    "<int(number)>": "OPTIONAL argument (int number) which will convert all tabs to the provided number of spaces.\nDefault value is 8 (Please not for python files (.py) the value is 4 by default (PEP8))",
    "check": "analyze file for TAB usage and provides output",
    "check-short": "analyze file for TAB usage and provide simplified output",
}

EXAMPLE_USAGES = {
    "example usage with 'check' argument": f"python3 {PROGRAM_NAME} <filename> check",
    "example usage with 'check-short' argument": f"python3 {PROGRAM_NAME} <filename> check-short",
    "example usage with 'replace' argument": f"python3 {PROGRAM_NAME} <filename> replace",
    "example usage with 'replace' argument and not default tab to space value": f"python3 {PROGRAM_NAME} <filename> <10> replace",
    "example usage with 'replace' argument and .py file": f"python3 {PROGRAM_NAME} <filename.py> replace ",
}


def clear() -> None:
    """Clears the terminal input"""
    current_os = platform.system()
    if current_os == "Linux":
        os.system("clear")
    else:
        os.system("cls")


def help():
    clear()
    print(
        f"{Colors.FAIL}Usage: python3 {PROGRAM_NAME} <file> <OPTINAL: space numbers> <check/check-short/replace>"
    )
    print(f"{Colors.DEFAULT}-" * 20)
    print(f"{Colors.BOLD}{Colors.WARNING}Usage of arguments:\n")
    for key, value in ARGS_EXPLANATION.items():
        print(f"{Colors.RESET}{Colors.OKGREEN}{key}: {value}")
        print(f"{Colors.DEFAULT}-" * 20)
    print(f"{Colors.BOLD}{Colors.WARNING}Example usages:\n")
    for key, value in EXAMPLE_USAGES.items():
        print(f"{Colors.RESET}{Colors.OKGREEN}{key}: {value}")
