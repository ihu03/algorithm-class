# circular_queue_class.py
######################

class CircularQueueOneSlotEmpty:
    """
    원형 큐 (one-slot-empty 방식)
    - 외부에서 지정한 capacity 만큼 '실제'로 담을 수 있음
    - 내부 배열은 capacity + 1 크기로 잡아 한 칸을 비워 둠
    - front: '첫 번째 요소'의 인덱스 바로 이전 위치
    - rear:  '맨 마지막 요소'의 인덱스
    """
    def __init__(self,capacity):
        self.capacity = capacity
        self.N = self.capacity + 1 # 내부 배열 크기 (단, 배열의 한칸(슬롯) 비움)
        self.array = [None] * self.N
        self.front = 0
        self.rear = 0 

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.N
    
    def enqueue(self,item):
        # 맨 뒤에 요소를 추가
        if not self.is_full() :
            self.rear = (self.rear + 1) % self.N
            self.array[self.rear] = item
        else:
            print("원형큐가 포화 상태-> 요소 삽입 불가")

    def dequeue(self):
        # 맨 앞의 요소를 삭제
        if not self.is_empty():
            self.front = (self.front + 1) % self.N
            item = self.array[self.front]
            self.array[self.front] = None # 옵션
            return item
        else:
            raise IndexError("원형큐가 비어있음-> 삭제 불가")
        
    def peek(self):
        # 현재 원형 큐에 저장된 맨 앞의 요소를 검색
        if not self.is_empty():
            return self.array[(self.front + 1) % self.N]
        else:
            raise IndexError("원형큐가 비어있음")
        
    def size(self):
        # 현재 원형큐에 저장되어 있는 요소의 총 개수
        return (self.rear - self.front + self.N) % self.N   
   
    def display(self, msg="CircularQueueOneSlotEmpty"):
        
        print(f"{msg}: front={self.front}, rear={self.rear}, size={self.size()}/{self.capacity}")

        # 1) 논리 순서(front 다음부터 size개)로 아이템 나열
        items = [] 
        idx = (self.front + 1) % self.N
        for _ in range(self.size()):
            items.append(self.array[idx])
            idx = (idx + 1) % self.N
        print("items =", items)

        # 2) 슬롯별 시각화: 빈 칸은 None, 채워진 칸은 값 (랩어라운드 고려)
        print("slots=[", end="")
        for i in range(self.N):
            if self.front < self.rear:
                # 연속 구간: (front, rear] 가 활성
                occupied = (self.front < i <= self.rear)
            else:
                # 랩어라운드 구간: (front, N-1] ∪ [0, rear]
                occupied = (i > self.front) or (i <= self.rear)
            
            if occupied and not self.is_empty():
                val = self.array[i]
            else:
                val = None
            
            print(val, end="   ")
            
        print("]")

  
# ----------------------------
#  원형 큐 테스트 프로그램
# ----------------------------
def test_basic():
    # code 2.2: 논리적 순서(front → rear)로 큐 내용을 보기 
    import random
    random.seed(1)
    # test_basic() : 가득 채우기 → 전부 비우기 → 다시 1개 넣기
    print("\n=== test_basic ===")
    q = CircularQueueOneSlotEmpty(capacity=8)
    q.display("초기 상태") # front=rear=0
    print()

    # 가득 채우기   
    while not q.is_full():
        q.enqueue(random.randint(0, 100))
    q.display("포화 상태")
    print()

    # 다시 1개 넣기 ===> overflow 발생 -> 삽입 실패 
    q.enqueue(777)
    q.display()
    print("peek:", q.peek())
    print()

    # 전부 비우기
    print("삭제순서: ", end="")
    while not q.is_empty():
        print(q.dequeue(), end=" ")
    q.display("모두 제거 후") # front == rear != 0 (False Full, 즉 거짓 포화 문제 해결)
    print()

    # 다시 1개 넣기
    print("비어있는 상태에서 삽입 시도!!")
    q.enqueue(777)
    q.display()
    print("peek:", q.peek())
     
def quiz_2():
    # 1. capacity = 8인 원형큐
    print("============Quiz_2============")
    q = CircularQueueOneSlotEmpty(capacity=8)
    # 2. front = rear = 6
    q.front = 6
    q.rear = 6
    # 연산 처리
    q.enqueue(10)
    q.display("10 삽입 결과")
    q.enqueue(11)
    q.display("11 삽입 결과")
    q.enqueue(12)
    q.display("12 삽입 결과")
    q.enqueue(13)
    q.display("13 삽입 결과")
    q.dequeue()
    q.display("삭제 결과")
    q.dequeue()
    q.display("삭제 결과")
    # front = ? , rear = ?
    print(f"front={q.front}, rear={q.rear}")

if __name__ == "__main__":
    # test_basic()
    quiz_2()
    
