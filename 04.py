#튜플

#인덱싱/슬라이싱
a = (1,2,3,4,5)
b = a[1] #결과는 요소 타입
c = a[1:] #결과는 튜플

print(b, type(b))
print(c, type(c))

#연산 및 함수 
a = (1,2,3)
b = (4,5,6)
c = a+b
d = a*3

print(len(c))
print(len(d))



#기본
tuple_1 = tuple()
tuple_2 = ()
tuple_3 = (1,)
tuple_no = (1) #이건 튜플 생성X, 우선순위 괄호 표시임
tuple_4 = "1",2, 3.3
tuple_5 = ("1", (2, 3.3))

print(tuple_1)
print(tuple_2)
print(tuple_3)
print(tuple_no)
print(tuple_4)
print(tuple_5)


#리스트

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'bmw'

motorcycles = ['honda', 'yamaha', 'suzuki', 'daelim']
del motorcycles[0]
del motorcycles[0:2]

a = [1, 2, 3]
b = [4, 5, 6]

c = a+b
d = [a,b]
e = a*3

print(len(c))
print(len(d))
print(len(e))

data1 = [1,2,3,4,5]
data2 = [1,2,3,["a","b","c"]]

#슬라이싱
print(data1[:2])
print(data1[2:])
print(data1[2:-1])

print(data2[2:], type(data2[2:0]))
print(data2[3][:2], type(data2[2:0]))


#인덱싱
print(data1[0])
print(data1[-1])
print(data1[0] + data1[-1])

data2 = [1,2,3, ["a", "b", "c"]]
print(data2[0], type(data2[0]))
print(data2[-1], type(data2[-1]))
print(data2[3][1], type(data2[3][1]))



#기본

list_1 = list()
list_2 = []
list_3 = list(["1", 2, 3.3])
list_4 = ["1", 2, 3.3]
list_5 = ["1", [2, 3.3]]

print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_5)

