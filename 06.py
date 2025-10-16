#dictionary(사전)



#중첩 반복문

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for d1 in data:
    for d2 in d1:
        print(d2, end=" ")

print()

for i in range(len(data)):
    for j in range(len(data[i])):
        print(data[i][j], end=" ")

print()

for i, d1 in enumerate(data):
    for j,d2 in enumerate(d1):
        print(f"data[{i}][{j}]={d2} \n", end="")

print()


#enumerate() 함수

#iterable 객체를 인자로 받아, 각 요소의 인덱스 번호와 요소 자체를 tuple 형태로 이루어진 iterator 객체를 반환

scores = [10, 20, 30]
i = 1
for score in scores:
    print(f"{i}: {score}")
    i+=i
    
for i in range(len(scores)):
    print(f"{i+1}: {scores[i]}")
    
for i, score in enumerate(scores):
    print(f"{i+1}: {score}")

#iterable: 반복할 수 있는 객체(list, tuple, str 등)
#itertor: 순차적으로 값을 하나씩 반환할 수 있는 객체(range, enumerate 등)



    
