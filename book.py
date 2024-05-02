class book:
    def __init__(self,tile,author,pages):
        self.title=tile
        self.author=author
        self.pages=pages

    def info(self):
        print(f"tile: {self.title},  author: {self.author},  pages: {self.pages}")
    def read(self,page_read):
        self.page_read=page_read
        if page_read<=self.pages:
            print(f"you  read: {self.page_read} and pages you can read:{self.pages-self.page_read}")
        else:
            print("there are no pages to read")

title=input("enter the title: ")
author=input("enter the author: ")
pages=int(input("enter the pages: "))
page_read=int(input("enter  the pages read: "))


book1=book(title,author,pages)
book1.info()
book1.read(page_read)

