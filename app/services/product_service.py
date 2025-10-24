from sqlalchemy.orm import Session
from app.repositories.product_repo import ProductRepository
from app.models.product import Product
from app.schemas.product_schemas import ProductCreate, ProductUpdate
from fastapi import HTTPException
from app.core.logger import logger

class ProductService:
    def __init__(self, db: Session):
        self.repo = ProductRepository(db)

    def list_products(self):
        logger.info("Listando produtos...")
        return self.repo.get_all()

    def get_product(self, product_id: int):
        logger.info(f"Buscando produto id={product_id}")
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        return product

    def create_product(self, data: ProductCreate):
        logger.info(f"Criando produto {data.name}")
        prod = Product(name=data.name, price=data.price, category=data.category)
        return self.repo.create(prod)

    def update_product(self, product_id: int, data: ProductUpdate):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        update_data = data.dict(exclude_unset=True)
        return self.repo.update(product, update_data)

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Produto não encontrado")
        self.repo.delete(product)
        logger.info(f"Produto {product_id} removido com sucesso")
        return {"detail": "Produto removido com sucesso"}
