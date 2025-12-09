def count_climbing_ways(n: int) -> int:
    """한 번에 1칸 또는 2칸씩 올라가면서 n개의 계단을 오르는 방법의 수를 반환합니다."""
    if n < 0:
        return 0
    if n == 0:
        return 1

    table = [0] * (n + 1)
    table[0] = 1
    table[1] = 1

    for step in range(2, n + 1):
        table[step] = table[step - 1] + table[step - 2]

    return table[n]


def main() -> None:
    raw_input = input("계단의 개수를 입력하시오: ")

    try:
        stair_count = int(raw_input.strip())
    except ValueError:
        print("정수 값을 입력해 주세요.")
        return

    if stair_count < 0:
        print("0 이상의 개수를 입력해 주세요.")
        return

    ways = count_climbing_ways(stair_count)
    print(f"{stair_count}개의 계단을 오르는 방법의 수는 {ways}가지입니다.")


if __name__ == "__main__":
    main()
