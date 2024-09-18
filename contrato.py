from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt 
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Produto A"
    produto2 = "Produto B"
    produto3 = "Produto C"

class Vendas(BaseModel):
        
    """
    Classe de vendas do meu banco de dados

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da comra
        valor (PositiveFloat): valor da compra
        qtde (PositiveInt): qtde de produtos
        produto (ProdutoEnum): produto

    """

    email: EmailStr
    data: datetime
    valor: PositiveFloat
    qtde: PositiveInt
    produto: ProdutoEnum