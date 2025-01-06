#defaultdict
# 존재하지 않는 키를 조회할 경우, 에러 대신 default값을 기준으로 해당 키에 대한 딕셔너리 아이템 생성
import collections
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 5
a['C']+=1
print(a)

#counter

a=[1,2,3,4,5,5,5,6,6]
b = collections.Counter(a)
print(b)
#실 타입은 딕셔너리를 Wrapping한 collections.Counter
print(type(b))
print(b.most_common(1)) #출력할 요소 수

#OrderedDict
# 입력 순서 유지
# 사실 python3.7부턴 걍 딕셔너리도 유지된다

ordered_dict = collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 1})
print(ordered_dict)
