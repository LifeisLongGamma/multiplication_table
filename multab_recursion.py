def square(n):
    if n == 11:
        print('Multiplication table is ready.')
        return
    
    squared_numbers = []
    number = 0 

    while len(squared_numbers) < 11:
        x = n * number 
        squared_numbers.append(x)
        number = number + 1 

    for i, v in enumerate(squared_numbers):
        print(f'{n} by', i, '=', v)

    print('\n')
    n = n + 1  

    square(n)
      
if '__name__' == '__main__':
    square(1)

print(square(1))