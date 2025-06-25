from models.item import Item
from datetime import datetime
from services.arquivo import salvar_estoque, carregar_estoque
import json

class EstoqueController:
    def __init__(self):
        self.estoque = carregar_estoque()
        
    def adicionar_item(self, nome, validade=None, quantidade=1, quantidade_minima=1):
        item = Item(nome, validade, quantidade, quantidade_minima)
        self.estoque.append(item)
        salvar_estoque(self.estoque)
        print(f"\n✅ Item '{nome}' adicionado com sucesso!")
        
    def remover_item(self, nome):
        for i, item in enumerate(self.estoque):
            if item.nome == nome:
                del self.estoque[i]
                salvar_estoque(self.estoque)
                print(f"\n❌ Item '{nome}' removido.")
                return
        print(f"\n⚠️ Item '{nome}' não encontrado ou já removido.")
        
    def editar_item(self, nome, novo_nome=None, nova_validade=None, nova_quantidade=None, nova_qtd_minima=None):
        for item in self.estoque:
            if item.nome == nome and item.data_remocao is None:
                if novo_nome: item.nome = novo_nome
                if nova_validade: item.validade = nova_validade
                if nova_quantidade is not None:
                    item.quantidade = nova_quantidade
                if nova_qtd_minima is not None:
                    item.quantidade_minima = nova_qtd_minima
                item.atualizar_classificacao()
                salvar_estoque(self.estoque)
                print(f"\n✏️ Item '{nome}' atualizado.")
                return
        print(f"\n⚠️ Item '{nome}' não encontrado ou já removido.")
        
    def listar_estoque(self, incluir_removidos=False):
        print("\n📦 Estoque atual:")
        for item in self.estoque:
            if incluir_removidos or item.data_remocao is None:
                print(item)
            
            print()
            
    def listar_estoque_baixo(self):
        print("\n📉 Itens com estoque baixo:")
        encontrou = False
        for item in self.estoque:
            if item.data_remocao is None and item.classificacao == "Baixo":
                print(item)
                encontrou = True
        if not encontrou:
            print("Todos os itens estão com estoque suficiente!")
        print()
        
    def gerar_relatorio_reposicao(self):
        print("\n📋 Relatório de itens para reposição:\n")
        lista_reposicao = []
        
        for item in self.estoque:
            if item.data_remocao is None and item.quantidade < item.quantidade_minima:
                falta = item.quantidade_minima - item.quantidade
                print(f"- {item.nome} (Faltam {falta} unidade(s))")
                lista_reposicao.append({
                    "nome": item.nome,
                    "quantidade_necessaria": falta
                })
                
        if not lista_reposicao:
            print("✅ Todos os itens estão com estoque adequado!\n")
        else:
            print("\n💡 Você pode transformar isso em uma nova lista de compras.")
            
        return lista_reposicao
    
    def gerar_lista_de_compras(self):
        itens_para_comprar = self.gerar_relatorio_reposicao()
        
        if itens_para_comprar:
            with open("data/lista_de_compras.json", "w", encoding="utf-8") as f:
                json.dump(itens_para_comprar, f, ensure_ascii=False, indent=4)
            print("📋 Lista de compras gerada com sucesso em 'data/lista_de_compras.json'!\n")
        else:
            print("Nada foi adicionado à lista de compras.\n")