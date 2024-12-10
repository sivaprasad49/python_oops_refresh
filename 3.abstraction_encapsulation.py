class Library():
    def __init__(self, all_books):
        self.all_books = all_books
        print(f'All books in Library {self.all_books}')

    def get_library_books(self, return_books: str):
        print(f'Adding a new book {return_books}')
        self.all_books.append(return_books)
        return self.all_books


all_books = ['book1', 'book2']
lib1 = Library(all_books)

print(lib1.get_library_books('book3'))


