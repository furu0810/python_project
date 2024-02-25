scores = [100, 90, 80, 70, 60]
sum = 0

# テストの合計値を計算
for score in scores:
    sum += score

avg = sum / len(scores) # テストの平均値を計算

print(f'合計値：{sum}') 
print(f'平均値：{avg}') 

