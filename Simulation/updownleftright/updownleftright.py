import sys

input = sys.stdin.readline

n = int(input())

# x와 y 현재 위치 설정
x,y = 1,1

plans = input().split()

#up down left right 순서 입니다.
dy = [-1,1,0,0]
dx = [0,0,-1,1]
types = ['U','D','L','R']


for plan in plans:
    #여기서 plan 은 'U','D','L','R' 중 하나
    for i in range(len(types)):
        if plan == types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    
    #업데이트 해주기 
    x,y = nx,ny
    
    
print(x,y)