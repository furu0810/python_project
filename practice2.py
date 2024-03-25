# Q1 # 再復習

List_A=[26, 12, 11, 100, 77]
List_B=[50, 56, 49, 17, 14]

List_C=[]

for i in range(0,5):
    List_C.append(List_A[i]+List_B[i])
print(List_C)


# Q2

# List=["abc", "defghi", "jklmn", "opqr", "stu", "vw", "xyz"]

# for i in range(len(List)):
#    for j in range(len(List)):
#        print(List[i][j])

# Q3

# word = input("英単語を入力してください。")

# if ("a" and "b") in word:
#    print("both")
#elif ("a" or "b") in word:
#    print("yes")
#else:
#    print("no")

# Q4

text = "あいうえおかきくけこ"

text2 = ''.join(list(reversed(text)))
print(text2)


# Q5

List1=[18, 21, 24, 32, 44, 50, 18, 7, 32, 4]

List2=set(List1) #一意の値を要素としたリストにする
print(List2)


# Q6

#List=["Apple", "Beautiful", "Teacher", "Lion", "Ocean", "Student", "Computer", "Amazon", "Python", "Phone"]


# Q7

keyword = input("キーワードを入力してください。")

# スライス記法で末尾から文字列を比較する

if keyword == keyword[::-1]:
    print("はい")
else:
    print("いいえ")


    
# Q8
    
pos_num = int(input())

for i in range(1, pos_num+1):
    if pos_num % i == 0:
        print(i)


# Q9 再チャレンジする
        
# date = input()

# Q10 再チャレンジする

file_list=["見積もり書_20230601_A.xlsx", "見積もり書_20231210_B.xlsx", "請求書_20230405.xlsx", "請求書_20231020.xlsx"]
for i in file_list:
    print(i.split("_")[1][:8])


# Q11 やり直す
    
text="Python is a versatile, high-level, interpreted language known for simple syntax, object-oriented programming, a large standard library, and applications in various fields, with a strong developer community and easy-to-read code."

# translateメソッドで特定文字を置き換える

print(text.replace(" a ", " the "))

# Q12 コードの可読性を向上させる

import random # 要素を不規則に並び替える

list_a = []
for i in range(1,301):
    if (i % 2 != 0) and (i % 7 == 0):
        list_a.append(i)

# print(list_a)
list_b = random.sample(list_a, len(list_a))
print(list_b)

# Q13

# 後で復習する

# Q14

# 再度解きなおす

# Q15

# 再度解きなおす

# List=[31, 19, 41, 45, 73, 19, 63, 93, 33, 72, 38, 84, 8, 42, 91, 77, 42, 94, 3, 46]
# var1 = 0
# var2 = 0
# for i in List:
#    if i % 9 != 0:
#        var1 += i
#    elif i % 9 == 0:
#        var2 += i


# Q16

# 再度解きなおす


# Q17

# 再度回答を読む
