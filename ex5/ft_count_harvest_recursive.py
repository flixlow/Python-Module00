def ft_count_harvest_recursive(days_input, days_count):
    if days_input is None:
        days_input = input("Days until harvest: ")
        days_input = int(days_input)
        days_count = 0
    if days_input == days_count and days_count != 0:
        print("Harvest time!")
        return
    if days_count < days_input:
        days_count += 1
        print("Day", days_count)
        ft_count_harvest_recursive(days_input, days_count)


ft_count_harvest_recursive(None, None)
