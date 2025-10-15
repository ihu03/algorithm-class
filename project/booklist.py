# =========================================================
# 도서 관리 프로그램 (단순 연결 리스트)
# 작성자 : 20220808 이승후
# 메뉴: 1. 도서 추가
#       2. 도서 삭제(책 제목으로)
#       3. 도서 조회(책 제목으로)
#       4. 전체 도서 목록 출력
#       5. 종료
# =========================================================

# ---------------------------
# 단순연결구조를 위한 Node 클래스
# ---------------------------
class Node:
    def __init__(self, elem, link=None):
        # elem: 이 노드가 담을 데이터(여기서는 Book 객체)
        # link: 다음 노드의 참조(처음엔 None)
        self.data = elem
        self.link = link

    def append(self, new):
        # 현재 노드 (self) 뒤에 새로운 노드 (new)를 추가하는 연산
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        # 현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
        deleted = self.link
        if deleted is not None:
            self.link = deleted.link
            deleted.link = None  # 연결 해제
        return deleted


# ---------------------------
# 단순연결리스트 클래스
# ---------------------------
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        # 리스트가 비어있는지 검사
        return self.head == None

    def isFull(self):
        # 리스트의 포화상태 검사
        return False

    def getNode(self, pos):
        # pos번째에 있는 노드를 반환하기
        # 리스트의 인덱스는 0부터 시작
        if pos < 0 : return None
        ptr = self.head
        for _ in range(pos):
            if ptr is None:
                return None
            ptr = ptr.link
        return ptr

    def getEntry(self, pos):
        # pos 위치의 노드 데이터(Book) 반환, 없으면 None
        node = self.getNode(pos)
        return None if node is None else node.data

    def insert(self, pos, elem):
        """
        pos 위치에 새 원소(elem)를 삽입.
        pos == 0 : 머리 삽입
        pos  > 0 : pos-1 노드 뒤에 삽입(append 사용)
        유효하지 않거나 범위를 벗어나면 IndexError
        """
        if pos < 0:
            raise IndexError("유효하지 않은 위치입니다.")
        new = Node(elem)
        before = self.getNode(pos - 1)
        if before is None:
            if pos == 0:
                new.link = self.head
                self.head = new
            else:
                raise IndexError("리스트 범위를 벗어난 위치입니다.")
        else:
            before.append(new)

    def delete(self, pos):
        """
        pos 위치의 노드를 삭제하고 '삭제된 노드(Node)'를 반환.
        머리 삭제: pos == 0
        중간 삭제: pos > 0 -> pos-1 노드가 필요
        """
        if pos < 0:
            raise IndexError("유효하지 않은 위치입니다.")
        before = self.getNode(pos - 1)
        if before is None:
            if pos == 0:
                if self.head is None:
                    raise IndexError("빈 리스트입니다.")
                deleted = self.head
                self.head = deleted.link
                deleted.link = None
                return deleted
            else:
                raise IndexError("리스트 범위를 벗어난 위치입니다.")
        else:
            deleted = before.popNext()
            if deleted is None:
                raise IndexError("리스트 범위를 벗어난 위치입니다.")
            return deleted

    def size(self):
        # 전체 노드 개수 카운트
        cnt, ptr = 0, self.head
        while ptr is not None:
            cnt += 1
            ptr = ptr.link
        return cnt

    def replace(self, pos, elem):
        # pos 위치의 노드 데이터를 elem으로 교체
        node = self.getNode(pos)
        if node is not None:
            node.data = elem

    def find_by_title(self, title):
        """
        '책 제목'으로 순회, 첫 번째로 일치하는 Book을 반환. (없을시 noen)
        """
        ptr = self.head
        while ptr is not None:
            if hasattr(ptr.data, "title") and ptr.data.title == title:
                return ptr.data
            ptr = ptr.link
        return None

    def find_pos_by_title(self, title):
        """
        '책 제목'으로 순회, 첫 번째로 일치하는 노드의 위치(pos) 반환. (없을시 -1)
        """
        idx, ptr = 0, self.head
        while ptr is not None:
            if hasattr(ptr.data, "title") and ptr.data.title == title:
                return idx
            idx += 1
            ptr = ptr.link
        return -1


# ---------------------------
# Book 데이터 객체
# ---------------------------
class Book:
    """
    book_id: 정수 ID(중복 금지)
    title:   책 제목(문자열)
    author:  저자(문자열)
    year:    출판 연도(정수)
    """
    def __init__(self, book_id, title, author, year):
        # 타입 안전을 위해 생성자에서 최소한의 형 변환
        self.book_id = int(book_id)
        self.title = str(title)
        self.author = str(author)
        self.year = int(year)

    # 목록·결과 표시에 사용할 통일된 문자열 표현
    def to_pretty(self):
        # 이미지 예시의 대괄호 및 라벨 표기 형식에 맞춤
        return "[책 번호: {}, 제목: {}, 저자: {}, 출판 연도: {}]".format(
            self.book_id, self.title, self.author, self.year
        )

    def __str__(self):
        # 단일 라인 표현(삭제 성공 메시지 등에 사용)
        return "[{}] {} / {} / {}".format(
            self.book_id, self.title, self.author, self.year
        )


