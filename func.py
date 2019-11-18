"""
function 函式/功能
語法:
def 函式名稱():
    內容
"""

# 定義
def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
        print('烘衣')

# 參數可設預設值
def add(x=1, y=0):      # 寫參數的時候,等號左右不用空格; 預設值
    # print(x + y)
    return x + y

def average(numbers):
    avg = sum(numbers) / len(numbers)   #除法會自動轉成float
    return avg

# 使用
wash()
wash(True)
wash(water=10)
result = add(3, 4)
print(result)
result = add()
print(result)
result = add(5)
print(result)
result = add(y=5)
print(result)

result = average([1, 2, 3])
print(result)


print(3,4)