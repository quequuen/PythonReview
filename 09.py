# 파일 

# basePath = "/data"
# 이건 절대 경로
basePath = "./data"
# 이게 상대 경로
test01Path = basePath + "/test01.txt"

# f = open(test01Path, 'w')  #쓰기모드
# r 읽기모드
# a 추가모드 : 기존 파일이 있으면 기존 내용에 추가, 없으면 새로 파일을 만듦
# 해당 문법은 꼭 f.close()가 필요함.

#파일처리 with문 사용
with open(test01Path, 'w') as f:
    scores = { '202544016' : {'name': 'Han Ga Yeon', 'github': 'quequuen'} }
    for key, value in scores.items():
        data = f"{key}, {value}\n"
        f.write(data)
 

