from controllers.estoque_controller import EstoqueController

def exibir_menu():
    print("=== MENU DO ESTOQUE ===")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Editar item")
    print("4 - Listar todos os itens")
    print("5 - Listar itens com estoque baixo")
    print("6 - Gerar relatório de reposição")
    print("7 - Gerar lista de compras")
    print("8 - Sair")
    
def main():
    controller = EstoqueController()
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome do item: ")
            validade = input("Data de validade (ou deixe em branco): ")
            validade = validade if validade.strip() else None
            try:
                quantidade = int(input("Quantidade inicial: "))
                qtd_minima = int(input("Quantidade mínima: "))
            except ValueError:
                print("⚠️ Quantidades devem ser números inteiros.")
                continue
            controller.adicionar_item(nome, validade, quantidade, qtd_minima)
            
        elif opcao == "2":
            nome = input("Nome do item a remover: ")
            controller.remover_item(nome)
            
        elif opcao == "3":
            nome = input("Nome do item a editar: ")
            novo_nome = input("Novo nome (ou deixe em branco): ")
            nova_validade = input("Nova validade (ou deixe em branco): ")
            try:
                nova_quantidade = input("Nova quantidade (ou deixe em branco): ")
                nova_qtd_minima = input("Nova quantidade mínima (ou deixe em branco): ")
                
                nova_quantidade = int(nova_quantidade) if nova_quantidade.strip() else None
                nova_qtd_minima = int(nova_qtd_minima) if nova_qtd_minima.strip() else None
            except ValueError:
                print("⚠️ Quantidades devem ser números inteiros.")
                continue
            
            controller.editar_item(
                nome,
                novo_nome if novo_nome.strip() else None,
                nova_validade if nova_validade.strip() else None,
                nova_quantidade,
                nova_qtd_minima
            )
            
        elif opcao == "4":
            controller.listar_estoque()
            
        elif opcao == "5":
            controller.listar_estoque_baixo()
            
        elif opcao == "6":
            controller.gerar_relatorio_reposicao()
            
        elif opcao == "7":
            controller.gerar_lista_de_compras()
            
        elif opcao == "8":
            print("Encerrando o programa.")
            break
        
        else:
            print("⚠️ Opção inválida.")
            
if __name__ == "__main__":
    main()