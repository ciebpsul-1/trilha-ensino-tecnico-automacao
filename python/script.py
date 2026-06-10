import pyautogui as auto
import csv

# Caminho para o arquivo HTML que contém o formulário
caminho_navegador = "..."

# Caminho para o arquivo CSV com os dados dos funcionários
dados = "../database/banco_funcionarios_ficticio_1000.csv"

# Abre a janela "Executar" do Windows (Win + R)
auto.hotkey('win', 'r')

# Digita o caminho do arquivo HTML
auto.write(caminho_navegador)

# Abre a página no navegador padrão
auto.press('enter')

# Aguarda o carregamento da página
auto.sleep(4)

# Abre o arquivo CSV para leitura
with open(dados, mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)

    # Percorre cada registro do arquivo
    for row in reader:

        # Divide os dados da linha utilizando ";" como separador
        campo = row[0].split(";")

        # Preenche os sete campos do formulário
        for funcionario in campo[:7]:

            # Avança para o próximo campo do formulário
            auto.press('tab')

            # Digita o valor correspondente ao campo atual
            auto.write(funcionario.strip())

        # Navega até o botão de cadastro
        auto.press('tab')

        # Envia o formulário
        auto.press('enter')

        # Retorna o foco ao primeiro campo do formulário
        # utilizando Shift + Tab repetidamente
        for _ in range(8):
            auto.hotkey('shift', 'tab')
