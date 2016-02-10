from abc import ABCMeta, abstractmethod
class Book:
    __metaclass__ = ABCMeta
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print "Title: "+self.title
        print "Author: "+self.author
        print "Price: "+str(self.price)


title=raw_input()
author=raw_input()
price=int(raw_input())
new_novel=MyBook(title,author,price)
new_novel.display()


######### ----------------------------  #################
##/*Following is an example of abstract class in java:
##abstract class Book{
##    String title;
##    String author;
##    Book(String t,String a){
##        title=t;
##        author=a;
##    }
##    abstract void display();
##  }
##
##
##An abstract class is a class that cannot be instantiated, meaning you cannot create a new instance of it. Attempting to instantiate an abstract class (such as abstract class Book, provided for you in the editor) like so:
##Book new_novel=new Book("The Alchemist","Paulo Coelho"); 
##
##
##results in error: Book is abstract; cannot be instantiated. This type of class is only meant to serve as a base or blueprint for connecting the subclasses that inherit it.
##
##To use an abstract class, you must create its subclass and then instantiate the subclass. Any abstract methods declared in the abstract class (such as abstract void display() in abstract class Book) must be implemented by the subclass.
##*/
