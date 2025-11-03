#############################################################################
#  Factorial App (반복/재귀 n! 계산기) - 인터랙티브 콘솔 프로그램
#  작성자: 이승후
#  작성일: 2025-09-29
#
#  메뉴(Menu):
#    1) 반복(iterative)으로 n!
#    2) 재귀(recursive)로 n!
#    3) 두 방식 결과/시간 비교(compare time)
#    4) 준비된 테스트 데이터(batch run)
#    q) 종료(quit)
#
#  알고리즘:
#    - factorial_iter(n): 반복문. n<0이면 ValueError
#    - factorial_rec(n):  재귀.   n<0이면 ValueError
#    - run_with_time(func, n): 결과와 경과시간(seconds) 반환 (perf_counter)
#    - 입력 검증: 정수 문자열 여부 확인, 음수 차단 → 오류 메시지 후 메뉴 복귀
#    - 예외: 큰 n에서 RecursionError 가능 → 그대로 노출(지시사항)
#############################################################################

from time import perf_counter

# 테스트 데이터
TEST_CASES = [0, 1, 2, 3, 5, 10, 15, 20, 30, 50, 100]


def factorial_iter(n: int) -> int:
    """반복문 기반 n! (n<0이면 ValueError)"""
    if n < 0:
        raise ValueError("n은 0 이상 정수여야 합니다.")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result


def factorial_rec(n: int) -> int:
    """재귀 기반 n! (n<0이면 ValueError)"""
    if n < 0:
        raise ValueError("n은 0 이상 정수여야 합니다.")
    if n == 0 or n == 1:  # 올바른 기저 조건
        return 1
    return n * factorial_rec(n - 1)


def run_with_time(func, n: int):
    """함수를 n에 대해 실행하고 (result, elapsed_seconds) 반환"""
    t0 = perf_counter()
    result = func(n)
    t1 = perf_counter()
    return result, (t1 - t0)


def is_nonneg_int_string(s: str) -> bool:
    """'0 이상 정수' 형태인지 검사 (선행/후행 공백 허용)"""
    s = s.strip()
    # +기호는 허용, -는 비허용
    if s.startswith("+"):
        s = s[1:]
    return s.isdigit()  # 빈 문자열/음수/문자열은 False


def prompt_n() -> int | None:
    """n 입력 프롬프트. 잘못되면 메시지 출력 후 None 반환(메뉴로 복귀)."""
    raw = input("n 값(정수, 0 이상)을 입력하세요: ").strip()
    if not is_nonneg_int_string(raw):
        print("정수(0 이상)만 입력하세요.")
        return None
    n = int(raw)
    return n


def print_header():
    print("\n================ 팩토리얼 ================\n"
          "1) 반복법으로 n! 계산\n"
          "2) 재귀로 n! 계산\n"
          "3) 두 방식 모두 계산 후 결과/시간 비교\n"
          "4) 준비된 테스트 데이터 일괄 실행\n"
          "q) 종료\n"
          "--------------------------------------------------")


def do_iterative():
    n = prompt_n()
    if n is None:
        return
    try:
        val, dt = run_with_time(factorial_iter, n)
        print(f"[반복] {n}! = {val}")
        print(f"[반복] 시간: {dt:.6f} s")
    except ValueError as e:
        print(e)


def do_recursive():
    n = prompt_n()
    if n is None:
        return
    try:
        val, dt = run_with_time(factorial_rec, n)
        print(f"재귀 {n}! = {val}")
        print(f"시간: {dt:.6f} s")
    except RecursionError:
        print("최대 재귀 깊이를 초과.")
    except ValueError as e:
        print(e)


def do_compare():
    n = prompt_n()
    if n is None:
        return
    try:
        ival, idt = run_with_time(factorial_iter, n)
        rval, rdt = run_with_time(factorial_rec, n)  # 재귀 허용
        same = (ival == rval)
        print(f"반복 {n}! = {ival}")
        print(f"재귀 {n}! = {rval}")
        print(f"결과 일치 여부: {'일치' if same else '불일치'}")
        print(f"반복 시간: {idt:.6f} s  |  재귀 시간: {rdt:.6f} s")
    except RecursionError:
        print("에러")
    except ValueError as e:
        print(e)


def do_batch():
    print("테스트 데이터 실행")
    for n in TEST_CASES:
        try:
            ival, idt = run_with_time(factorial_iter, n)
            rval, rdt = run_with_time(factorial_rec, n)
            same = (ival == rval)
            print(f"{n:>3} | same={same} | iter={idt:.6f}s, rec={rdt:.6f}s")
            print(ival)
        except RecursionError:
            print(f"{n:>3} | 재귀 에러 발생")
        except ValueError as e:
            print(f"{n:>3} | 오류: {e}")


def main():
    while True:
        print_header()
        choice = input("선택: ").strip().lower()
        if choice == "1":
            do_iterative()
        elif choice == "2":
            do_recursive()
        elif choice == "3":
            do_compare()
        elif choice == "4":
            do_batch()
        elif choice in ("q", "quit"):
            print("종료합니다.")
            break
        else:
            print("메뉴에서 1/2/3/4 또는 q를 입력하세요.")


if __name__ == "__main__":
    main()
