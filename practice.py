# python practice 

# Q1

x = 10
y = 20

print("x * y の値は", x * y)

# Q2

word1 = "演習"
word2 = "問題"

print(f"{word1 + word2}")

# Q3

name = "古澤翔"
age = "28"

print(f"私は{name}です。{age}歳です。")

# Q4

List=[81, 15, 11, 60, 57]

print(List[0]-List[4])

# Q5

num = int(input("整数を入力してください。："))

print(num % 10)

# Q6

val = int(input("整数を入力してください。："))

if val >= 20:
    print("はい")
else:
    print("いいえ")

# Q7
    
for i in range(1, 101):
    print(i)

# Q8

List = []    

for j in range(1, 101):
    List.append(j)
print(List)

# Q9

text="あいうえおかきくけこ"

print(text[4:7]) # スライシング

# Q10

word_list=["Apple", "Beautiful", "Teacher", "Lion", "Ocean", "Student", "Computer", "Amazon", "Python", "Phone"]

for word in word_list:
    print(word)

# Q11
    
word_list=["Apple", "Beautiful", "Teacher", "Lion", "Ocean", "Student", "Computer", "Amazon", "Python", "Phone"]

for i in range(len(word_list)):
    print(word_list[i])

# Q12

text="あいうえおかきくけこ"

for i in range(len(text)):
    print(text[i])

# Q13
    
# import re

text="あいうえおかきくけこ"

for i in range(len(text)):
    if text[i] == "く":
        print(text[i])


# Q14

# string = input("文字列を入力してください。")
# for string in range(0, 5):
#     print(string)

# Q15
        
str = input()

print(str[-5:])


# Q16

string = input("文字列を入力してください。")

print(len(string))

# Q17

text="あいうえおおえういあ"

for i in range(len(text)):
    if text[i] == "う":
        print(i)


# Q18
        
#word = input("英単語を入力してください。")

#for i in range(len(word)):
#    if word[i] == "a":
#        print("yes")
#        break
#    else:
#        print("no")
#        break

# Q19

# datetimeライブラリをインポートする    

#date="4/10/2023"

#japanese_datetime = date.strfttime("%Y年%m月%d日")

#print(japanese_datetime)
        

# Q20

# OSでファイル名等を取得したい場合のライブラリ
import os

path="/Users/username/Desktop/test/sample.txt"

filename = os.path.splitext(os.path.basename(path))[0]
print(filename)


# Q21 2回目の実施を行う

# datetimeモジュールを使用
import datetime

today = datetime.date.today()
date = today.strftime('%Y/%m/%d')
print(date)

# Q22

# text="Python is a versatile, high-level, interpreted language known for simple syntax, object-oriented programming, a large standard library, and applications in various fields, with a strong developer community and easy-to-read code."

# Q23

# List=[5,6,7,8,9]

# for list in range(List):
#    if list == 8:
#        print(list+10)

# Q24

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]

print(sorted(List)) # 小さい順に並び替える

# Q25

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]

print(sorted(List, reverse=True)) # 大きい順に並び替える

# Q26

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]

sum = 0

for num in List:
    sum += num
print(sum)

# Q27

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]
print(max(List))

# Q28

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]
print(min(List))

# Q29 ## 別解も利用する

# 平均値を算出する
import statistics

List=[35, 7, 26, 59, 55, 73, 90, 24, 13, 28, 20, 71, 8, 89, 81, 97, 39, 66, 42, 57]
print(statistics.mean(List))

# Q30 ## 再度やり直し

word_list=["Apple", "Beautiful", "Teacher", "Lion", "Ocean", "Student", "Computer", "Amazon", "Python", "Phone"]

word_list2=[]

for word in word_list:
    if word[0]=="A":
        word_list2.append(word)
print(word_list2)

