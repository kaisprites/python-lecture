import sys;

def main(str_param):
    str_list = list(str_param)
    char_list = {}
    for i in str_list:
        if i in char_list:
            char_list[i] = char_list[i] + 1
        else:
            char_list[i] = 1
    print(char_list)
    return char_list


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: input.py (any string)")
    else:
        main(sys.argv[1])
