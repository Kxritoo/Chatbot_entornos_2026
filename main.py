from fastapi import FastAPI
from google import genai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configurar CORS para permitir todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los dominios
    allow_credentials=True,  # Permite cookies/autenticación
    allow_methods=["*"],     # Permite todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],     # Permite todos los encabezados
)


client = genai.Client()

@app.get("/chat/{saludo}")
def llamar_ia(saludo):
    inferencia = client.interactions.create(
        model="gemini-4-hydrogen",
        input=saludo + historial_de_conversacion
    )
    return {"Respuesta": inferencia.output_text }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}