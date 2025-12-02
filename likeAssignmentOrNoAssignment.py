#과제인듯과제아닌


class Score():
    def __init__(self, mid=0, final=0, attend=0, homework=0):
        self.mid = mid
        self.final = final
        self.attend = attend
        self.homework = homework

    def __str__(self):
        print(f"{self.mid} / {self.final} / {self.attend} / {self.homework}")

    def total(self):
        return self.mid + self.final + self.attend + self.homework
    
    #0~35점
    def set_mid(mid):
        pass
    
    #0~35점
    def set_final(final):
        pass
    
    #0~15점
    def set_attend(attend):
        pass
    
    #0~15점
    def set_homework(homework):
        pass