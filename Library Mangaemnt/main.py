class Library:
    print("Welcome To Our Online Library")

    def __init__(self):
            self.books_avail = ["Harry Potter Series:", "", "Chamber Of Secrets", "Prisoner Of Azkaban", "Goblet of Fire", "Order Of the Phoenix", "Half Blood Prince", "Deathly Hallows: Part 1", "Deathly Hallows: Part 2"]
            self.sample_of_books = ["Harry Potter Series:", "Philosopher's Stone", "Chamber Of Secrets", "Prisoner Of Azkaban", "Goblet of Fire", "Order Of the Phoenix", "Half Blood Prince", "Deathly Hallows: Part 1", "Deathly Hallows: Part 2"]

    def show_books(self):
        print("\nBooks Present In This Library are: \n")
        print('*'*30)
        for books in self.books_avail:
            print(books)
        print('*'*30)
        print("\n")

    def borrow_a_book(self, book_n):
        if book_n not in self.books_avail:
            print("Sorry, Book is not available")

        ask = input("You want to borrow this book: ")
        if 'yes' in ask.lower():
            self.books_avail.remove(book_n)
            print("Here is your book keep it safe and don't forget to return it in 30 days")

        elif 'no' in ask.lower():
            print("Ok sir")

    def return_a_book(self):
        ask = input("You want to return a book: ")
        if 'yes' in ask.lower():
            r_book = input("What is the name of Book: ")
            if r_book.lower() in self.sample_of_books:
                self.books_avail.append(r_book)
                print("Thanks For Returning the Book")

            elif r_book not in self.sample_of_books:
                print("This book is not of our Library")

        elif 'no' in ask.lower():
            print("Ok sir")

RudrOsford = Library()
while True:
        ask = input("\nWhat You Want to do: ")

        if 'quit' in ask.lower():
            print("Thanks For Using Our Library")
            break

        if 'show' in ask.lower():
            RudrOsford.show_books()
        
        if 'borrow' in ask.lower():
            bn = input("Which book You like to borrow sir: ")
            RudrOsford.borrow_a_book(bn)

        if 'return' in ask.lower():
            RudrOsford.return_a_book()




# Harry_Potter = ["Harry Potter Series:", "Philosopher's Stone", "Chamber Of Secrets", "Prisoner Of Azkaban", "Goblet of Fire", "Order Of the Phoenix", "Half Blood Prince", "Deathly Hallows: Part 1", "Deathly Hallows: Part 2"]
# Riddles = ["Top 100 Riddles", "Funny Sentences", "Duck in a book", "What you you dont", "Somtimes it's riddle", "You will Like it", "I say You laugh", "It's Funny"]
# Fairy_Tales = ["Cindrella", "Snow White", "Sofia", "The Red Riding Hood", "The Three Little Pigs", "The Gringer Bread Man", "Beauty and Beast"]
# Marvel_Comics = ["Iron Man", "Captain America", "World War Hulk", "Avengers", "Civil War", "Infinity War", "EndGame"]
# Crime = ["CID Season 1", "Cid Season 2", "Sherlock Holmes", "Sherlock Holmes 2", "Sherlock Holmes 3"]

# books_avail ="Harry Potter Series:", "Philosopher's Stone", "Chamber Of Secrets", "Prisoner Of Azkaban", "Goblet of Fire", "Order Of the Phoenix", "Half Blood Prince", "Deathly Hallows: Part 1", "Deathly Hallows: Part 2"