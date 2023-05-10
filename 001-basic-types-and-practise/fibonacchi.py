def run_calculation(x, y, i, l):
    i = i + 1
    z = x + y
    print(f'{x}, {y} : {z}')
    if i == l:
        print(f'completed sequence of lenght: {l}')
    else:
        run_calculation(y, z, i, l)

l = int(input("How long do you want the sequence to be? \n"))

run_calculation(0, 1, 0, l)