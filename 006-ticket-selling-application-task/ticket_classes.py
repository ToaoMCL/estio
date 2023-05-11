class Price():
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

class Ticket():
    def __init__(self, price, customer, identifier):
        self.price = price
        self.customer = customer
        self.identifier = identifier

class Event():
    def __init__(self, name, venue, event_price, available_tickets):
        self.name = name
        self.venue = venue
        self.event_price = event_price
        self.available_tickets = available_tickets
        self.tickets = [] 

    def buyTickets(self, numbertobuy, customer):
        for i in range(numbertobuy):
            mod_price = self.event_price.value * len(self.tickets)
            new_ticket = Ticket(mod_price, customer, len(self.tickets))
            self.tickets.append(new_ticket)
            self.available_tickets =- 1
            print(mod_price)

    def deleteTicket(self, identifier):
        for ticket in self.tickets:
            if ticket.identifier == identifier:
                self.tickets.remove(ticket)
                break

class Venue():
    def __init__(self, location):
        self.location = location

class Customer():
    def __init__(self, name):
        self.name = name