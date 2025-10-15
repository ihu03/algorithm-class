# doubly_linked_list.py
#=================================================================
# 코드 3.4 : 이중 연결 구조를 위한 Node 클래스 
"""
1. 이중 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드와 두 개의 링크 필드를 가짐
3. 링크 필드는 각각 이전 노드와 다음 노드를 가리킴
4. 이 구조는 양방향 탐색이 가능하게 함
5. 이중 연결 리스트의 기본 단위로 사용됨
6. 노드 생성 시 데이터와 링크 필드를 초기화
7. 주요 메서드:
    - append(node) : 새로운 노드를 현재 노드 뒤에 삽입
    - popNext() : 현재 노드 뒤에 있는 노드 삭제
"""
class DNode:
   def __init__(self, elem, prev=None,next=None):
      self.data = elem
      self.next = next
      self.prev = prev

   def append(self, new):
      # 현재 노드(self) 다음에 새 노드(new)를 삽입
      if new is not None:
         new.next = self.next
         new.prev = self
         if new.next is not None:
            new.next.prev = new 
         self.next = new

   def popNext(self):
      # 현재 노드 (self)의 다음 노드를 삭제하고 그 노드를 반환
      deleted = self.next
      if deleted is not None:
         self.next = deleted.next
         deleted.next = None # 연결 해제
         if self.next is not None:
            self.next.prev = self
      return deleted
    
#===============================================================================================
# 코드 3.5: 이중연결리스트 클래스
"""
1. 이중 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드: 
    - 동일 연산
        - isEmpty(): 리스트가 비어있는지 확인 
        - isFull(): 리스트가 가득 찼는지 확인
        - getEntry(pos): 특정 위치의 노드 데이터를 반환
    - 연산에서 .link -> .next로 수정
        - getNode(pos): 특정 위치의 노드를 반환 
        - size(): 리스트의 크기를 반환
        - display(msg): 리스트의 내용을 출력
    - 나머지 연산       
        - insert(pos, elem): 특정 위치에 새 노드를 삽입
        - delete(pos): 특정 위치의 노드를 삭제
        - replace(pos, elem): 특정 위치의 노드 데이터를 변경        
"""
class DLinkedList:                       
    def __init__( self ):             
      self.head = None           
    
    def isEmpty( self ):      
       return self.head == None       

    def isFull( self ):     
       return False                  
    
    def getEntry(self, pos) : 
        node = self.getNode(pos)      
        if node == None :              
            return None               
        else :                      
            return node.data 

    def replace(self, pos, elem):
        # 리스트의 pos에 있는 노드의 데이터 변경 (QUIZ p.106)
        node = self.getNode(pos) 
        if node != None:
            node.data = elem
        else: 
            return 
        
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
                ptr = ptr.next # 링크따라 이동
            return ptr #pos에 있는 노드 반환   

    def size(self):   
        # 리스트의 전체 노드의 개수 구하기
        if self.head == None : # 리스트가 빈 경우
            return 0        
        else:
            ptr = self.head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.next
            return count 

    def display(self, msg = "LinkedList:"):
        print(msg, end = ' ')
        ptr = self.head
        while ptr is not None:
            print(ptr.data, end = '<=>')
            ptr = ptr.next
        print("None")

    def  insert(self, pos, elem): 
        # 리스트의 pos 위치에 새 노드 삽입
        if pos < 0 : return
        new = DNode(elem) # 1. 새 노드 생성
        before = self.getNode(pos-1) # 2.  pos-1 위치의 노드 탐색
        if before == None:
            if pos == 0: # 1) 머리노드로 삽입
                new.next = self.head
                if new.next is not None:
                    new.next.prev = new
                self.head = new
                return 
            else : # 2) pos가 리스트의 범위를 초과
                return
        else: # 3) 중간 노드로 삽입
            before.append(new)

    
    def delete(self, pos):
        # pos 위치의 노드를 삭제하고, 그 노드를 반환
        if pos < 0 : return
        before = self.getNode(pos-1) # 1. 삭제 노드 이전 노드 탐색
        if before == None:
            if pos == 0: # 1) 머리노드로 삭제
                deleted = self.head
                if self.head is not None:
                    self.head = deleted.next
                    self.head.prev = None # 새로운 머리 노드의 이전 노드는 None
                    deleted.prev = None # 삭제 노드 연결 해제
                    deleted.next = None # 삭제 노드 연결 해제
                return deleted 
            else : # 2) pos가 리스트 범위 초과
                return
        else: # 3) 중간 노드로 삭제
            before.popNext() 

#=========================================================
# 코드 3.3 단순연결리스트 테스트 프로그램 이용   
#1. 이중 연결 리스트 생성
ll = DLinkedList()
ll.display("연결리스트(초기):   ")      # 출력: LinkedList: None

#2. 노드 삽입
ll.insert(0, 10) # 첫 번째 위치에 10 삽입
ll.insert(0, 20)  # 첫 번째 위치에 20 삽입
ll.insert(1, 30)  # 두 번째 위치에 30 삽입
ll.insert(ll.size(), 40)  # 마지막 위치에 40 삽입
ll.insert(2, 50)  # 세 번째 위치에 50 삽입
ll.display("연결리스트(삽입x5): ")     # 출력: LinkedList: 20->30->50->10->40->None 
ll.replace(2,90) # 세 번째 위치의 노드 데이터를 90으로 변경
ll.display("연결리스트(교체X1-> 90으로 변경): ")     # 출력: LinkedList: 20->30->90->10->40->None

# 3.노드 삭제
ll.delete(2)      # 세 번째 노드 삭제
ll.delete(3)      # 네 번째 노드 삭제
ll.delete(0)      # 첫 번째 노드 삭제
ll.display("연결리스트(삭제x3): "   )      # 출력: LinkedList: 30->10->None

#============================================================
print("연결리스트의 크기= ", ll.size())  # 출력: 연결리스트의 크기= 2
print("2번째 노드의 데이터= ", ll.getEntry(1)) # 출력: 2번째 노드의 데이터= 10
print("1번째 노드의 데이터= ", ll.getEntry(0)) # 출력: 1번째 노드의 데이터= 30
print("3번째 노드의 데이터= ", ll.getEntry(2)) # 출력: 3번째 노드의 데이터= None  


