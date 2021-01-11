def main(f):
    while True:
        string = f.readline()
        if string == '':
            break
        s = string.split(" ")
        p = ''
        for i in s[1]:
            if i == '\n':
                break
            p += i * int(s[0])
        print(p)


if __name__ == "__main__":
    try:
        f = open("code12082.txt", "r")
        main(f)
        f.close()
    except FileNotFoundError:
        print("there is no input file")

