#202544016 한가연

import os
from book import Book



def readinfo():
    target_path = "books.csv"
    result = []
    with open(target_path, "r", encoding="utf-8") as f:
        while True:
            line =f.readline()
            if not line:
                break
            data = line.strip().split(",")
            name = data[0]
            rentname = data[1] if len(data) == 3 else None
            rentdate = data[2] if len(data) ==3 else None
            result.append(Book(name, rentname, rentdate))

    return result


book_list = readinfo()

if not book_list:
    print("도서정보가 없습니다.")

else:
    for i, v in enumerate(book_list):
        print(i+1, v)