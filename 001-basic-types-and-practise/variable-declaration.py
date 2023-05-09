def print_results(i,f,s):
    print(f'{i} is an integer')
    print(f'{f} is a float')
    print(f'{s} is a string')

i = 1   # int declaration
f = 1.1 # float declaration
s = "1" # string declaration
print_results(i,f,s)

# manual attempt to view differences when running program
i = int(input("Please provide a whole number: "))
f = float(input("Please provide a decimal number: "))
s = input("Please provide any text: ")
print_results(i,f,s)