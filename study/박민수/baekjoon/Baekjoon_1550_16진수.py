o = [i for i in input()]

ot = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

result = 0
for n in o:
    result*=16
    result+=ot.index(n)
print (result)