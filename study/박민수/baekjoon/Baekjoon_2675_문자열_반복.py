num = int(input())
for i in range(num):
    order = input()
    iter_count = int(order.split()[0])
    sentence = order.split()[1]
    for j in sentence:
        print(j * iter_count,end="")
    print()
