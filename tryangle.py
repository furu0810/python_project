# 三角形の面積を求める
# 1.引数付きの関数を定義する 
# 2.三角形の面積の公式を定義する。
# 3.関数＋引数で値を呼び出す

def triangle_area(bottom, height):
    area = (bottom * height) / 2
    print(f"{area}cm^2")

triangle_area(2,2)
