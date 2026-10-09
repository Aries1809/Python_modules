def ft_count_harvest_iterative() -> None:
	days = int(input("Days until harvest: "))
	cnt = 0
	while (cnt != days):
		cnt += 1
		print(f"Day {cnt}")
	print("Harvest time!")
