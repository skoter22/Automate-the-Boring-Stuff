# Collatz from Automate the Boring Stuff Chapter 3

def collatz(number):        
        if number % 2 == 0:
            print (number //2)
            return number / 2
        elif number % 2 == 1:
            return number * 3 + 1       
            print (number)

number = input('input a number:  ')
while number != 1:
    number = collatz(int(number))
    
    
