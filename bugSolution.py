def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage with an empty list
average = calculate_average([])
print(f"The average is: {average}")

#Example usage with a list of numbers
numberList = [10,20,30,40,50]
average = calculate_average(numberList)
print(f"The average is: {average}")