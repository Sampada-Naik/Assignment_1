#Fibonaaci series between 0 to 50
first_number = 0
second_number = 1

while(second_number < 50):
    print(second_number, end=" ")
    temp = first_number+second_number
    first_number = second_number
    second_number = temp