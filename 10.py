# 클래스와 매직 메소드

# 파이썬의 모든 자료형을 class로 만든다.
# 클래스 정의 연습
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle1():
    def __init__(self, x, y, w, h):
        point = Point(x, y)
        self.w = w
        self.h = h

class Rectangle2():
    def __init__(self, point, w, h):
        self.point = point
        self.w = w
        self.h = h


point = Point(1,2)
r = Rectangle2(point, 1, 2)
print(f"{r.point.x}")
print(f"{r.point.y}")


class Rectangle3():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


class Subject():
    def __init__(self, num, name, grage):
        self.num = num
        self.name = name
        self.grage = grage

class Section():
    def __init__(self, subject, teacher, ban, room, time):
        self.subject = subject
        self.teacher = teacher
        self.ban = ban
        self.room = room
        self.time = time

class Student():
    def __init__(self, name, snum, spec, birth):
        self.name = name
        self.snum = snum
        self.spec = spec
        self.birth = int(birth)

    def __str__(self):
        # 객체를 인쇄 가능한 형식으로 사용할 때 자동 실행
        # print(student)
        return f"이름: {self.name} 학번: {self.snum} 생년: {self.birth} 전공: {self.spec}" 

students = []

for i in range(3):
    answer = input("학생 정보 입력(이름/학번/학과/생년): ")

    if answer == "":
        break

    name, snum, spec, birth = answer.split('/') 

    student = Student(name, snum, spec, birth)  
    students.append(student)                    

stuA = Student("A", "01", "컴퓨터정보", 2005)
# stuB = Student("B", "02", 3, "시각디자인", 2003)
# stuC = Student("C", "03", 2, "건축학과", 2000)

# print(stuA.name)
# print(stuB.name)
# print(stuC.name)

print(stuA)



    

