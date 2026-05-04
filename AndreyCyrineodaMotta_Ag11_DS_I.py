from colorama import Fore, Style, init

init(autoreset=True)

# Lista com os níveis do reservatório
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função para definir a cor conforme o nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função para exibir o status do reservatório
def exibir_status(nivel):
    if nivel < 1 or nivel > 5:
        print(Fore.WHITE + "Nível inválido!")
        return
    
    cor = definir_cor(nivel)
    mensagem = niveis[nivel - 1]
    
    print(cor + f"Situação do reservatório: {mensagem}")

# ===== PROGRAMA PRINCIPAL =====

try:
    nivel_atual = int(input("Digite o nível do reservatório (1 a 5): "))
    exibir_status(nivel_atual)
except ValueError:
    print(Fore.RED + "Por favor, digite um número válido!")

# Garante reset final antes de sair
input("Pressione Enter para sair...")