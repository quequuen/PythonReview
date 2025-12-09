#202544016 한가연

from datetime import datetime

class Book:
    # 미대출 책은 대여자와 대여일은 None
    # 해당 정보는 매개변수를 통해 받아옴
    def __init__(self, name, rentname = None, rentdate = None):
        self.name = name
        self.rentname = rentname
        self.rentdate = rentdate

    # 대여기간을 반환/ 대여안함:None, 대여중: (현재시간-대여시간).days
    def rentterm(self):
        
        return None if self.rentdate is None else (datetime.now() - self.rentdate).days

    # 연체여부 판단/ 대출중이 아니거나 연체중이 아닌 경우 False 반환, 7일을 초과한 경우 True 반환    
    def isoverdue(self, baseday=7):

        if self.rentdate is not None:
            return False
        self.overduedate = self.rentterm() + baseday
        overdue = False if self.overduedate >= datetime.now() else True

        return overdue 

    # 연체일수 반환/ 대출기한이 7일을 초과한 경우 초과한 날짜를 반환, 그 외의 경우는 0 반환
    def overdueday(self, baseday=7):
        overdue = 0
        if self.isoverdue(baseday):
            overdue = self.rentterm() - baseday
        
        return overdue


    def __str__(self):
        if self.rentname is None:
            return f"[대여가능]{self.name}"

        rentable = "대여가능" if self.rentname is None else "대여불가"
        return f"[{rentable}]{self.name} 대출자:{self.rentname} 대출일:{self.rentdate}"

# b1 = Book("두근두근 JS", None, None)
# b2= Book("C#정복", '이인하', datetime.now())
# print(b1)
