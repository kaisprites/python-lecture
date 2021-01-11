from functools import reduce


def main(f):
    str_array = f.readline().split(' ')
    num_multi = str(reduce(lambda acc, cur: acc * int(cur), str_array, 1))
    num_dict = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0,
                "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}
    for i in num_multi:
        num_dict[i] += 1
    for k, v in num_dict.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    try:
        f = open("code12083.txt", "r")
        main(f)
        f.close()
    except FileNotFoundError:
        print("there is no input file")

