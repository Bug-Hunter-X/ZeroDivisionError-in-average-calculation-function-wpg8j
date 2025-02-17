def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage (this will now return 0 for empty list):
my_list = []
average = calculate_average(my_list)
print(f"Average: {average}")

my_list = [10, 20, 30]
average = calculate_average(my_list)
print(f"Average: {average}") 