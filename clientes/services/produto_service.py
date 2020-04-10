from ..models import Produto
from django.db import connection

def listar_produtos():
    produtos = Produto.objects.all()
    return produtos

def listar_produto_id(id):
    produto = Produto.objects.get(id=id)
    return produto

def inserir_produto(produto):
    Produto.objects.create(nome=produto.nome, descricao=produto.descricao, valor=produto.valor)

def editar_produto(produto, produto_novo):
    produto.nome = produto_novo.nome
    produto.descricao = produto_novo.descricao
    produto.valor = produto_novo.valor
    produto.save(force_update=True)

def listar_pedido_id(id):
    produto = Produto.objects.get(id=id)
    for i in produto.produtos.all():
        print(i.nome)
    print(connection.queries)
    print(len(connection.queries))
    return produto