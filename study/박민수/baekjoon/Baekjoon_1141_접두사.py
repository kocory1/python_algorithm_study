n = int(input())

words=[]
final=[]
for i in range(n):
    words.append(input())
for i in range(len(words)):
    word = words[i]
    flag = 0
    for compare in words:
        if word in compare[:len(word)] and i != words.index(compare):
            flag+=1
    if flag==0 :
        final.append(word)
print(len(final))

