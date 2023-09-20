from fastapi import FastAPI

app = FastAPI()

products = [
  {
  "id": 1,
  "name": "Product 1",
  "price": 20,
  "stock": 10 
  },
  {
  "id": 2,
  "name": "Product 2",
  "price": 20,
  "stock": 10 
  }
]
  
@app.get("/")
def message():
  return "Hello World" # Usar uvicorn main:app
  return "añadir /docs a la ruta muestra documentacion"

@app.get("/products")
def get_products():
  return products # retornar listado

@app.get("/products/{id}") #empexamos con parametros
def get_products(id: int):
  return list(filter(lambda item: item["id"] == id,products)) #llama un filtro que busque coincidencia