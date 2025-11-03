#===========================================================
# 코드 3.4 : 이중 연결 구조를 위한 Node 클래스 
"""
1. 이중 연결 구조를 위한 Node 클래스
2. 각 노드는 데이터 필드와 두 개의 링크 필드를 가짐
3. 링크 필드는 각각 이전 노드와 다음 노드를 가리킴
4. 이 구조는 양방향 탐색이 가능하게 함
5. 노드 생성 시 데이터와 링크 필드를 초기화
7. 링크 필드는 기본적으로 None으로 설정
8. 주요 메서드:
    - append(node) : 새로운 노드를 현재 노드 뒤에 삽입
    - popNext() : 현재 노드 뒤에 있는 노드 삭제
"""
# 이중연결 Node 클래스

class DNode:
    def __init__(self,elem, prev=None, next=None):
        self.data = elem #데이터 필드
        self.prev = prev #이전 노드를 가리키는 링크 필드
        self.next = next #다음 노드를 가리키는 링크 필드

    def append(self, new): #노드 기반 삽입 연산 
        #현재 노드 (self)의 다음 노드로 새 노드 (new) 삽입
        if new is not None:
            new.next = self.next # new의 다음 노드  self 노드의 다음 노드 
            new.prev = self # new의 이전 노드는 self 노드
            if new.next is not None:
                new.next.prev = new
            self.next = new

    def popNext(self): #노드 기반 삭제 연산
        #현제 노드 (self)의 다음 노드 삭제 
        deleted = self.next
        if deleted is not None:
            self.next = deleted.next
            deleted.next = None #연결 헤제
            if self.next is not None:
                self.next.prev = self
        return deleted









#=========================================================
# 코드 3.5: 이중연결리스트 클래스
"""
1. 이중 연결 리스트 구조를 관리하는 클래스
2. head: 리스트의 첫 번째 노드를 가리키는 포인터
3. 주요 메서드: 
동일연산
    - isEmpty(): 리스트가 비어있는지 확인
    - isFull(): 리스트가 가득 찼는지 확인
    - getNode(pos): 특정 위치의 노드를 반환
    - getEntry(pos): 특정 위치의 노드 데이터를 반환
    - replace(pos, elem): 특정 위치의 노드 데이터를 변경
연산에선 .link-> .next로 수정 
    - getNonde(pos): 특정 위치의 노드를 반환
    - size(): 리스트의 크기를 반환
    - display(msg): 리스트의 내용을 출력
나머지 연산 
    - insert(pos, elem): 특정 위치에 새 노드를 삽입
    - delete(pos): 특정 위치의 노드를 삭제
    - find(elem): 특정 데이터를 가진 노드를 검색
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

    def replace(self, pos, elem) : 
        node = self.getNode(pos)       
        if node != None :       
          node.data = elem          
        else :                 
            return None  
        
    def getNode(self, pos): #pos 기반 연산
        #pos 위치에 있는 노드를 반환 
        #pos는 리스트의 인덱스 0부터
        if pos < 0: return None # pos는 유효하지 않은 위치
        if self.head == None: #리스트가 빈상태
            return None
        else:
            ptr = self.head 
            for _ in range(pos):
                if ptr == None: #pos가 리스트보다 크기가 큰 경우
                    return None
                ptr = ptr.next
            return ptr 
        
    def size(self):
        # 리스트의 전체 노드의 개수
        if self.head == None: #리스트가 빈 상태
            return 0
        else:
            ptr = self. head
            count = 0
            while ptr is not None:
                count += 1
                ptr = ptr.next
            return count
        
    def display(self, msg = "DLinkedList: "):
        #리스트의 모든 노드 데이터 출력
        print(msg, end='')
        if self.head == None:
            return None
        else:
            ptr = self.head
            while ptr is not None:
                print(ptr.data, end=' <-> ')
                ptr = ptr.next
            print("None")

    def insert(self, pos, elem): #인덱스 기반 연산
        #pos 위치에서 새 노드(elem)를 삽입
        if pos < 0:
            raise ValueError("잘못된 위치 값!")
        new = DNode(elem) #1. 새 노드 생성
        before = self.getNode(pos-1) #2. pos-1 위치의 노드 탐색
        #before 노드의 위치에 따라 구분
        if before is None:
            if pos == 0: #머리 노드로 삽입
                new.next = self.head
                if new.next is not None:
                    new.next.prev =new #new 노드의 다음 노드의 이전 노드는 new
                self.head = new #머리 노드을 new 로 갱신 
                return
            else: #2) pos 가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않습니다")
        else: #3) 중간노드 삽입
            before.append(new) #before 노드 뒤에 new 노드 삽입

    def delete(self, pos): #인덱스 기반 연산
        #pos 위치에서 해당 노드 삭제 연산 
        if pos <0 :
            raise ValueError("잘못된 위치 값!")
        before = self.getNode(pos-1) # 1. 삭제 노드 이전의 노드 탐색 
        #2. before 노드의 위치에 따라 구분
        if before == None: 
            if pos == 0: # 1)머리 노드를 삭제 
                deleted = self.head
                if self.head is not None:
                    self.head = deleted.next
                    self.head.prev = None
                    deleted.prev = None #연결 해제
                    deleted.next = None #연결 해제 
                return deleted.data
            else: # 2) pos가 리스트 범위에서 벗어남
                raise IndexError("삽입할 위치가 유효하지 않습니다")
            
        else: # 3) 중간 노드로 삭제
            return before.popNext()

 
    
    
    

    

#=========================================================
# 코드 3.3 단순연결리스트 테스트 프로그램   
#========================================================
#1. 연결 리스트 생성
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

