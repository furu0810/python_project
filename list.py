scores = [90, 80, 100]
print(scores)

members = ['liam', 'olivia', 'emma']
print(members)

print(scores[0])
print(scores[1])
print(scores[2])
# print(scores[3])


# LEN関数
print(len(scores))

# SUM関数
total = sum(scores)
print(total)

# 負のインデックス
print(scores[-1])
print(scores[-2])
print(scores[-3])

# リストの操作
scores.append(60)
print(scores)

scores.remove(60)
print(scores)

scores.pop(2)
print(scores)