# ---------------------------
# 책 관리 프로그램 UI
# ---------------------------
class BookManagement:
    """
    LinkedList에 Book을 저장하고, 사용자 입력을 받아 기능 실행
    '추가' 시 book_id 중복 금지
    '조회/삭제'는 '첫 번째로 일치하는 제목'에 대해 동작
    """
    def __init__(self):
        self.books = LinkedList()

    # ---- 단순 순회로 book_id 중복 체크 ----
    def _exists_id(self, book_id):
        ptr = self.books.head
        while ptr is not None:
            if hasattr(ptr.data, "book_id") and ptr.data.book_id == book_id:
                return True
            ptr = ptr.link
        return False

    # ---- 리스트 끝에 삽입 ----
    def _append_book(self, book):
        n = self.books.size()      # 현재 크기 = 꼬리 다음 위치
        self.books.insert(n, book) # O(n) 횟수의 순회 + O(1) 삽입

    # ---------------- 공개 API ----------------
    def add_book(self, book_id, title, author, year):
        # 1) ID 중복 방지
        if self._exists_id(book_id):
            print("도서 추가 실패: 이미 존재하는 책 번호입니다.")
            return

        # 2) Book 생성 및 리스트 끝에 삽입
        try:
            book = Book(book_id, title, author, year)
            self._append_book(book)
            # 이미지 예시와 맞춘 문구: "도서 '제목'가 추가되었습니다."
            # (조사 '이/가' 자동 판별은 생략, 단순 '가' 고정)
            print("도서 '{}'가 추가되었습니다.".format(title))
        except Exception as e:
            print("도서 추가 실패: {}".format(e))

    def remove_book(self, title):
        # 1) 제목으로 위치 검색
        pos = self.books.find_pos_by_title(title)
        if pos == -1:
            print("삭제 실패: 해당 제목의 도서가 없습니다.")
            return

        # 2) 해당 위치 삭제
        try:
            self.books.delete(pos)
            # 이미지 예시와 맞춘 문구
            print("책 제목 '{}'의 도서가 삭제되었습니다.".format(title))
        except Exception as e:
            print("삭제 실패: {}".format(e))

    def search_book(self, title):
        # 제목으로 Book 검색
        book = self.books.find_by_title(title)
        if book is None:
            print("조회 실패: 해당 제목의 도서가 없습니다.")
        else:
            # 이미지 예시에 맞춘 1줄 결과 출력
            print(book.to_pretty())

    def display_books(self):
        # 공백 처리
        if self.books.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return

        # 이미지 예시 문구: "현재 등록된 도서 목록:"
        print("현재 등록된 도서 목록:")
        # 연결 리스트를 앞에서 뒤로 순회하며 한 줄씩 출력
        ptr = self.books.head
        while ptr is not None:
            b = ptr.data
            print(b.to_pretty())
            ptr = ptr.link

    # ---------------- 메뉴 UI ----------------
    def run(self):
        """
        무한 루프에서 메뉴 출력 -> 입력 받은 후 각 기능 실행
        잘못된 입력(정수 아님 등)은 메시지 출력 후 메뉴로 복귀
        """
        # 한 번에 재사용할 메뉴 문자열
        MENU = (
            "=== 도서 관리 프로그램 ===\n"
            "1. 도서 추가\n"
            "2. 도서 삭제 (책 제목으로 삭제)\n"
            "3. 도서 조회 (책 제목으로 조회)\n"
            "4. 전체 도서 목록 출력\n"
            "5. 종료\n"
            "메뉴를 선택하세요: "
        )

        while True:
            try:
                # 1) 메뉴 표기 및 선택 입력
                choice = input(MENU).strip()

                # 2) 분기 처리
                if choice == '1':
                    # --- 도서 추가 ---
                    # 정수 입력 검증: book_id, year
                    try:
                        book_id = int(input("책 번호를 입력하세요: ").strip())
                    except ValueError:
                        print("입력 오류: 책 번호는 정수여야 합니다.")
                        continue

                    title = input("책 제목을 입력하세요: ").strip()
                    author = input("저자를 입력하세요: ").strip()

                    try:
                        year = int(input("출판 연도를 입력하세요: ").strip())
                    except ValueError:
                        print("입력 오류: 출판 연도는 정수여야 합니다.")
                        continue

                    self.add_book(book_id, title, author, year)

                elif choice == '2':
                    # --- 도서 삭제(제목) ---
                    title = input("삭제할 책 제목을 입력하세요: ").strip()
                    self.remove_book(title)

                elif choice == '3':
                    # --- 도서 조회(제목) ---
                    title = input("조회할 책 제목을 입력하세요: ").strip()
                    self.search_book(title)

                elif choice == '4':
                    # --- 전체 도서 목록 출력 ---
                    self.display_books()

                elif choice == '5':
                    # --- 종료 ---
                    print("프로그램 종료.")
                    break

                else:
                    # 메뉴 번호가 1~5 가 아닌 경우
                    print("1부터 5 사이의 번호를 입력하세요.")

                print()

            except Exception as e:
                # 디버깅메세지
                print("오류가 발생했습니다: {}".format(e))
                print()


# ---------------------------
# 실행부
# ---------------------------
if __name__ == "__main__":
    # 프로그램 객체를 생성하고 바로 실행
    app = BookManagement()
    app.run()
