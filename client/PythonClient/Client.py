from zeep import Client

url = "http://localhost:2317/BookSoap?wsdl"
client = Client(url)

# Crear un libro
new_book = {"Title": "Libro de Prueba", "Author": "Autor Prueba", "Year": 2024}
response = client.service.CreateBook(newBook=new_book)
print("Libro creado:", response)

# Obtener todos los libros
books = client.service.GetBooks()
print("Lista de libros:", books)
