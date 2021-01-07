import sys


def main(argv):
    str_argv = ' '.join(argv)
    str_argv = str_argv.replace(",", "")
    str_argv_list = str_argv.split()
    count = 0
    for i in str_argv_list:
        if i == "사람":
            count += 1
    result = f"사람({count})"
    print(result)
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: code11302.py (any string)")
    else:
        main(sys.argv[1:])
