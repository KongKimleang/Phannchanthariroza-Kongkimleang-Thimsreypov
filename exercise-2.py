
def index_power(numbers, n):
    if n < 0 or n >= len(numbers):
        return -1
    
    result = numbers[n] ** n
    
    return result


# User input
print("Enter the elements of the array, separated by spaces:")
array_input = input()
array = list(map(int, array_input.split()))

print("Enter the number N:")
N = int(input())

result = index_power(array, N)
if result == -1:
    print("N is outside of the array bounds.")
else:
    print(f"The result is: {result}")
