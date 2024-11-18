"""Library Management System"""
"""Steps:
    1. List of Books to choose
    2. Member and non member
    3. Time for book return = 1 week
    4. Fine for late return and lost ..so M.R.P of the book. exclude from the library books
    5. Lost membership
    6. Check if the book is available / a book is 4 in numbers
    7. 
"""

class LIBRARY_MANAGEMENT:
    def __init__(self,member_code, books = None):
        if books is None:
            books = []
        self.books = books
        self.member_code = member_code 
    def books(self):
        self.books = {"Harry Potter":[200,4], "Seto Dharti":[300,3], "Karnali Blues":[400,3]}
    def _Check_member(self):
        self.member_code = ["123","456","7,8,9"]
        temp = input("Please provide your membership number ")
        if temp in self.member_code:
            print(" You can now proceed as a member  ")
            def check_out()
        else:
            print(f"Sorry no membership number {temp} found ")
            exit()
    def check_out(self):
        u_book = input("Which book would you like to borrow? ")
        if u_book in self.books:
            print(f"Congratulations, please receive the book {u_book} from the department ")
            self.books

        
        