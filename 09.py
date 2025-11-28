# 파일 
import os 

# basePath = "/data"
# 이건 절대 경로
basePath = "./data"
# 이게 상대 경로
test01Path = basePath + "/test01.txt"

# f = open(test01Path, 'w')  #쓰기모드
# r 읽기모드
# a 추가모드 : 기존 파일이 있으면 기존 내용에 추가, 없으면 새로 파일을 만듦
# 해당 문법은 꼭 f.close()가 필요함.

# 숫자 판별 함수
def isNumber(value):
    try:
        float(value)
        return value != "" and value is not None
    except (ValueError, TypeError):
        return False

if not os.path.isfile(test01Path):
    #파일처리 with문 사용
    with open(test01Path, 'w') as f:
        scores = { '202544016' : {'name': 'Han Ga Yeon', 'github': 'quequuen'}, '202540001' : {'name': 'Han Yeon', 'github': 'queqen'} }
        for key in scores.keys():
            data = f"{key}\n"
            f.write(data)
            for subkey, value in scores[key].items():
                data = f"   {value}\n"
                f.write(data)
 
result = {}
snum = 0
with open(test01Path, 'r') as f:
   
        while True:
            line = f.readline()
            # 여러 줄을 readline로 읽는 거라서 while True임
            if not line:
                break
            data = line.strip()
            if(len(data)==9 and isNumber(data)):
                snum = int(data)
                result[snum] = []
            else: 
                result[snum].append(data) 



print(result)