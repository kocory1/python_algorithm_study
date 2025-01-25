import string
a = list(string.ascii_lowercase)
s=input()
char=[]
for c in s:
    char.append(c)
for c in a:
    if c in char:
        print(f"{char.index(c)} ",end="")
    else:
        print("-1 ",end="")