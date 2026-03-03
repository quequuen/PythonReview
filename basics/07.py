#함수
#입력을 받아서 특정 작업을 수행하고, 해당 결과를 반환하는 블랙 박스와 같은 역할을 한다.
#return이 전달하는 결과값은 Only one. 두개처럼 보이는 것은 tuple의 형태로 반환을 함.
#주의!
#코드 작성시 함수 정의 호출보다 반드시 먼저 기술할 것 .


#사용하는 이유
#1. 반복적으로 사용하는 가치 있는 부분을 묶어서 사용하는 것
#2. 전체 흐름을 단계적으로 만든다.

#가변 매개변수 2
#밑의 가변 매개변수와 달리 key=값 형태로 인수를 전달
#keyword arguments packing(키워드 인자 패킹)
def build_profile(first, last, **userinfo):
    print(f"{last} {first}의 추가 정보는 아래와 같습니다.")
    print(" 활동지역 : ", userinfo.get('loc', '정보없음'))
    print(f" 분야 : {userinfo.get('field', '정보없음')}")

build_profile('albert', 'einstein', loc = 'princeton')
build_profile(last = 'kim', first='inha', loc = 'incheon', field = 'cs')
build_profile('inha', 'lee', loc='incheon', field='lg')
    

#가변 매개변수(*args) positional arguments packing
#인수의 개수가 정해져 있지 않는 경우에 사용.

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    
    elif choice == "mul":
        result = 1
        for i in args:
            result += i
    else:
        result = None
    return result

a = add_mul("add", 1, 2, 3)
b = add_mul("mul", 1, 2, 3, 4, 5, 5)


#함수 변수 범위(중요!!!!)
a = 1 #전역변수

def vartest(a): # 지역변수, 호출 시 넘어온 값을 가리킴
    a = a + 1   # 지역변수, a가 가리키는 값에 1을 저장하고, 그 결과를 다시 a로 가리킴.
#지역변수 a의 값을 전역변수 a로 넣고 싶으면, 지역변수 a의 값을 return 하는 것과
#global 키워드를 사용하는 방식이 있는데 global은 신중히 써야 함.
    

vartest(a)  # vartest()에게 a가 가리키는 1의 위치를 넘김
print(a)    # 전역변수 a를 출력



def test(a, b, c, d=10):
    print(a, b, c, d)

#기본값 매개변수 default value argument
test(1,2,3)
#d는 기본값인 10을 출력

#키워드 매개변수 keyword argument
test(b=2, a=1, c=3, d=4)

#위치형 매개변수 positional argument
test(1,2,3,4)



#함수 기본

def add1(a, b):
    result = a+b
    return result


