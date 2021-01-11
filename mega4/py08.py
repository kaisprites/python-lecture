from tkinter import messagebox
import datetime

for i in range(1, 11):
    print('*' * i)

print('나의이름은: ', end='')
name = input()
print('나의나이는: ', end='')
age = input()
print('나의성별은: ', end='')
gender = input()
print('나의좌우명은: ', end='')
quote = input()
print(f"나는 {name}이고 내 나이는 {age}세, 내년 나이는 {int(age)+1}세가 될 예정이고\n"
      f"나는 {gender}, {quote}가 내 좌우명!")

print('당신의이름은: ', end='')
name = input()
print('당신의관심사는: ', end='')
interest = input()
message = ''
if interest == '파이썬':
    message = '분석가가 되실거군'
else:
    message = '개발자가 되실거군'
messagebox.showinfo("메시지상자",
                    f"이름:{name}\n"
                    f"관심사:{interest}\n"
                    f"{message}")

print(datetime.datetime.now())
month = datetime.datetime.now().month
if 3 <= month <= 5:
    print("봄")
elif 6 <= month <= 8:
    print("여름")
elif 9 <= month <= 11:
    print("가을")
else:
    print("겨울")

sumvalue = 0
for i in range(55,689,3):
    sumvalue += i
print(sumvalue)

gildong = []
while True:
    print('길동을 입력: ', end='')
    string = input()
    if string == 'x' or string == 'X':
        break
    else:
        gildong.append(string)
print(f"첫번째 선수는 {gildong[0]}, 세번째 선수는 {gildong[2]}")