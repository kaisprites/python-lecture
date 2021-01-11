print("주민번호입력: ", end='')
num = input()
if num[7] == '1' or num[7] == '3':
    print("남자")
else:
    print("여자")

print("현재시각입력(24h): ", end='')
time = input()
if int(time[0:2]) < 11:
    print("굿모닝")
elif int(time[0:2]) < 15:
    print("굿애프터눈")
elif int(time[0:2]) < 20:
    print("굿이브닝")
else:
    print("굿나잇")

candid= [0,0,0]
while True:
    print("1) 아이유 2) 공유 3) 유재석 0) 종료", end='')
    num = input()
    if num == '1':
        candid[0] += 1
    elif num == '2':
        candid[1] += 1
    elif num == '3':
        candid[2] += 1
    elif num == '0':
        break
    else:
        print("다시 입력")
print(f"아이유: {candid[0]}표, 공유: {candid[1]}표, 유재석: {candid[2]}표")

