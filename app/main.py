from fastapi import FastAPI
from app.controllers import product_controller
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="API de Produtos - ASCII Challenge",
    version="2.0",
    description="API RESTful criada em Python (FastAPI) com PostgreSQL, SQLAlchemy e Alembic."
)


@app.get("/", response_class=HTMLResponse)
async def read_root():

    html_content = """
     <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>API de Produtos - ASCII Challenge</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }
            body {
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #1e1e2f, #2b5876);
                font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
                color: #fff;
            }
            .card {
                background: rgba(255, 255, 255, 0.08);
                border: 1px solid rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 40px 60px;
                border-radius: 16px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.3);
                animation: fadeIn 1s ease-in-out;
            }
            h1 {
                font-size: 2.2rem;
                font-weight: 600;
                margin-bottom: 15px;
            }
            p {
                color: #e0e0e0;
                font-size: 1rem;
                margin-bottom: 25px;
                line-height: 1.5;
            }
            a {
                display: inline-block;
                padding: 12px 24px;
                background: #00b4d8;
                color: #fff;
                text-decoration: none;
                border-radius: 8px;
                font-weight: 600;
                letter-spacing: 0.5px;
                transition: all 0.3s ease;
            }
            a:hover {
                background: #0096c7;
                transform: translateY(-2px);
            }
            footer {
                position: absolute;
                bottom: 20px;
                font-size: 0.85rem;
                color: #b5b5b5;
            }
            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>🚀 API do Desafio ASCII</h1>
            <p>O servidor FastAPI está ativo e conectado ao PostgreSQL com sucesso.</p>
            <p>Acesse a documentação interativa abaixo para explorar os endpoints da aplicação.</p>
            <a href="/docs" target="_blank">Abrir documentação Swagger</a>
        </div>
        <footer>Desenvolvido com ❤️ por Lucas França — ASCII Challenge</footer>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

app.include_router(product_controller.router,
                   prefix="/api/produtos",
                   tags=["Produtos"])


@app.get("/health")
def health():
    return {"status": "ok"}
