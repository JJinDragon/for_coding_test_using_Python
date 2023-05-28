#백준 10815 숫자카드
import sys

input= sys.stdin.readline
N=int(input())
sanggeun=list(map(int,input().split()))
M=int(input())
card=list(map(int,input().split()))

N_M=list(set(sanggeun)&set(card))

for i in card:
    if i in N_M:
        print(1, end=" ")
    else:
        print(0, end=" ")
