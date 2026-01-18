def ft_count_harvest_iterative(day: int = 1) -> None:
    until_harvest: int = int(input("Days until harvest: "))
    while day <= until_harvest:
        print(f"Day {day}")
        day += 1
    print("Harvest time!")


# ft_count_harvest_iterative()
