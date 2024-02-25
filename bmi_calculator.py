#BMIを計算する
height = float(input("身長を入力してください。\n"))
weight = float(input("体重を入力してください。\n"))

bmi = weight / (height * height)
print("BMI:",str(bmi))
