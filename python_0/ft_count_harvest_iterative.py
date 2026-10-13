def ft_count_harvest_iterative() -> None:
    days: int = int(input("Days until harvest: "))
    cnt: int = 0
    while (cnt != days):
        cnt += 1
        print(f"Day {cnt}")
    print("Harvest time!")
