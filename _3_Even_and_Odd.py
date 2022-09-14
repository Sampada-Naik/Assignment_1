number_count = int(input("Enter the number of elements: "))
lst = []

for i in range(0,number_count):
    numbers=int(input())

    lst.append(numbers)

print(lst)

even_numbers = 0
odd_numbers = 0

for j in lst:

    if j % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
print("Number of even numbers: ",even_numbers)
print("Number of odd numbers: ",odd_numbers)