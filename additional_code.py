#추가 실습 코드

#딕셔너리 값의 평균 계산하기

def calculate_average_from_dict(student_scores):
    values = student_scores.values()
    return sum(values) / len(values)

student_scores = {"김인하": 92, "이인하": 85, "박인하": 78}
avg_score = calculate_average_from_dict(student_scores)
print(f"평균 점수: {avg_score:.2f}")

#리스트에서 특정 값 지우기
def remove_value(numbers, value_to_remove):
    for i, num in enumerate(numbers): #인덱스, 요소
        if num == value_to_remove:
            del numbers[i]
    return numbers

#리스트 컴프리헨션(꼭 숙지 할 것)
#def remove_value(numbers, value_to_remove):
#    return [num for num in numbers if num != value_to_remove]

numbers = [1, 2, 3, 2, 4, 2, 5]

value_to_remove = 2
updated_list = remove_value(numbers, value_to_remove)
print(f"제거 후 리스트: {updated_list}")




#리스트의 중복 항목 개수 세기
def count_duplicates(numbers):
    dup_dict = dict()
    for num in numbers:
        if num not in dup_dict:
            dup_dict[num] = 1
        else:
            dup_dict[num] += 1

    for num in numbers:
        if dup_dict[num] == 1:
            del dup_dict[num]

    return dup_dict

numbers = [1,2,3,2,4,2,5,3]
duplicate_counts = count_duplicates(numbers)
#더 좋은 코드
#딕셔너리 컴프리헨션(꼭 숙지 할 것)
#dup_dict = {num: numbers.count(num) for num in set(numbers)}
print(f"중복 항목: {duplicate_counts}")



#참고 코드

#리스트를 함수에서 수정

def print_models(unprinted_design, completed_models):
    while unprinted_design:
        current_design = unprinted_design.pop()

        print(f"Printing Mode: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been printed:")
    for cm in completed_models:
        print(cm)
        
unprinted_design = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)

print

#리스트를 함수에 전달

def greet_users(names):
    for name in names:
        msg = f"hello, {name.title()}"
        print(msg)

usernames = ['kim inha', 'park inha']
greet_users(usernames)

#반복문에서 함수 호출
def get_formatted_name(first, last):
    fullname = f"{first} {last}"
    return fullname

while True:
    print("\nTell me your name (quit: 'q')")

    f_name = input("First Name:")
    if f_name.lower() == 'q':
        break

    l_name = input("Last Name:")
    if l_name.lower()== 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Hello, {formatted_name}")

#=================================================    

def get_formatted_name(first, last):
    fullname = f"{first} {last}".title(); #단어 앞글자 대문자
    return fullname

def build_person(first, last, age=None):
    person = {'f': first, 'l': last}
    if age:
        person['a'] = age
    return person

#딕셔너리 반환 값
musician_list = []
musician_list.append(build_person('jimi', 'hendrix'))
musician_list.append(build_person('sukjin', 'kim', age=27))

for m in musician_list:
    print(get_formatted_name(m['f'],m['l']))


#단순 반환 값
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#parameter
def describe_pet(type, name):
    print(f"\n나는 {type}라는 동물을 데리고 있어요.")
    print(f"내 {type}의 이름은 {name} 입니다.")

describe_pet('햄스터', '해리')
describe_pet('개', '방울이')
describe_pet('소리', '카나리아')
describe_pet(type='소리', name='카나리아')
describe_pet(name='소리', type='카나리아')
describe_pet('소리', name='카나리아')

def describe_pet2(name, type='개'):
    print(f"\n나는 {type}라는 동물을 데리고 있어요.")
    print(f"내 {type}의 이름은 {name} 입니다.")

describe_pet2('방울이1')
describe_pet2(name='방울이2')
describe_pet2('방울이3',  '햄스터')
describe_pet2(name='방울이4', type='햄스터')
describe_pet2(type='햄스터', name='방울이5')
