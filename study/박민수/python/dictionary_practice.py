#딕셔너리 선언 및 값 할당
a= {'key1' : 'value1', 'key2':'value2'}
print(a)
a['key3'] = 'value3'
print(a)

# key에 해당하는 value 반환
print(a['key1'])

#예외처리
try :
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키')

if 'key4' in a:
    print("존재하는 키")
else :
    print("그딴건 없다")

# for 반복문을 통한 조회
for k,v in a.items():
    print(k,v)

# 삭제
del a['key1']
print(a)