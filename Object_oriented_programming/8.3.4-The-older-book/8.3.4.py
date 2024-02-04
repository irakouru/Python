"""Please write a function named older_book(book1: Book, book2: Book) which takes two objects of 
type Book as its arguments. The function should print out a message with the details of whichever 
is the older. It should print out a different message if the two books were written in the same year."""

class Book():

    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

def older_book(book1: Book, book2: Book):
    if book1.year > book2.year:
        print(f"{book2.name} is older, it was published in {book2.year}.")
    elif book1.year < book2.year:
        print(f"{book1.name} is older, it was published in {book1.year}.")
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}.")


python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

older_book(python, everest)
older_book(python, norma)
