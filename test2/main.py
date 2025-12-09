from datetime import datetime
import os

base_path = "./test2/data"
target_path = base_path + "/student.txt"
date_format = "%Y-%m-%d %H:%M:%S"

# 파일 읽기
def read_info():
    result = {}
    with open(target_path, 'r', encoding = "utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            name, in_time, out_time = line.strip().split("|")
            in_dt = datetime.strptime(in_time.strip(), date_format)

            if out_time.strip() == "None":
                out_dt = None
            else:
                out_dt = datetime.strptime(out_time.strip(), date_format)

            # Record 객체 생성
            r = Record(name, in_dt, out_dt)

            result[r.name] = {
                "입장": in_dt,
                "퇴장": out_dt if out_dt else "없음",
                "머문 시간": r.duration()
            }

    return result


class Record():
    def __init__(self, name, in_time, out_time=None):
        self.name = name
        self.in_time = in_time
        self.out_time = out_time

    # 머문 시간(초) 발생   
    def duration(self):
        out_time = self.out_time if self.out_time is not None else datetime.now() 
        return (out_time - self.in_time).seconds


if not os.path.exists(base_path):
    os.mkdir(base_path)


# 출력
student_list = read_info()

for i, key in enumerate(student_list):
    if len(student_list) == 0:
        break
    output = f"[{i+1}] {key}"
    for key, value in student_list[key].items():
        output += f"{key}:{value} "
    print(output)


# 입력
while True:

    name = input("이름:")
    if name == "":
        break
    in_time = input("입장시간(YYYY-MM-DD HH:MM:SS):").strip()
    in_time = datetime.strptime(in_time, date_format)
    out_time = input("퇴장시간(없으면 Enter):").strip()
    out_time = None if out_time=="" else datetime.strptime(out_time, date_format)

    # print(name, in_time, out_time)

    # 파일 저장
     

    with open(target_path, 'a') as f:
        f.write(f"{name} | {in_time} | {out_time}\n")