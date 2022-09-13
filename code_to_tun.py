from library import User, Librarian, Library
X= ["harry", "jose", "tom"]
libros= Library(User, Library)
X= ["1", "2", "3", "4"]

user1 = User("jose")
user1.borrow("1", X)
print(X)
user1.display(X)
user1.returns("1",X)
print(X)

bibliotecaria1 = Librarian("mariana")
bibliotecaria1.upload(X, "5")
print(X)
bibliotecaria1.remove(X, "1",1)
print(X)



