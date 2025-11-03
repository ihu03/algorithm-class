"""
도서 관리 프로그램 (단순 연결 리스트 기반)
"""


class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None
        return deleted


class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert_end(self, elem):
        new = Node(elem)
        if self.head is None:
            self.head = new
            return
        p = self.head
        while p.link is not None:
            p = p.link
        p.append(new)

    def delete(self, pos):
        if pos < 0 or self.head is None:
            return None
        if pos == 0:
            deleted = self.head
            self.head = deleted.link
            deleted.link = None
            return deleted.data
        before = self.getNode(pos - 1)
        if before is None:
            return None
        deleted = before.popNext()
        return deleted.data if deleted is not None else None

    def getNode(self, pos):
        if pos < 0:
            return None
        i, p = 0, self.head
        while p is not None and i < pos:
            p = p.link
            i += 1
        return p

    def find_by_title(self, title):
        p = self.head
        while p is not None:
            if getattr(p.data, "title", None) == title:
                return p.data
            p = p.link
        return None

    def find_pos_by_title(self, title):
        idx, p = 0, self.head
        while p is not None:
            if getattr(p.data, "title", None) == title:
                return idx
            idx += 1
            p = p.link
        return -1

    def find_by_id(self, book_id):
        p = self.head
        while p is not None:
            if getattr(p.data, "book_id", None) == book_id:
                return p.data
            p = p.link
        return None

    def items(self):
        p = self.head
        while p is not None:
            yield p.data
            p = p.link


class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int):
        self.book_id = int(book_id)
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    def __str__(self):
        return f"[책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판 연도: {self.year}]"


class BookManagement:
    def __init__(self):
        self.books = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.books.find_by_id(book_id) is not None:
            print("동일한 책 번호가 이미 존재합니다. 추가에 실패했습니다.")
            return
        self.books.insert_end(Book(book_id, title, author, year))
        print("도서가 추가되었습니다.")

    def remove_book(self, title):
        pos = self.books.find_pos_by_title(title)
        if pos == -1:
            print("해당 책 제목의 도서를 찾을 수 없습니다.")
            return
        self.books.delete(pos)
        print("도서가 삭제되었습니다.")

    def search_book(self, title):
        b = self.books.find_by_title(title)
        if b is None:
            print("해당 책 제목의 도서를 찾을 수 없습니다.")
        else:
            print(b)

    def display_books(self):
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        for b in self.books.items():
            print(b)

    def _input_int(self, prompt):
        try:
            # int()는 앞뒤 공백을 허용하므로 strip() 없이 처리
            return int(input(prompt))
        except ValueError:
            return None

    def run(self):
        while True:
            print("=== 도서 관리 프로그램 ===")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 종료")
            choice = input("메뉴를 선택하세요: ")

            if choice == "1":
                book_id = self._input_int("책 번호를 입력하세요: ")
                if book_id is None:
                    print("책 번호는 정수여야 합니다.")
                    continue
                title = input("책 제목을 입력하세요: ")
                author = input("저자를 입력하세요: ")
                year = self._input_int("출판 연도를 입력하세요: ")
                if year is None:
                    print("출판 연도는 정수여야 합니다.")
                    continue
                self.add_book(book_id, title, author, year)

            elif choice == "2":
                title = input("삭제할 책 제목을 입력하세요: ")
                self.remove_book(title)

            elif choice == "3":
                title = input("조회할 책 제목을 입력하세요: ")
                self.search_book(title)

            elif choice == "4":
                self.display_books()

            elif choice == "5":
                print("프로그램을 종료합니다.")
                break
            else:
                print("올바른 메뉴 번호를 선택하세요.")
            print()


if __name__ == "__main__":
    BookManagement().run()

