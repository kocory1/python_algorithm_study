# n = int(input())
# grades=input().split()
# for i in range(len(grades)):
#     grades[i] = int(grades[i])
# fixed=0
# max_grade = max(grades)
# for grade in grades:
#     fixed+=(grade/max_grade*100)
#
# print(fixed/n)

n = int(input())
my_list = list(map(int, input().split()))
mymax = max(my_list)
sum = sum(my_list)

print(sum*100/mymax/n)

