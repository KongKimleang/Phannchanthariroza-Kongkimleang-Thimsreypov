def reverse_ascending(numbers):
    ...
    result=[]
    start=0
    for i in range(1, len(numbers)):
        if numbers[i]<=numbers[i-1]:
            result.extend(reversed(numbers[start:i]))
            start=i
    result.extend(reversed(numbers[start:]))
    return result
list_number=[]
while True:
    num=input("Enter number ('s' to stop): ")
    if num=="s":
        break
    list_number.append(int(num))
print(reverse_ascending(list_number))

