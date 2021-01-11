def main(f):
    window_dict = {}

    while True:
        floor_str = f.readline()
        if floor_str == "":
            break
        floor_num = floor_str[0:floor_str.find("(")-2]
        open_window_num = floor_str.count("(o)")
        window_dict[floor_num] = open_window_num

    window_sum = 0
    for floor, window in window_dict.items():
        print(f"{floor}번째 층의 열린 창문 수 : {window}개")
        window_sum += window

    print(f"총 열린 창문 수: {window_sum}개")
    return window_dict


if __name__ == "__main__":
    try:
        f = open("input.txt", "r")
        main(f)
        f.close()
    except FileNotFoundError:
        print("there is no input file")

