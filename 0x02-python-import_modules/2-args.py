#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    keys = len(argv) - 1
    if keys == 0:
        print("0 arguments.")
    elif keys == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(keys))
    for index in range(keys):
        print("{}: {}".format(index + 1, argv[index + 1]))
