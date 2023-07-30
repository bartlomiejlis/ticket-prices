total = 0
passengers = int(input('Enter number of passengers: '))
i = 0

while i < passengers:
    age = int(input('Enter the age of the passenger: '))
    i += 1
    if(age < 3):
        continue
    total += 100

print(f'Tickets price: ${total}')