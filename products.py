# product如何又裝名字又裝清單 ? 二維清單(小清單放到大清單)

products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')
    #p = []
    #p.append(name)      # 小清單
    #p.append(price)     # 小清單
    p = [name, price]    # 簡化上面三行
    products.append(p)  # 大清單, products.append([name, price]) 更簡化
    # products.append(name)
print(products)

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