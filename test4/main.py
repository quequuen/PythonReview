import os
from datetime import datetime as dt, timedelta

dt_format = "%Y-%m-%d %H:%M:%S"
base_path = "./test4/data"
target_path = base_path + "/books.txt"


if not os.path.exists(base_path):
    os.mkdir(base_path)

class Book():
    def __init__(self, title, author, is_rented = False, due_date = None):
        self.title = title
        self.author = author
        self.is_rented = is_rented
        self.due_date = due_date

    def to_string(self):
        return f"{self.title}|{self.author}|{self.is_rented}|{"" if self.due_date==None else dt.strftime(self.due_date, dt_format)}\n"

class Library():
    def __init__(self):
        self.books = []
    # 책 정보 파일 저장
    def save_books(self):
        print(self.books)
        with open(target_path, 'w', encoding= "utf-8") as f:
            for book in self.books:
                f.write(book.to_string())


    def print_books(self):
        for i,book in enumerate(self.books):
            print_str = f"[{i+1}] {book.title} - "
            if book.is_rented:
                print_str += f"대여 중 (반납예정: {book.due_date})"
            else:
                print_str += f"대여 가능"
            print(print_str)
    
    # 책 목록 출력
    def load_books(self):
        if not os.path.exists(target_path):
            print("파일이 존재하지 않습니다.")
            return []
        with open(target_path, 'r', encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line:
                    break
                title, author, is_rented, due_date = line.strip().split("|")
                print(title, author, is_rented, due_date)
                book = Book(title, author, is_rented = (is_rented == "True"), due_date = None if due_date == "" else dt.strptime(due_date, dt_format))
                self.books.append(book) 
    
    # 책 대여
    def rent_book(self, title):
        for book in self.books:
            if title == book.title:
                if book.is_rented:
                    print("이미 대여 중입니다.")
                    return
                
                book.is_rented = True
                book.due_date = dt.now() + timedelta(days=7)
                print("대여 완료!")

                return
        print("책을 찾을 수가 없습니다.")

    # 책 반납
    def return_book(self, title):
        for book in self.books:
            if title == book.title:
                if not book.is_rented:
                    print("이 책은 대여 상태가 아닙니다.")
                book.is_rented = False
                book.due_date = None
                print("반납 완료!")
                return
            
        print("책을 찾을 수 없습니다.")

lib = Library()
lib.load_books()


while True:
    print("===== 도서 대여 시스템 =====")
    print("1. 책 목록 보기")
    print("2. 책 대여")
    print("3. 책 반납")
    print("4. 종료")
    answer = input("메뉴 선택:")

    # 파이썬은 match-case에서 break 하면 프로그램이 무한반복 되지 않음
    match answer:
        case "1":
            lib.print_books()
        case "2":
            print("대여")
            title = input("대여할 책 제목 입력:")
            lib.rent_book(title)
        case "3":
            print("반납")
            title = input("반납할 책 제목 입력:")
            lib.return_book(title)
        case "4":
            lib.save_books()
            break


