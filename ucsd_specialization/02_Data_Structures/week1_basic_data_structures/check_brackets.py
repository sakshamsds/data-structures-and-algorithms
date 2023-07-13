# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)

        if next in ")]}":
            # Process closing bracket, write your code here
            if are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
            else:
                return i + 1
            
    return i+1 if opening_brackets_stack else "Success"


def main():
    text = input()
    # text = "foo(bar);"
    # text = "{[}"
    # text = "foo(bar[i);"
    # text = "[]"
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
