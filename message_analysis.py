data=[]
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        #print print(len(data))  #每筆都印會拖慢速度
        if count % 1000 == 0:
            print(len(data))

print(data[0])