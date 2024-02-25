# 文字列中に値を埋め込むプログラム

name = "Oliva"
hometown = "Tokyo"
print("My name is " + name + "." + "I am from " + hometown + ".")
print("My name is {}. I am from {}.".format(name, hometown))

# フォーマット済文字列リテラル
print(f"My name is {name}. I am {hometown}.")

# 演習

name = input("名前を入力してください。\n")
age = input("年齢を入力してください。\n")

print(f"私の名前は{name}です。{age}歳です。")