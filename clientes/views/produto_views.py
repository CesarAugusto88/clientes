from clientes.forms.produto_forms import ProdutoForm
from ..forms import produto_forms
from ..entidades import produto

from ..entidades.produto import Produto
from ..services import produto_service

from django.shortcuts import render, redirect


def listar_produtos(request):
    produtos = produto_service.listar_produtos()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

def inserir_produto(request):
    if request.method == "POST":
        form_produto = ProdutoForm(request.POST)
        if form_produto.is_valid():
            nome = form_produto.cleaned_data["nome"]
            descricao = form_produto.cleaned_data["descricao"]
            valor = form_produto.cleaned_data["valor"]
            produto_novo = Produto(nome=nome, descricao=descricao, valor=valor)
            produto_service.inserir_produto(produto_novo)
    else:
        form_produto = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form_produto':form_produto})

def listar_produto_id(request, id):
    produto = produto_service.listar_produto_id(id)
    return render(request, 'produtos/lista_produto.html', {'produto': produto})

def editar_produto(request, id):
    produto_antigo = produto_service.listar_produto_id(id)
    form_produto = produto_forms.ProdutoForm(request.POST or None, instance=produto_antigo)
    if form_produto.is_valid():
        nome = form_produto.cleaned_data["nome"]
        descricao = form_produto.cleaned_data["descricao"]
        valor = form_produto.cleaned_data["valor"]
        produto_novo = produto.Produto(nome=nome, descricao=descricao, valor=valor)
        produto_service.editar_produto(produto_antigo, produto_novo)
        return redirect('listar_produtos')
    return render(request, 'produtos/form_produto.html', {'form_produto': form_produto})