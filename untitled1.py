class Book:
    def __init__(self, name, date, author):
        self.date = date
        self.name = name
        self.author = author
        
    def confirm_entry(self):
        print(self.date)
        print(self.name)
        print(self.author)
            
    def calculate_age(self):
        age_in_years = 2024 - self.date
        print("Age of the book:", age_in_years, "years")
        
Book1 = Book("The Tester Book", 2001, "Anonymous")
Book1.confirm_entry()
Book1.calculate_age()
