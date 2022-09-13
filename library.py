from xmlrpc.client import boolean
class User: 
    def __init__(self,name:str)->None:
        """
        El usuario solo recibe su nombre
        """
        self.name = name

    def borrow(self, book_name:str, books:list)->None:
        """
        como los libros estan en una lista si el usuario desea prestarlo
        solo hay que removerlo
        """
        for X in books:
            if book_name in X:
                books.remove(book_name)
            
        return books

    def returns(self, book_name:str, books:list)->None:
        """
        para devolver un libro solo hay que agregarlo a la lista
        el sw es para que si encontro el libro se cambie a 1 para
        que no pueda agregar un libro que ya se encuentra disponible
        """
        sw=0
        for X in books:
            if book_name in X:
                sw=1
                print("No se puede devolver ya el libro esta registrado")
                break
        if sw==0:
            books.append(book_name)
            return books

    def display(self,books: list)->None:
        """
        este metodo solo debe mostrar la lista
        """
        print(books)

class Librarian:
    def __init__(self, name:str)->None:
        self.name= name

    def upload(self, books: list, book_name:str)->None:
        """
        Misma logica para retornar del usuario
        """
        sw=0
        for X in books:
            if book_name in X:
                sw=1
        if sw==0:
            books.append(book_name)
        
    def remove(self, books:list, book_name:str, lost_damaged:int)->None:
        """
        si el libro esta dañado o perdido se debe remover
        esto se verifica si la biliotecaria digita 1 o cualquier 
        otro numero
        """
        if lost_damaged==1:
            for X in books:
                if book_name in X:
                    books.remove(book_name)
                    return books
                else: 
                    print("no lo he encontrado todavía")

class Library:
    def __init__(self, user:User, library:Librarian)->None:
        self.user = user
        self.library = library
