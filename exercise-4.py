def chunking_by(numbers, chunck):
    return [numbers[i:i+chunck] for i in range(0, len(numbers), chunck)]
    ...
number=[]
while True:
    num=input("Enter number: ")
    if num=="q":
        break
    number.append(int(num))
size=int(input("Enter chunck size: "))
print(chunking_by(number,size))


