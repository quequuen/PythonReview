#24 개선 버전2
def add_list2(list1, list2):
    # zip으로 같은 인덱스끼리 더하기
    result = [a + b for a, b in zip(list1, list2)]
    
    # 남는 부분(더 긴 리스트의 뒷부분) 추가
    if len(list1) > len(list2):
        result += list1[len(list2):]
        # 인덱스는 0부터 시작하기 때문에 list2의 마지막 숫자는 포함하지 않고 그 다음 숫자부터 포함됨.
    else:
        result += list2[len(list1):]
        
    return result

print(add_list2([1,2,3,4],[1,2]))
print(add_list2([0,1],[1,2,6,7,8]))

#24 개선 버전1
def add_list1(list1, list2):
    # 더 긴 리스트 복사 (원본 변경 방지)
    result = list1[:] if len(list1) >= len(list2) else list2[:]
    
    # 짧은 리스트 길이만큼 반복
    min_len = min(len(list1), len(list2))
    
    for i in range(min_len):
        result[i] = list1[i] + list2[i]
    
    return result

print(add_list1([1,2,3,4],[1,2]))
print(add_list1([0,1],[1,2,6,7,8]))

#24

def add_list(list1, list2):
    result_list = (list1 if len(list1) > len(list2) else list2)
    # 일단 리스트의 범위를 넘는 인덱스를 조회하는 것에서부터 오류가 남.

    for i, n in enumerate(list1 if len(list1) < len(list2) else list2):
        result_list[i] = result_list[i] + n
        
    return result_list

print(add_list([1,2,3,4],[1,2]))
print(add_list([0,1],[1,2,6,7,8]))

#23
def search_index(list1, num):
    list2 = []
    for i,n in enumerate(list1):
        if n == num :
            list2.append(i)

    return list2

print(search_index([35, 28, 30, 29, 30],30))
print(search_index([35, 28, 30, 29, 30],31))

#22

def merge_list(list1, list2):
     # 두 리스트 합치기
    merged = list1 + list2

    # 중복 제거 (직접 검사)
    unique = []
    for n in merged:
        if n not in unique:
            unique.append(n)

    print(unique)

    # 오름차순 정렬 (버블 정렬)
    for i in range(len(unique) - 1):
        for j in range(len(unique) - 1 - i):
            if unique[j] > unique[j + 1]:
                unique[j], unique[j + 1] = unique[j + 1], unique[j]

    return unique

print(merge_list([1,2,3,4],[1,2,5]))
print(merge_list([0,1,10],[1,2,6,7,8]))

#21
def add_dict(scores, name, score):
    if name in scores.keys():
        return False
    else:
        scores[name] = score
        return True

scores = {"kim": 95, "lee": 65}
if add_dict(scores, "park", 100):
    print("입력 완료")
else:
    print("동일 학생 있음")

if add_dict(scores, "kim", 100):
    print("입력 완료")
else:
    print("동일 학생 있음")

print(scores)

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
