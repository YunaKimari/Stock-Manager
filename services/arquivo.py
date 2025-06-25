import json
import os
from models.item import Item

CAMINHO_ARQUIVO = "data/estoque.json"

def salvar_estoque(lista_de_itens):
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        dados = [item.__dict__ for item in lista_de_itens]
        json.dump(dados, f, ensure_ascii=False, indent=4)
        
def carregar_estoque():
    if not os.path.exists(CAMINHO_ARQUIVO):
        return[]
    
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        dados = json.load(f)
        estoque = []
        for item_dict in dados:
            item = Item(
                nome=item_dict["nome"],
                validade=item_dict["validade"],
                quantidade=item_dict["quantidade"],
                quantidade_minima=item_dict["quantidade_minima"]
            )
            item.data_insercao = item_dict["data_insercao"]
            item.data_remocao = item_dict["data_remocao"]
            item.atualizar_classificacao()
            estoque.append(item)
        return estoque