import os   #operating system

products = []
if os.path.isfile('products.csv'):  # 檢查檔案是否存在
    print('找到檔案')
    # product如何又裝名字又裝清單 ? 二維清單(小清單放到大清單)
    """
    讀取檔案
    1. 增加讀取檔案程式碼
    2. 用split(',')來用逗點做分割
    3. 用strip()來除掉換行符號(\n)
    4. 加上encoding='utf-8'來讀取
    5. 解釋split完會變清單
    6. 把讀到的內容裝進清單
    """
    with open('products.csv', 'r', encoding = 'UTF-8') as f: # 記得編碼
        for line in f:
            # 跳過欄位名稱
            if '商品,價格' in line:
                continue
            # 注意! split切割完的結果是清單
            name, price = line.strip().split(',')     # 先把換行符號去掉,再逗點分割
            products.append([name, price])
    print(products)    
else:
    print('找不到檔案')

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    price = int(price)
    #p = []
    #p.append(name)      # 小清單
    #p.append(price)     # 小清單
    p = [name, price]    # 簡化上面三行
    products.append(p)  # 大清單, products.append([name, price]) 更簡化
    # products.append(name)
print(products)

# 印出商品紀錄
for p in products:
    print(p)
    print(p[0], '的價格是', p[1])

"""
product[0][0] 代表甚麼意思? 代表n0
product[0][1] 代表甚麼意思? 代表p0
product[1][0] 代表甚麼意思? 代表n1
product[1][1] 代表甚麼意思? 代表p1

product[大清單index][小清單index]

[[n0,p0],[n1,p1]]
"""

# 字串可做加乘法
# 'abc' + 'abc' = 'abcabc'
# 'abc' * 3 = 'abcabcabc'

# 寫入檔案
# 複習: with可自動close已經open的檔案
# 在寫入與讀取時, 都會遇到編碼問題
"""
Excel導入CSV資料:
資料 > 取得外部資料 > 從文字檔
編碼: 選UTF-8
分格符號: 選逗點
"""

# 寫入檔案
with open('products.csv','w', encoding='utf-8') as f:   # 加入編碼避免寫入中文時造成亂碼
    #f.write('商品,價格\n')                  # 這樣寫顯示會有問題(編碼問題造成, 上行須加入編碼)
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')   # 加法可以字串相加,若p[1]是整數呢?
        f.write(p[0] + ',' + str(p[1]) + '\n')  # 用STR轉換成字串