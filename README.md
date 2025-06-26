## Gerenciador de Estoque (stock-manager) 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![JSON](https://img.shields.io/badge/JSON-Data%20Format-10a5d4?logo=json)

Uma aplicação de linha de comando em Python para gerenciar o estoque de itens, controlar reposições e gerar listas de compras automaticamente.

## 🎮 Sobre o projeto
stock-manager é uma aplicação simples de terminal feita em Python, ideal para aprender lógica de programação, modularização e manipulação de listas com persistência de dados. Foi planejada como base para uma futura
integração com um sistema de lista de compras e posterior transformação em um app mobile.

## 🔧 Funcionalidades
- Adicionar itens com nome, validade, quantidade e quantidade mínima.
- Remover itens do estoque.
- Editar nome, validade, quantidade e quantidade mínima de um item.
- Classificação automática do estoque (baixo, médio ou alto).
- Listar todos os itens cadastrados.
- Listar apenas os itens com estoque baixo.
- Gerar relatório de itens para reposição.
- Gerar uma lista de compras com base nos itens que precisam ser repostos.

## 📁 Estrutura do projeto
- `app.py`: Arquivo principal com o menu do sistema.
- `models/item.py`: Classe `Item`, que representa os dados de cada produto.
- `controllers/estoque_controller.py`: Lógica de manipulação dos itens.
- `services/arquivo.py`: Leitura e escrita dos dados no arquivo `.json`.
- `utils/`: (pasta reservada para funções auxiliares, se necessário).
- `data/`
  - `estoque.json`: Armazena os dados do estoque (não incluído no repositório).
  - `lista_de_compras.json`: Lista gerada automaticamente (não incluída).
- `.gitignore`: Arquivos/pastas ignorados pelo Git.
- `README.md`: Este arquivo (em português e em inglês).

## 🚀 Como executar
- Python 3.8 ou superior instalado.
- Terminal (PowerShell, CMD, Terminal Linux/Mac, etc.).

#### Windows/Linux/macOS
##### Passo 1. Clone o repositório:
```bash
git clone https://github.com/YunaKimari/Stock-Manager.git
cd stock-manager
```

##### Passo 2. Execute o programa:
```bash
python app.py
```

## 📄 Licença
Este projeto está licenciado sob a Licença MIT.

## 👤 Autor
- YunaKimari (Denise Rocha)
- GitHub: github.com/YunaKimari

---

## Inventory Manager (stock-manager) 
![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![JSON](https://img.shields.io/badge/JSON-Data%20Format-10a5d4?logo=json)

A simple Python terminal app to manage item stock, track restocking needs, and automatically generate shopping lists.

## 🎮 About th project
stock-manager is a basic Python command-line application, great for learning programming logic, modular structure, and persistent list handling. It was designed as a foundation for integrating with a shopping list system
and evolving into a mobile app.

## 🔧 Features
- Add items with name, expiration date, quantity, and minimum quantity.
- Remove items from stock.
- Edit item name, expiration date, quantity, and minimum quantity.
- Automatic stock classification (low, medium, or high).
- List all registered items.
- List only items with low stock.
- Generate a report of items that need restocking.
- Generate a shopping list based on missing items.

## 📁 Project structure
- `app.py`: Main file with meny system.
- `models/item.py`: `Item` class to represent product data.
- `controllers/estoque_controller.py`: Logic for managing items.
- `services/arquivo.py`: File read/write logic for `.json`.
- `utils/`: (folder reserved for helper functions, if needed).
- `data/`
  - `estoque.json`: Local storage for stock data (not included).
  - `lista_de_compras.json`: Generated shopping list (not included).
- `.gitignore`: Git ignored files and folders.
- `README.md`: This file (in both Portuguese and English).

## 🚀 How to run
- Python 3.8 or higher installed.
- Terminal (PowerShell, CMD, Linux/Mac Terminal, etc.).

#### Windows/Linux/macOS
##### Step 1. Clone the repository:
```bach
git clone https://github.com/YunaKimari/Stock-Manager.git
cd stock-manager
```

#### Step 2. Run the application:
```bash
python app.py
```

## 📄 License
This project is licenced under the MIT License.

## 👤 Author
- YunaKimari (Denise Rocha)
- GitHub: github.com/YunaKimari
