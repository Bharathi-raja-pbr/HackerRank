'''
Given a Book class and a Solution class, write a MyBook class that does the following:

Inherits from Book
Has a parameterized constructor taking these  parameters:
string 
string 
int 
Implements the Book class' abstract display() method so it prints these  lines:
title, a space, and then the current instance's .
author, a space, and then the current instance's .
price, a space, and then the current instance's .
Note: Because these classes are being written in the same file, you must not use an access modifier (e.g.: ) when declaring MyBook or your code will not execute.

Input Format

You are not responsible for reading any input from stdin.
The Solution class creates a Book object and calls the MyBook class constructor (passing it the necessary arguments).
It then calls the display method on the Book object.

Output Format

The  method should print and label the respective title , author and price of the MyBook object's instance (with each value on its own line) like so:

Title: $title
Author: $author
Price: $price
Note: The  is prepended to variable names to indicate they are placeholders for variables.

Sample Input

The following input from stdin is handled by the locked stub code in your editor:

The Alchemist
Paulo Coelho
248
Sample Output

The following output is printed by your display() method:

Title: The Alchemist
Author: Paulo Coelho
Price: 248
'''

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    
    def display(self):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")
        

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
