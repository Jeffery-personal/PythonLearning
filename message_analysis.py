data=[]
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        #print print(len(data))  #每筆都印會拖慢速度
        #if count % 1000 == 0:
            #print(len(data))

#print('檔案讀取完了,總共有',len(data),'筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
    #print(sum_len)
print('留言的平均長度是',sum_len/len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)

print('一共有',len(new),'筆留言長度小於100')
print(new[0])

good = []
for d in data:
    if 'good' in d:
        good.append(d)

# list comprehension, 下面寫法等同上面
# good = [d for d in data if 'good' in d]
# 最前面那個 d, 就是good.append(d)中的d

print('一共有',len(good),'筆留言提到good')
print(good[0])

# 前面可以放運算 'bad' in d
# bad = ['bad' in d for d in data]

# 同義寫法
bad = []
for d in data:
    bad.append('bad' in d)
