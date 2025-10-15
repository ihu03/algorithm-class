# circularDequeue_class.py
#=============================================================================================
# 원형덱 특징 :
# - 시간 복잡도: 모든 연산 O(1)
# - 원형 큐를 기반으로 구현 (one-slot-empty 방식)
# - front, rear 포인터를 % 연산으로 시계방향/반시계방향으로 순환시켜 사용
# - enqueue, dequeue 시 포인터를 % N 연산으로 순환시켜 사용
# - 단점:
# 1) 실제 담을 수 있는 최대 개수가 capacity - 1 로, 한 칸이 비어 있어야 함 
# 2) 원형 덱은 선형 큐의 “거짓 포화(false full)”를 없앨 뿐, 용량을 초과해서 담을 때 overflow가 발생\
#    (동적 배열을 사용하거나, 덮어쓰기 기능이 있는 링버퍼를 사용해야 함)    
# 원형 덱 구현 : 
# - 원형 큐 (one-slot-empty 방식)을 상속하여 원형 덱 클래스 구현
# - circular_queue_class.py 에 있는 CircularQueueOneSlot 상속
# - 덱의 전단 : add_front, delete_front, get_front 연산은 각각 큐의 enqueue, dequeue, peek와  동일
# - 덱의 후단 : add_rear, delete_rear, get_rear 연산은 각각 스택의 push, pop, peek과 동일
# - 덱의 add_front, delete_rear, get_rear 연산은 별도 구현 필요

from circular_queue_class import CircularQueueOneSlotEmpty

class CircularDeque(CircularQueueOneSlotEmpty):
    def __init__(self, capacity):
        super().__init__(capacity)

    """
    self.is_empty(), self.is_full(), self.size(), self.display() \
    위의 연산들 : 상속을 통해 그대로 사용
    """
    def delete_front(self): # 전단에서 삭제 
        return self.dequeue() # 부모 메서드 호출
    
    def get_front(self): # 전단에서 검색
        return self.peek() # 부모 메서드 호출
    
    def add_rear(self, item): # 후단에서 삽입
        return self.enqueue(item) #부모 메서드 호출
    
    # Dequeue에만 있는 연산 : 자식 클래스에서 구현
    def add_front(self,item): # 전단에서 삽입
        if self.is_full():
            raise IndexError("덱이 포화 상태 -> 삽입 불가")
        else:
            self.array[self.front]= item
            self.front = (self.front - 1+ self.N) % self.N # front 를 반시계반향으로 한 칸 회전
    
    def delete_rear(self): #후단에서 삭제
        if self.is_empty():
            raise IndexError("덱이 빈 상태 -> 삭제 불가")
        else:
            item = self.array[self.rear] # rear포인터는 마지막 요소을 가리킴
            self.array[self.rear] = None
            self.rear = (self.rear -1 + self.N) % self.N
            return item  #반환
    
    def get_rear(self): # 후단에서 최근 자료 검색
        if self.is_empty():
            raise IndexError("덱이 빈 상태 ")
        else:
            return self.array[self.rear] # 바로  rear 위치

#===============================
# 링버퍼 테스트 프로그램
# =============================

def test_code_2_5():
    # test : 코드 2.5
    dq = CircularDeque(9)  # 실제 저장 가능 개수 = 9 (내부 N=10)
    dq.display("초기 상태")
    print()

    # 짝수는 후단, 홀수는 전단 삽입 (총 9개)
    for i in range(9):
        if i % 2 == 0:
            dq.add_rear(i)
        else:
            dq.add_front(i)
    dq.display("홀수 전단, 짝수 후단 삽입")
    print(dq.get_front(), dq.get_rear())     
    print()

    # 앞쪽 2개 삭제
    for _ in range(2):
        dq.delete_front()
    dq.display("앞쪽 2개 삭제")
    print(dq.get_front(), dq.get_rear())  
    print()

    # 뒤쪽 3개 삭제
    for _ in range(3):
        dq.delete_rear()
    dq.display("뒤쪽 3개 삭제")
    print(dq.get_front(), dq.get_rear())  
    print()

    # 앞쪽에 5개(9~13) 삽입 → 현재 사이즈에 맞춰 overflow 없이 채움
    for i in range(9, 14):
        dq.add_front(i)
    
    dq.display("덱의 앞쪽에 9~13 5개 삽입")
    print(dq.get_front(), dq.get_rear())    


if __name__ == "__main__": 
    test_code_2_5()   
    