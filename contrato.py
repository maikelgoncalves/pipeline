from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt #, validate_call 
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Produto A"
    produto2 = "Produto B"
    produto3 = "Produto C"

class Vendas(BaseModel):
        email: EmailStr
        data: datetime
        valor: PositiveFloat
        qtde: PositiveInt
        produto: ProdutoEnum

        # @validate_call('produto')
        # def validacao_produto(cls, v):
        #     return v