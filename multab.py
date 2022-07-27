def square(n):
    name = input('What is your name, dear guest?')
    print(f'Welcome, {name}, to multiplication table! Here is the result of the figure {n}, multiplied by from 0 to 10.')
    squared_numbers = []
    number = 0 
    while len(squared_numbers) < 11:
        x = n * number 
        squared_numbers.append(x)
        number = number + 1 

    for i, v in enumerate(squared_numbers):
        print(f'{n} by', i, '=', v)
          
if '__name__' == '__main__':
    square(1)

print(square(8))