# book_class.py

class Book:
    """
    A class representing a book with title, author, and publication year.
    """

    def __init__(self, title: str, author: str, year: int):
        """
        Initializes a Book instance with title, author, and year.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Prints a message upon object deletion.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: A string in the format "(title) by (author), published in (year)".
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns an official representation of the book.

        Returns:
            str: A string that would recreate the Book instance.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"


# Example usage:
if __name__ == "__main__":
    book = Book("To Kill a Mockingbird", "Harper Lee", 1960)
    print(book)  # Output: To Kill a Mockingbird by Harper Lee, published in 1960
    print(repr(book))  # Output: Book('To Kill a Mockingbird', 'Harper Lee', 1960)
    del book  # Output: Deleting To Kill a Mockingbird