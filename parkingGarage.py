


class ParkingGarage:

    def __init__(self):
        self.parking_spaces = 500
        self.current_tickets = 400
        self.ticket_reader = 0    #setting a default value for an attribute (pg 163)
        self.paid = 0
        self.price = 20

# -----------------------TAKE TICKET(BEGINNING)--------------------------------

    # def getAvailableTickets(self):
    #     # returns how many tickets are available
    #     available = f'[**THE DRIVER ARRIVES AT THE GATE**]\nThere are {self.current_tickets} available.'
    #     return available

    def takeTicket(self):
        print(f'[** THE DRIVER TAKES A TICKET**]\nHere is your ticket!')
        self.current_tickets -= 1
        print(f'There are {self.current_tickets} remaining tickets.')
        self.parking_spaces -= 1
        print(f'There are {self.parking_spaces} parking spaces.\n\n-------------------------------------------------------------')


# -----------------------TAKE TICKET(END)--------------------------------

# -----------------------PAY FOR PARKING(BEGINNING)--------------------------------
    
    def payment(self):
        self.paid = int(input("Please enter the payment amount of $20. "))
        print(f'You paid ${self.paid}, you have 15 minutes to exit the lot.\n\n------------------------------------------------------')
        

# -----------------------PAY FOR PARKING(END)--------------------------------
# -----------------------LEAVE GARAGE(BEGINNING)-----------------------------------

    def leaving(self):
        if self.paid >= 20:
            print("Thank You, have a nice day.")
        else:
            self.paid = int(input("You haven't paid yet, please enter payment amount "))
            print(f'You paid {self.paid}. Thank you, have a nice day!')
            self.current_tickets += 1
            print(f'There are now {self.current_tickets} available tickets')                 

# -----------------------LEAVE GARAGE(END)-----------------------------------

# ---------------------------CALLING IN (BEGINNING)-------------------------------
    def goParking(self):
        while True:
            choice = input("Type 'enter' to receive ticket and enter the garage \nType 'pay' to pay the parking fee \nType 'exit' to leave the garage \nType 'quit' to end program.\n\nSELECT FROM THE ABOVE OPTIONS: " )
            if choice == "enter":
                self.takeTicket()
            
            elif choice == "pay":
                self.payment()

            elif choice == "exit":
                self.leaving()
                break

            elif choice == "quit":
                break

# ---------------------------CALLING IN (END)-------------------------------

michelle_parking = ParkingGarage()
birdie_parking = ParkingGarage()
tuna_parking = ParkingGarage()

michelle_parking.goParking()