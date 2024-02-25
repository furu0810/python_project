# パーティグッズのサイコロプログラムを開発

import random # サイコロの出目を生成する
dice_list = ["私の秘密", "のろけ話", "夏の思い出", "ありえない話", "ショックな話", "若気の至り"]
num = random.randint(0,5)
print(dice_list[num])

