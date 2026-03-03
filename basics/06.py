#dictionary(사전)
#순서가 없음!

#딕셔너리의 value가 딕셔너리

students = {
    '12210001': {'name': '김인하', 'major': '컴퓨터'},
    '12210011': {'name': '김슈슉', 'major': '전자'},
    '12210111': {'name': '김슈룩', 'major': '물류'}
    }

for number, student in students.items():
    print(f"학번: {number}")
    print(f"이름: {student['name']}")
    print(f"전공: {student['major']}")
#key값이 문자열이면 무조건 dict['key']처럼 ''붙일 것!

#딕셔너리의 value가 리스트
bibimbap = {
    '양념': '고추장',
    '고명': ['버섯', '계란', '콩나물', '시금치', '육회']
    }
print(f"당신이 주문한 비빔밥의 양념은 {bibimbap['양념']}이고, 고명은 ",end="")
print(", ".join(bibimbap['고명']), end="입니다.\n")

for value in bibimbap['고명']:
    print(f"{value}", end=", "); 

#딕셔너리가 요소인 리스트
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'red', 'points': 15}
alien_2 = {'color': 'blue', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for idx in range(len(aliens)):
    print(f"{idx+1}번 외계인 색상: {aliens[idx]['color']}")


#딕셔너리 기본
fav_fruits = {
    '김인하': '딸기',
    '이물류': '복숭아',
    '최컴정': '키위'
    }

for name, fruit in fav_fruits.items():
    print(f"{name}이 좋아하는 과일은 {fruit}입니다.")
#.items로 key, value 둘 다 받고 띄울 수 있는 거 꼭 기억하기!

for value in fav_fruits.values():
    print(f"좋아하는 과일은 {value}에 투표해주셔서 감사합니다.")
#.values()로 value만 조회 가능

#for key in fav_fruits.keys():
for key in fav_fruits:
#keys()없이 사용해도 키 순회로 동작한다.
    print(f"{key}가 좋아하는 과일은 {fav_fruits[key]}입니다.")

myInfo = {1: 'one', 2: 'two'}
height = myInfo.get('height')
#myInfo['height'] != myInfo.get('height')
#myInfo.get('height')는 key가 없으면 None을 반환한다.

print(f"나의 키는 {height} cm입니다." ) if None != height else print("아직 키 정보가 없습니다.")

if None != height:
    print(f"나의 키는 {height}cm 입니다.")
else:
    print("아직 키 정보가 없습니다.")

myinfo = {'name':'kim inha', 'age':23}
print("이름: ", myinfo['name'])
print("나이: ", myinfo['age'])



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



    
