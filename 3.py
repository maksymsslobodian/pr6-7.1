class Book:
    def __init__(self, name, autor, count=1):
        self.name = name
        self.autor = autor
        self.count = count

    def __str__(self):
        return f"'{self.name}' - {self.autor} (Кількість: {self.count})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, name, autor):
        for book in self.books:
            if book.name == name and book.autor == autor:
                book.count += 1
                return


        new_book = Book(name, autor)
        self.books.append(new_book)

    def user_take_book(self, name, autor):
        for book in self.books:
            if book.name == name and book.autor == autor:
                if book.count > 0:
                    book.count -= 1
                    print(f"Ви взяли книгу: {name}")
                else:
                    print(f"Вибачте, книги '{name}' зараз немає в наявності.")
                return
        print("Такої книги в бібліотеці не існує.")

    def show_books(self):
        print("\nПоточний асортимент бібліотеки:")
        for book in self.books:
            print(book)


# Тестування
my_library = Library()

my_library.add_book("1984", "Джордж Орвелл")
my_library.add_book("Кобзар", "Тарас Шевченко")

my_library.show_books()

my_library.user_take_book("1984", "Джордж Орвелл")
my_library.show_books()