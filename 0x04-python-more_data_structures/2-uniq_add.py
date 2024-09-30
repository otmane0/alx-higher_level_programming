def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Create a set to store unique integers
    total_sum = 0  # Initialize the sum variable

    for number in unique_numbers:
        total_sum += number  # Add each unique number to the total sum

    return total_sum
