data=[]
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        #print print(len(data))  #每筆都印會拖慢速度
        # if count % 1000 == 0:
        #     print(len(data))

print('檔案讀取完了,總共有',len(data),'筆資料')
print(data[0])

# 統計每個字在留言中出現幾次
# d是字串, data是清單(裝一百萬筆的留言)
wc = {} # word count
for d in data:
    words = d.split(' ') # split('') 等同於 split() > 預設值為空白鍵
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1    # 新增新的key進wc字典
for word in wc:  #word is key
    if wc[word] > 100:
        print(word, wc[word])
print(len(wc))

# 讓使用者來查想查的字
while True:
    word = input('想查甚麼字: ')
    if word == 'q':
        break
        print('離開程式')
    if word in wc:
        print(word, '出現過的次數為:', wc[word])
    else
        print('這個字沒有出現過.')


# 文字記數

# sum_len = 0
# for d in data:
#     sum_len += len(d)
#     #print(sum_len)
# print('留言的平均長度是',sum_len/len(data))

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)

# print('一共有',len(new),'筆留言長度小於100')
# print(new[0])

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)

# list comprehension, 下面寫法等同上面
# good = [d for d in data if 'good' in d]
# 最前面那個 d, 就是good.append(d)中的d

# print('一共有',len(good),'筆留言提到good')
# print(good[0])

# 前面可以放運算 'bad' in d
# bad = ['bad' in d for d in data]

# 同義寫法
# bad = []
# for d in data:
#     bad.append('bad' in d)
