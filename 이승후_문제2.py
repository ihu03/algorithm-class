ITEMS = [
    ("노트북", 3, 12),
    ("카메라", 1, 10),
    ("책", 2, 6),
    ("옷", 2, 7),
    ("휴대용 충전기", 1, 4),
]


def build_knapsack_table(capacity: int) -> list[list[int]]:
    """0/1 배낭 문제 물건으로 주어진 용량에 대한 Bottom-up DP 테이블을 생성합니다."""
    table = [[0] * (capacity + 1) for _ in range(len(ITEMS) + 1)]

    for i, (_, weight, value) in enumerate(ITEMS, start=1):
        for cap in range(capacity + 1):
            if weight <= cap:
                without_item = table[i - 1][cap]
                with_item = value + table[i - 1][cap - weight]
                table[i][cap] = max(without_item, with_item)
            else:
                table[i][cap] = table[i - 1][cap]

    return table


def traceback_selected_items(table: list[list[int]], capacity: int) -> list[str]:
    """역추적하여 선택된 물건 이름들을 반환합니다."""
    selected = []
    remaining_capacity = capacity

    for i in range(len(ITEMS), 0, -1):
        if table[i][remaining_capacity] != table[i - 1][remaining_capacity]:
            name, weight, _ = ITEMS[i - 1]
            selected.append(name)
            remaining_capacity -= weight
            if remaining_capacity <= 0:
                break

    selected.reverse()
    return selected


def main() -> None:
    raw = input("배낭 용량을 입력 하세요 : ")

    try:
        capacity = int(raw.strip())
    except ValueError:
        print("정수 값을 입력해 주세요.")
        return

    if capacity < 0:
        print("0 이상의 용량을 입력해 주세요.")
        return

    table = build_knapsack_table(capacity)
    max_value = table[len(ITEMS)][capacity]
    selected_items = traceback_selected_items(table, capacity)

    print(f"최대 만족도: {max_value}")
    print(f"선택된 물건: {selected_items}")


if __name__ == "__main__":
    main()
