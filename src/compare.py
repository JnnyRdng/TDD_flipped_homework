def compare(num_1, num_2):
    num_1 = int(num_1)
    num_2 = int(num_2)
    if num_1 > num_2:
        return f"{num_1} is greater than {num_2}"
    elif num_1 < num_2:
        return f"{num_1} is less than {num_2}"
    else:
        return "both numbers are equal"
