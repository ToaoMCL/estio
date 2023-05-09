def run_calculation(x, y, b, l):
    b = b + 1
    z = x + y
    print(f'{x}, {y} : {z}')
    if b == l:
        print(f'completed sequence of lenght: {l}')
    else:
        run_calculation(y, z, b, l)

l = int(input("How long do you want the sequence to be? \n"))

run_calculation(0, 1, 0, l)