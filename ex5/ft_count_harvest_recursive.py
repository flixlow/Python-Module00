def ft_count_harvest_recursive(days_input: int = None, days_count: int = None):
    if days_input is None:
        days_input = int(input("Days until harvest: "))
        days_count = 0
    if days_input == days_count:
        print("Harvest time!")
        return
    if days_count < days_input:
        days_count += 1
        print(f"Day {days_count}")
        ft_count_harvest_recursive(days_input, days_count)


# ft_count_harvest_recursive(None, None)
