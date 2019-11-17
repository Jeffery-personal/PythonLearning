# if

"""
rain = input('請問今天有沒有下雨:')

if rain == '有':
    print('撐傘出門')
    print('買一包洋芋片')
    print('在家看電影')
"""

# 型別轉換(casting),if,elif
"""
age = input('請輸入年齡:')
age = int(age)
if age >= 20:
    print('你可以投票')
else:
    print('你還不能投票')
"""

"""
age = input('請輸入年齡:')
age = int(age)
if age < 13:
    print('國小')
elif age >= 13 and age < 18:
    print('國高中')
elif age >= 18 and age < 22:
    print('大學')
else:
    print('社會')
"""

# while

"""
x = 5
while x < 10:
    print('x小於10喔!')
    x = x + 1
print('我逃出了!')
"""

while True:
    mode = input('請輸入遊戲模式: ')
    if mode == 'q': #quit
        break
    elif mode == '1':
        print('啟動模式一')
    elif mode == '2':
        print('啟動模式二')
    else:
        print('只能輸入1/2/q')