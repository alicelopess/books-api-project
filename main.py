# Passo a Passo:
# 1 - Instalações e Importações
from db import BOOKS
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Union, Optional

# 2 - Iniciação do FastAPI - Instanciar
app = FastAPI()


# 3 - Criação do Banco de Dados em Memória
## Definindo classe livros e seus atributos
class Book(BaseModel):
  id: int
  title: str
  author: str
  category: str
  description: Optional[str] = None

# 4 - Criação dos Endpoints - Rotas da API
##Root
@app.get("/") #Homepage
def read_root():
    return {"message": "Hello, World! Welcome to my first FastAPI!"}

##GET
@app.get('/books')
def books():
  return BOOKS

##GET ID
@app.get('/books/{book_id}')
def book_id(book_id: int):
  for book in BOOKS:
    if book['id'] == book_id:
      return book

##POST => Criação com Validação
@app.post('/books')
def create_book(book: Book):
  BOOKS.append(book)
  return {
    'message': 'Congratulations! Your book was created!',
    'data': book
  }

##PUT
@app.put('/books/{book_id}')
def update_book(book_id: int, book: Book):
  counter = 0
  for i in BOOKS:
    counter += 1
    if i['id'] == book_id:
      BOOKS[counter - 1] = book
      return {
        'message': 'Congratulations! Your book was updated!',
        'data': book
      }

##DELETE
@app.delete('books/{book_id}')
def delete_book(book_id: int):
   for book in BOOKS:
    if book['id'] == book_id:
      BOOKS.remove(book)
      return {'message': 'Book was deteled!'}

