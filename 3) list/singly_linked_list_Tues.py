# singly_linked_list.py
#=========================================================
# 코드 3.1: 단순연결구조를 위한 Node 클래스
"""
1. 단순 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드(data)와 다음 노드를 가리키는 링크 필드(link)를 가짐
3. append(node): 현재 노드(self) 뒤에 주어진 새로운 노드(new)를 연결
4. popNext(): 현재 노드의 다음 노드를 리스트에서 제거하고, 그 노드를 반환
"""
# 단순연결구조를 위한 Node 클래스
class Node:
    def __init__(self,elem,link=None):
        self.data = elem # 데이터 필드
        self.link = link # 링크 필드

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
            deleted.link = None # 연결 해제
        return deleted 

# 코드 3.2: 단순연결리스트 클래스
"""
1. 단순 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드:
   - isEmpty(): 리스트가 비어있는지 확인
   - isFull(): 리스트가 가득 찼는지 확인
   - getNode(pos): 특정 위치의 노드를 반환
   - getEntry(pos): 특정 위치의 노드 데이터를 반환
   - replace(pos, elem): 특정 위치의 노드 데이터를 변경
   - size(): 리스트의 크기를 반환
   - display(msg): 리스트의 내용을 출력
   - insert(pos, elem): 특정 위치에 새 노드를 삽입
   - delete(pos): 특정 위치의 노드를 삭제
   - find(elem): 특정 데이터를 가진 노드를 검색
"""
# 단순연결리스트 클래스
class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self) :
        # 리스트가 비어있는지 검사
        return self.head == None

    def isFull(self):
        # 리스트의 포화상태 검사
        return False
    
    def getNode(self, pos):
        # pos번째에 있는 노드를 반환하기
        # 리스트의 인덱스는 0부터 시작
        if pos < 0 : return None # pos는 invalid 졍우
        if self.head == None: # 주어진 리스트가 공백
            return None
        else:
            ptr  = self.head
            for _ in range(pos):
                if ptr == None: # pos가 리스트 크기보다 큰 경우 
                    return None
                ptr = ptr.link # 링크따라 이동
            return ptr #pos에 있는 노드 반환
        
    def getEntry(self, pos):
        # 리스트의 pos 위치에 있는 노드의 데이터를 반환
        node = self.getNode(pos) # getNode() 를 이용하여 pos 위치에 있는 노드 먼저 찾기
        if node == None:
            return None
        else :
            return node.data
        
    def insert(self,pos,elem):
        # 리스트의 pos 위치에 새로운 노드를 추가
        if pos < 0 : return # 자동으로 유효하지않는 위치에 대해 ValueError 발생

        new = Node(elem) # 또는 Node(elem, None) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2. pos-1 위치의 노드를 가져오기
        # 3. before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0 :# 1) 머리 노드로 삽입
                new.link = self.head
                self.head = new
                return
            else: # 2)pos가 리스트의 범위를 벗어나는 경우
                raise IndexError(" 리스트 밖에 있는 위치")
        else: # 3) 중간노드로 삽입
            before.append(new) # before 노드 뒤에 삽입

    def delete(self, pos):
        # 리스트에 pos 위치에 있는 노드 삭제한고 반환
        if pos < 0 : 
            raise IndexError("empty 또는 리스트 범위 밖 오류")
        
        before = self.getNode(pos-1) # 1. 삭제할 노드 이전 노드 
        # 2. before 노드의 위치에 따라 구분
        if before == None:
            if pos == 0 : # 1)머리 노드 삭제
                deleted = self.head
                self.head = deleted.link
                deleted.link = None # 연결 해제
                return deleted
            else: #  2)pos가 리스트 밖에 있는 경우
                raise ValueError("리스트 범위 밖 오류")
        else: 
            before.popNext() # #3) 중간 노드로 삭제 

    def size(self):   
        # 리스트의 전체 노드의 개수 구하기
        if self.head == None : # 리스트가 빈 경우
            return 0        
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.link
            return count 
    
    def display(self, msg = "LinkedList:"):
        print(msg, end = ' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '->')
            ptr = ptr.link
        print("None")

    def replace(self, pos, elem):
        # 리스트의 pos에 있는 노드의 데이터 변경 (QUIZ p.106)
        node = self.getNode(pos) 
        if node != None:
            node.data = elem
        else: 
            return 
 
# 연습문제2: 어떤 요소를 찾아 위치를 반환하는 함수를 정의하기 : 리스트에 없으면 -1 반환, 있으면 그 위치를 정수로 반환
    
   
#=========================================================
# 테스트 프로그램
#=========================================================
def test_code_3_3():
    #1. 연결 리스트 생성
    ll = LinkedList()
    ll.display("연결리스트(초기):   ")      # 출력: LinkedList: None

    #2. 노드 삽입
    ll.insert(0, 10) # 첫 번째 위치에 10 삽입
    ll.display("첫 번째 위치에 10 삽입")
    ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
    ll.display("첫 번째 위치에 20 삽입")
    ll.insert(1, 30)  # 두 번째 위치에 30 삽입
    ll.display("두 번째 위치에 30 삽입")
    ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
    ll.display("마지막 위치에 40 삽입")
    ll.insert(2, 50)  # 세 번째 위치에 50 삽입
    ll.display("세 번째 위치에 50 삽입")
    ll.display("연결리스트(삽입x5): ")     
    ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
    ll.display("연결리스트(교체X1-> 90으로 변경): ")    

    # 3.노드 삭제
    ll.delete(2)      # 세 번째 노드 삭제
    ll.display("세 번째 노드 삭제")
    ll.delete(3)      # 네 번째 노드 삭제
    ll.display("네 번째 노드 삭제")
    ll.delete(0)      # 첫 번째 노드 삭제
    ll.display("첫 번째 노드 삭제")
    ll.display("연결리스트(삭제x3): "   )      

if __name__ == "__main__" :
    test_code_3_3()  
    # test()
    


