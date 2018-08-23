
from .. import command
import re

def commands():
    return [
            make_regex_capture_command(),
            make_regex_replace_command(),
            make_regex_match_command(),
            make_length_command(),
            make_devnull_command(),
            ]

def make_regex_capture_command():
    def capture(pattern, *strings):
        pattern = re.compile(pattern)
        captures = []
        for string in strings:
            match = pattern.search()
            if not match:
                 continue

            captures.append(" ".join(match.groups()))

        if captures: print("\n".join(captures))
        return 0 if captures else 1

    return  command.Command(
            capture,
            "regex-capture",
            "regex-capture pattern [strings ...]",
            "Use regex to extract substrings"
            )

def make_regex_replace_command():
    def replace(pattern, replacement, *targets):
        out = []
        for target in targets:
            out.append(re.sub(pattern, replacement, target))

        out = "\n".join(out)
        if out: print(out)
        return 0

    return command.Command(
            replace,
            "regex-replace",
            "regex-replace pattern replacement [strings ...]",
            "Do regex replacement on strings"
            )

def make_regex_match_command():
    def match(pattern, *targets):
        matches = []
        pattern = re.compile(pattern)
        for target in targets:
            if pattern.match(target):
                matches.append(target)

        if matches: print("\n".join(matches))
        return 0 if matches else 1

    return command.Command(
            match,
            "regex-match",
            "regex-match pattern [strings ...]",
            "Filter strings through a python regex",
            )

def make_length_command():
    def length(string):
        print(len(string))
        return 0

    return command.Command(
            length,
            "length",
            "length string",
            "Determine the length of a string"
            )

def make_devnull_command():
    def devnull():
        try:
            while(input()): pass
        except EOFError as e:
            pass
        return 0

    return command.Command(
            devnull,
            "devnull",
            "devnull",
            "Accept input and do nothing with it"
            )
