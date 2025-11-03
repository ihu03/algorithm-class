# 팩토리얼


# 1) 반복법으로 n! 계산
def factorial_iter(n):
    if n<0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    result =1
    for k in range(2,n+1):
        result = result*k
    return result


# 2) 재귀로 n! 계산
def factorial_rec(n):
    # n이 0보다 작으면 오류 발생 
    if n < 0:
        raise ValueError("정수(0 이상의 숫자)만 입력하세요.")
    
    # 0!과 1! = 1로 정의
    if n <= 1:
        return 1
    
    return n * factorial_rec(n - 1)

# 3) 두 방식 모두 계산 후 결과/시간 비교
def run_with_time(n):
     import time
     start_time = time.time()
     result_iter = factorial_iter(n)
     end_time = time.time()
     iter_time = end_time - start_time

     start_time = time.time()
     result_rec = factorial_rec(n)
     end_time =time.time()
     rec_time = end_time - start_time

     if result_iter == result_rec:
          result_coincidence = "일치"
     else: result_coincidence = "불일치"


     print(f"[반복] {n}! = {result_iter}")
     print(f"[재귀] {n}! = {result_rec}")
     print(f"결과 일치 여부: {result_coincidence}")
     print(f"[반복] 시간:{iter_time:.6f} s |   [재귀] 시간:{rec_time:.6f} s\n")
     return iter_time, rec_time

# 4) 준비된 테스트 데이터 일괄 실행
def ready_test_data():
    import time
    data = [0,1,2,3,5,10,15,20,30,100]
    for n in data:
        
        start_time = time.time()
        result_iter = factorial_iter(n)
        end_time = time.time()
        iter_time = end_time - start_time

        start_time = time.time()
        result_rec = factorial_rec(n)
        end_time =time.time()
        rec_time = end_time - start_time    

        if result_iter == result_rec:
               same_result = 'True'
        else:
                same_result = 'False'
        print(f"n={n} | same = {same_result} | iter= {iter_time:.6f}s, rec={rec_time:.6f}s\n {n}! = {result_iter}\n")
           
          


def main():
    print("팩토리얼 계산기 (반복/재귀) - 정수 n>=0를 입력하세요.\n")
    print('================ Factorial Tester ================\n')
    print('1 반복법으로 n! 계산\n')
    print('2 재귀로 n! 계산\n')
    print('3 두 방식 모두 계산 후 결과/시간 비교\n')
    print('4 준비된 테스트 데이터 일괄 실행\n')
    print('q) 종료\n')
    print('--------------------------------------------------\n')
    chose = input('선택 : ').strip()
    
    if chose in('1','2','3'):
            try:
                n = int(input('n 값(정수,0 이상)을 입력하세요: ').strip())
                if n <0:
                    print('정수(0 이상의 숫자)만 입력하세요.')
                else:
                    if chose =='1':
                        print(f'반복법: {n}! = {factorial_iter(n)}')
                    elif chose =='2':
                        print(f'재귀법: {n}! = {factorial_rec(n)}')
                    elif chose =='3':
                        run_with_time(n)
                    
                    
                         
            except ValueError:
                print('정수(0 이상의 숫자)만 입력하세요.')  
    elif chose == '4':
            ready_test_data()
    elif chose =='q':
            print("프로그램을 종료합니다")




if __name__ == "__main__":
    main()


                
 



    


