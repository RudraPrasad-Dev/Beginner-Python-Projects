import text_coloring as tc

class movie_theater_seats:
    def __init__(self, rows, seats_per_row):
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats = [['O' for _ in range(seats_per_row)] for _ in range(rows)]

    def display_seats(self):
        print(tc.color_text("\nThis is the Current Seat Status:", tc.blue))
        for row in self.seats:
            print(tc.color_text(" ".join(row), tc.end))
        print()
    
    def seats_booking(self):
        self.booking_row = int(input(tc.color_text("\nWhich row's seat do you want: ", tc.blue)))
        self.booking_seat = int(input(tc.color_text(f"Which seat do you want: ", tc.blue)))
        if 1 <= self.booking_row <= self.rows and 1 <= self.booking_seat <= self.seats_per_row:
            if self.seats[self.booking_row - 1][self.booking_seat - 1] == 'O':
                self.seats[self.booking_row - 1][self.booking_seat - 1] = tc.color_text("X", tc.red)
                print(tc.color_text("Your ticket is successfully booked!", tc.blue))
                self.display_seats()
            else:
                print("The seat you tried to book is already booked by you!")
        else:
            print(tc.color_text("Your entry was Invalid!\n", tc.red))

if __name__ == '__main__':
    animal = movie_theater_seats(3, 5)
    print(tc.color_text("\nWelcome to the Theater Seats Management", tc.blue))
    animal.display_seats()
    while True:
        print(tc.color_text("1. Display The Seats \n2. Book a Ticket \n3. Exit", tc.yellow))
        user_req = input(tc.color_text("Enter your choice (1-3): ", tc.orange))
        if user_req == "1":
            animal.display_seats()
        elif user_req == "2":
            animal.seats_booking()
        elif user_req == "3":
            print(tc.color_text("Thank You for using this program!", tc.pink))
            break