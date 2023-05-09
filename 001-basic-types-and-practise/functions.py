def hello_world():
    return "Hello world!"

def hello_world_2(s):
    return f'{hello_world()} How are you {s}?'

s = input("What is your name? \n")

print(hello_world())
print(hello_world_2(s))