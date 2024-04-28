import os
import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from schema.book import Book as SchemaBook
from model.book import Book as ModelBook

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url='postgresql://root:root@localhost/pman')


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.post('/book/', response_model=SchemaBook)
async def book(book: SchemaBook):
    db_book = ModelBook(title=book.title, rating=book.rating)
    db.session.add(db_book)
    db.session.commit()
    return db_book


@app.get('/book/')
async def book():
    book = db.session.query(ModelBook).all()
    return book

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)
