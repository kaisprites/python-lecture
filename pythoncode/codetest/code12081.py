def main(l_num, s_num):
    result = 0
    for i in s_num:
        result += int(i)
    print(result)


if __name__ == "__main__":
    try:
        f = open("code12081.txt", "r")
        length_num = int(f.readline())
        str_num = f.readline()
        main(length_num, str_num)
        f.close()
    except FileNotFoundError:
        print("there is no input file")
