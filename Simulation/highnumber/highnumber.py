#입력 예시 
# 5 8 3
# 2 4 5 4 6

#출력 예시
#46


import sys 

input = sys.stdin.readline
N,M,K = map(int,input().split())
numbers = list(map(int,input().split()))

#print(N)
#print(numbers)

#한번 정렬해주는 것이 필요
numbers.sort()

fir = numbers[-1] #가장 큰 수 
sec = numbers[-2] #두번째로 큰 수 

print(fir)
print(sec)

#M은 반복 횟수
#k는 최대 반복 횟수

#결과값 저장할 변수 result

result = 0

while True:
    for i in range(K):
        if M == 0:
            break
        result+=fir
        M-=1
    if M == 0:
        break
    
    result+=sec
    M-=1

print(result)
    
    
