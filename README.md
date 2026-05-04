# 💧 Sistema de Monitoramento de Reservatório

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![Colorama](https://img.shields.io/badge/Colorama-0.4%2B-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)

## 📚 Sobre o Projeto

**Sistema de Monitoramento de Reservatório** é uma aplicação desenvolvida em Python que exibe alertas visuais coloridos no terminal conforme o nível de água de um reservatório, permitindo identificar rapidamente a situação hídrica atual.

Este projeto foi desenvolvido como atividade educacional no curso de **Desenvolvimento de Sistemas** da **ETEC**.

## 🎯 Objetivo

Fornecer uma ferramenta simples para:
- Receber o nível atual do reservatório informado pelo usuário
- Exibir uma mensagem de alerta com cor correspondente à situação
- Praticar o uso de listas, funções e bibliotecas externas em Python

## ✨ Funcionalidades Principais

- **Lista de níveis**: Armazena as descrições de cada situação do reservatório
- **Cores dinâmicas**: Cada nível exibe uma cor diferente usando a biblioteca `colorama`
- **Validação de entrada**: Rejeita valores não numéricos e fora do intervalo de 1 a 5
- **Tratamento de erros**: Mensagens claras em caso de entrada inválida, sem quebrar o programa
- **Reset do terminal**: Restaura o estilo padrão do terminal após a exibição dos alertas

## 📋 Níveis do Reservatório

| Nível | Situação              | Cor         |
|-------|-----------------------|-------------|
| 1     | Muito baixo (crítico) |  Vermelho   |
| 2     | Baixo                 |  Amarelo    |
| 3     | Médio                 |  Verde      |
| 4     | Alto                  |  Ciano      |
| 5     | Muito alto (alerta)   |  Azul       |

## 💡 Exemplo de Uso

```
Digite o nível do reservatório (1 a 5): 1
Situação do reservatório: Nível 1 - Muito baixo (crítico)   ← exibido em vermelho

Digite o nível do reservatório (1 a 5): 3
Situação do reservatório: Nível 3 - Médio                   ← exibido em verde

Digite o nível do reservatório (1 a 5): abc
Por favor, digite um número válido!                          ← exibido em vermelho
```

## 📁 Estrutura do Projeto

```
monitoramento_reservatorio/
├── AndreyCyrineodaMotta_Ag11_DS_I.py   # Programa principal
└── README.md                       # Este arquivo
```

## 👤 Autor

Andrey Cyrineo da Motta
