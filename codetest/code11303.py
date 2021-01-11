import sys


def main(argv):
    str_argv = ' '.join(argv)
    str_argv = str_argv.replace(",", "")
    str_argv_list = str_argv.split()
    str_dict = {}
    count = 0
    for i in str_argv_list:
        if i in str_dict:
            str_dict[i] += 1
        else:
            str_dict[i] = 1
    print(str_dict)
    return str_dict


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: code11303.py (any string)")
    else:
        main(sys.argv[1:])
