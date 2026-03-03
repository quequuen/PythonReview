#과제인듯과제아닌


class Score():
    def __init__(self, mid=0, final=0, attend=0, homework=0):
        self.mid = mid
        self.final = final
        self.attend = attend
        self.homework = homework

    def __str__(self):
        return f"{self.mid} / {self.final} / {self.attend} / {self.homework}"

    def total(self):
        return self.mid + self.final + self.attend + self.homework
    
    #0~35점
    def set_mid(self, mid):
        if 0 <= mid <= 35:
            self.mid = mid
        else: 
            print("중간시험 점수는 0~35점 사이어야 합니다.")
    
    #0~35점
    def set_final(self, final):
        if 0 <= final <= 35:
            self.final = final
        else:
            print("기말시험 점수는 0~35점 사이어야 합니다.")
    
    #0~15점
    def set_attend(self, attend):
        if 0 <= attend <= 15:
            self.attend = attend
        else:
            print("출석 점수는 0~15점 사이어야 합니다.")
    
    #0~15점
    def set_homework(self, homework):
        if 0 <= homework <= 15:
            self.homework = homework
        else:
            print("과제 점수는 0~15점 사이어야 합니다.")

    def set_score(self, mid, final, attend, homework):
        if 0 <= mid <= 35:
            self.mid = mid
        if 0 <= final <= 35:
            self.final = final
        if 0 <= attend <= 15:
            self.attend = attend
        if 0 <= homework <= 15:
            self.homework = homework
        else:
            print("올바른 점수를 기입해주세요.")

    def get_grade(self):
        scoreSum = self.mid + self.final + self.attend + self.homework
        grade = ""

        if scoreSum >= 90:
            grade = "A"
        elif scoreSum >= 80:
            grade = "B"
        elif scoreSum >= 70:
            grade = "C"
        elif scoreSum >= 60:
            grade = "D"
        else:
            grade = "F"

        return f"{grade}점"
    

score1 = Score()
score1.set_mid(30)
score1.set_score(30, 30, 10, 8)
print(score1)
print(score1.total())
print(score1.get_grade())