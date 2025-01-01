# Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
# Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 

numbers = input("enter your numbers:").split()

numbers = list(map(int, numbers))

squares = []
for i in numbers:
    squares.append(i ** 2)

print("number:", numbers)
print("squares before sorting", squares)
