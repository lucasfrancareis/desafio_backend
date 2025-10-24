from fastapi import FastAPI
from app.controllers import product_controller
from app.db.database import Base, engine
from fastapi.responses import HTMLResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Produtos - ASCII Challenge",
    version="2.0",
    description="API RESTful criada em Python (FastAPI) com PostgreSQL, SQLAlchemy e Alembic."
)


@app.get("/", response_class=HTMLResponse)
async def read_root():

    html_content = """
    <html>
        <head>
            <title>API Rest Desafio ASCII</title>
            <style>
                body { 
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; 
                    margin: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #f4f4f9;
                }
                .container {
                    text-align: center;
                    background-color: #ffffff;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
                }
                h1 {
                    color: #333;
                }
                p {
                    color: #555;
                    font-size: 1.1em;
                }
                a {
                    display: inline-block;
                    margin-top: 20px;
                    padding: 10px 20px;
                    background-color: #007BFF;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-weight: bold;
                    transition: background-color 0.3s;
                }
                a:hover {
                    background-color: #0056b3;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>API do Desafio ASCII está no ar!</h1>
                <p>O servidor está funcionando perfeitamente.</p>
                <p>Clique no botão abaixo para ir à documentação interativa (Swagger).</p>
                <a href="/docs">Ir para /docs</a>
            </div>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(product_controller.router,
                   prefix="/api/produtos", tags=["Produtos"])


@app.get("/health")
def health():
    return {"status": "ok"}
