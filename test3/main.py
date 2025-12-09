from datetime import datetime as dt
import os

student = {}
base_path = "./test3/data"
target_path = base_path + "/student.txt"

class Student():
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        sum = 0
        for score in self.scores.values():
            sum += score
        return sum/len(self.scores)

    def to_string(self):
        result = f"{self.name}|"
        for subject, score in self.scores.items():
            result += f"{subject}:{score},"
        return result[:-1] 


# 파일 저장 함수

def save_file(stu):

    if not os.path.exists(target_path):
        os.mkdir(base_path)

    with open(target_path, 'a', encoding="utf-8") as f:
        write_str = stu.to_string()+ "\n"
        f.write(write_str)


# 파일 읽기 함수

def read_info():
    with open(target_path, 'r', encoding="utf-8") as f:
        
        while True:
            scores = {}
            line = f.readline()
            if not line:
                break

            name, data = line.strip().split("|")
            score_data = data.strip().split(",")


            for value in score_data:
                subj, score = value.strip().split(":")
                scores[subj] = int(score)

            stu = Student(name, scores)
            avg = stu.average()

            print(f"{stu.name} 평균: {avg:.1f}")

# 출력
read_info()

# 입력
while True:
    name = input("이름:").strip()
    
    if name == "":
        break
    # 데이터 배열이나 딕셔너리 초기화 위치 중요
    scores = {}
    while True:
        subj = input("과목명:").strip()
        if subj == "":
            break

        score = input("점수:")
        score = int(score)
        scores[subj] = score
        student[name]= scores
        print("-> 종료하려면 엔터")
    print("-> 종료하려면 엔터")



#파일 저장
for name in student.keys():
    stu = Student(name,student[name])
    save_file(stu)


        


        