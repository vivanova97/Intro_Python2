import unittest
from library import *
from unittest.mock import patch
import io

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("how to make friends and influence people", "Dale Carnegie")

    def test_book_initialization(self):
        # Testing invalid initialization with author being incorrect type
        with self.assertRaises(TypeError) as e:
            Book('How to Make Friends and Influence People', 7)
        self.assertEqual(str(e.exception), "Author should be in string format.")

        # Testing invalid initialization with title being incorrect type
        with self.assertRaises(TypeError) as e:
            Book(7, "Dale Carnegie")
        self.assertEqual(str(e.exception), "Title should be in string format.")

        #Testing valid initialization and capitalization of title and author
        self.assertEqual(Book("how to make friends and influence people", "Dale Carnegie").title,
                         "How To Make Friends And Influence People")
        self.assertEqual(Book("How to Make Friends and Influence People", "dale carnegie").author,
                         "Dale Carnegie")

    def test_setting_attributes_after_init(self):
        with self.assertRaises(AttributeError) as e:
            self.book.title = "War and Peace"
            self.book.author = "Leo Tolstoy"
        self.assertEqual(str(e.exception), "Cannot change attribute once it's been initialized.")


class TestLibrary(unittest.TestCase):
    def setUp(self):
        # creates books and library for testing
        self.book1 = Book("How To Make Friends And Influence People", "Dale Carnegie")
        self.book2 = Book("War and Peace", "Leo Tolstoy")
        self.library = Library()

    @patch('sys.stdout', new_callable=io.StringIO)
    # uses setUp to test adding books
    def test_add_book(self, mock_stdout):
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.list_books()
        self.assertEqual(mock_stdout.getvalue(), "How To Make Friends And Influence People by Dale Carnegie"
                                                 "\nWar And Peace by Leo Tolstoy\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_remove_book(self, mock_stdout):
        # uses setUp to test removing non-existing book
        with self.assertRaises(BookNotFoundError) as e:
            self.library.remove_book("Crime and Punishment", "Fyodor Dostoevsky")
        self.assertEqual(str(e.exception), "Crime and Punishment by Fyodor Dostoevsky not found.")

        # uses setUp to test removing existing book
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)
        self.library.remove_book("War And Peace", "Leo Tolstoy")
        self.library.list_books()
        self.assertEqual(mock_stdout.getvalue(), "How To Make Friends And Influence People by Dale Carnegie\n")

