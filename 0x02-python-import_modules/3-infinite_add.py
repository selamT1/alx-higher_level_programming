#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    keys = int(len(argv) - 1)
    if keys == 0:
        print("0")
    elif keys == 1:
        print("{}".format(argv[keys]))
    else:
        for index in range(keys):
            result += int(argv[index + 1])
        print("{}".format(result))
