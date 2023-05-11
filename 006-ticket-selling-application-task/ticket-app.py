from ticket_classes import *

actions = ["Buy tickets", "Return tickets", "Create event", "Cancel event", "Exit"]

default_price = Price(10, "GPB")
default_venue = Venue("London")
default_customer = Customer("Nathan")

event = Event("default", default_venue, default_price, 30)

while True:
    operation = int(input(f"What do you want to do? \n 1: {actions[0]} \n 2: {actions[1]} \n 3: {actions[2]} \n 4: {actions[3]} \n 5: {actions[4]} \n"))
    if operation == 1:
        tickets_to_buy = int(input("How many tickets do you want to buy: "))
        event.buyTickets(tickets_to_buy, default_customer)
        print(event.name)
        print(event.tickets)
    elif operation == 2:
        ticket_to_remove = int(input("What ticket do you want to remove: "))
        event.deleteTicket(ticket_to_remove)
        print(event.tickets)
    elif operation == 3:
        event = Event("cool event", default_venue, default_price, 30)
    elif operation == 4:
        print("a")
    elif operation == 5:
        exit()