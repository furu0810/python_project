# bmiから体格を出力する

# Aさんの体重、身長
weight = 60
height = 1.0

bmi = weight / ( height * height )

# bmiで指定して体格を出力する
if bmi >= 25:
    print('肥満')
elif bmi >= 18.5 and bmi < 25:
    print('普通')
else:
    print('瘦せ')

