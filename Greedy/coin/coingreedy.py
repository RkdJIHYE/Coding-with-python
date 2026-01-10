n = 1260 #거슬러 줘야 할 돈 예시 n

count =0 #동전의 최소 개수 

coin = [500,100,50,10]

for i in coin:
    tmp = n // i
    count +=tmp
    n = n % i
    
print(count)
