n = int(input())
count = []
if n % 5 == 0:
    count.append(n//5)
if n % 3 == 0:
    count.append(n//3)

d = 0
while n > 5:
    n -= 5
    d+=1
    if n % 3 == 0 and n<15:
        d+=n//3
        count.append(d)
        break

if len(count) == 0:
    print(-1)
else :
    print(min(count))
