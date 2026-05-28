from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///bancodedados.db")
Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()

class Produtos(Base):
    __tablename__ = "produtos"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    preco = Column("preco", Float)
    quantidade = Column("quantidade", Integer)

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    


class Usuario(Base):
    __tablename__ = "usuarios"
    userid = Column("userid", Integer, primary_key=True, autoincrement=True)
    login = Column("login", String,)
    senha = Column("senha", String)






Base.metadata.create_all(bind=db)

insert_nome = input("Nome: ")
insert_preco = input("Preço: ")
insert_quantidade = input("Quantidade: ")
produto = Produtos(nome=insert_nome, preco=insert_preco, quantidade=insert_quantidade)
session.add(produto)
session.commit()