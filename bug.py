def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (this will cause a ZeroDivisionError):
my_list = []
average = calculate_average(my_list)