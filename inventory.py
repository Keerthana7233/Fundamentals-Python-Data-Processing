import csv


class Book:
    def __init__(self, title: str, author: str, price: float, stock: int):
        self.title = title
        self.author = author
        self.price = float(price)
        self.stock = int(stock)

    def __repr__(self) -> str:
        return (
            f"Book(title='{self.title}', "
            f"author='{self.author}', "
            f"price={self.price:.2f}, "
            f"stock={self.stock})"
        )


def load_inventory(filepath: str) -> list[Book]:
    """Read books from a CSV file and return a list of Book objects."""
    books = []

    with open(filepath, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            if not row:
                continue

            title, author, price, stock = row

            book = Book(
                title,
                author,
                float(price),
                int(stock)
            )

            books.append(book)

    return books


def total_inventory_value(books: list[Book]) -> float:
    """Calculate the total value of all books in stock."""
    return sum(book.price * book.stock for book in books)


def most_expensive_book(books: list[Book]) -> Book | None:
    """Return the book with the highest price."""
    if not books:
        return None

    return max(books, key=lambda book: book.price)


def author_stock_report(books: list[Book]) -> dict[str, int]:
    """Calculate total stock for each author."""
    report = {}

    for book in books:
        if book.author in report:
            report[book.author] += book.stock
        else:
            report[book.author] = book.stock

    return report


def main():
    # Load inventory from the sample CSV file
    filepath = "sample_inventory.csv"

    books = load_inventory(filepath)

    print("=== Book Inventory ===")

    for book in books:
        print(book)

    # Total inventory value
    total_value = total_inventory_value(books)

    print("\n=== Total Inventory Value ===")
    print(f"₹{total_value:.2f}")

    # Most expensive book
    expensive = most_expensive_book(books)

    print("\n=== Most Expensive Book ===")

    if expensive is not None:
        print(expensive.title)
    else:
        print("No books available.")

    # Author stock report
    report = author_stock_report(books)

    print("\n=== Author Stock Report ===")

    for author, stock in report.items():
        print(f"{author}: {stock} books")


if __name__ == "__main__":
    main()