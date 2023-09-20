from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def message():
  return "Hello World" # Usar uvicorn main:app
  return "añadir /docs a la ruta muestra documentacion"