#202544016 한가연

def info(name, **kwargs):
    if name is None:
        print("이름은 필수 입력 항목입니다.")
    else:
        if kwargs:
            print(f"{name}의 정보")
            for key, value in kwargs.items():
                print(f"{key}:{value}")
        else:
            print(f"{name}의 정보가 없음")



# info("김인하")
# info("김인하", 취미="독서", 나이=20)
# info("송인하", 키=165)