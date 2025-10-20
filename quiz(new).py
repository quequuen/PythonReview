#20
def get_students(scores):
    return scores.keys() if get_students else []


scores = {"kim":95, "lee":65}
students = get_students(scores)
if students:
    students = ",".join(students)
    print(f"명단:{students}")
else:
    print("학생이 없음")

#19
def avg_score(dictionary):
    hap = 0
    for v in dictionary.values():
        hap += v
    return int(hap/len(dictionary)) if dictionary else None

scores={"kim":95, "lee":65}
avg = avg_score(scores)

if avg!=None:
    print(f"평균:{avg}")
else:
    print("점수가 없음")

#18

def remove_value(numbers, n):
    while n in numbers:   # 리스트에 n이 존재하는 동안 반복
        numbers.remove(n) # 해당 값 삭제
    return numbers

numbers = [1, 2, 3, 4, 5]
remove_value(numbers, 2)
print(numbers)

#def remove_value(numbers, n):
#    numbers_2 = []
#    for number in numbers:
#        if(n != number):
#            numbers_2.append(number)
#    return numbers_2
    
#numbers = [1, 2, 3, 4, 5]
#result = remove_value(numbers, 2)
#print(result)


#17
def list_avg(numbers):
    hap = 0
    for n in numbers:
        hap += n
    return int(hap/len(numbers))

numbers = [1, 2, 3, 4, 5]
result = list_avg(numbers)
print(result)

#16
def list_sum(numbers):
    hap = 0
    for n in numbers:
        hap += n
    return hap
    
numbers = [1, 2, 3, 4, 5]
result = list_sum(numbers)
print(result)

#15
def hello_12(str):
    n = int(input("원하는 반복횟수를 입력:"))
    for n in range(n):
        print(str )
        
str = input("반복할 문구 입력:")
hello_12(str)

#14
n1 = int(input("숫자1을 입력하세요:"))
n2 = int(input("숫자2를 입력하세요:"))
def div(n1, n2):
    if n2==0:
        return None
    else:
        return n1/n2

result = div(n1, n2)
print(result)

#13
n1 = int(input("숫자1을 입력하세요:"))
n2 = int(input("숫자2를 입력하세요:"))

def mul(n1, n2):
    return n1*n2
result = mul(n1,n2)
print(result)

#6, 7, 8, 9, 10, 11, 12
def hello(n):
    #6, 7
    #print("안녕하세요\n"*3)
    #print()
    
    #8
    #hi = 0
    #while(hi<3):
    #    print("안녕하세요")
    #    hi += 1
    #print()
    
    #9
    #for n in range(3):
    #    print("안녕하세요")
    #print()
    
    #10
    #print("안녕하세요\n"*n, end="\n")

    #11
    #i = 0
    #while(i<n):
    #    print("안녕하세요")
    #    i += 1

    #12
    for n in range(3):
        print("안녕하세요")
    print()

n = int(input("숫자를 입력하세요:"))
hello(n)

#5
for n in range(3):
    print("안녕하세요")
print()

#4
i = 0
while(i<3):
    print("안녕하세요")
    i += 1
print()

#3
print("안녕하세요\n"*3)

#2
print("안녕하세요\n안녕하세요\n안녕하세요\n")

#1
print("안녕하세요")
