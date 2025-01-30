t=int(input())

for _ in range(t):
    h, w, n = map(int, input().split())
    answer=0
    r = n % h
    m = n // h
    if r==0:
        answer+= h*100
        answer+= m
    else:
        answer+=100 * r
        answer+= m + 1
    print(answer)