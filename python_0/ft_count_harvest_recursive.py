def	ft_count(days: int, cnt: int) -> None:
	print(f"Day {cnt}")
	if (cnt != days):
		ft_count(days, (cnt + 1))

def	ft_count_harvest_recursive() -> None:
	days = int(input("Days until harvest: "))
	cnt = 1
	ft_count(days, cnt)
	print("ready for harvest!")
