class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages = pages

    def print_information(self):
        print(f"Kirjan {self.name} ({self.pages} sivua) kirjoittaja on {self.author}.")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"Lehden {self.name} päätoimittaja on {self.editor}.")

book1 = Book("Hytti no. 6", "Rosa Liksom", 200)
mag1 = Magazine("Aku Ankka", "Aki Hyyppä")

book1.print_information()
mag1.print_information()