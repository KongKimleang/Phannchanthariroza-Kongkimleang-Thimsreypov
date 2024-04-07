
def remove_all_after(numbers, n):
    if n in numbers:
        index = numbers.index(n)
        return numbers[:index+1]
    else:
        return numbers

# User  input
print("Enter the elements of the list, separated by spaces:")
numbers_input = input()
numbers = list(map(int, numbers_input.split()))

print("Enter the border element:")
n = int(input())

result = remove_all_after(numbers, n)
print(result)
