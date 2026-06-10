# CIEBP - ÂNGELO MENDES

---

# Automação de Cadastro de Funcionários com PyAutoGUI

## Objetivos de Aprendizagem

- Automação de tarefas repetitivas.
- Manipulação de arquivos CSV.
- Navegação por formulários utilizando teclado.
- Integração entre Python e aplicações web.
- Aplicação prática de conceitos de produtividade e automação de processos.

## Descrição

Este projeto tem como objetivo automatizar o preenchimento de um formulário web utilizando Python e a biblioteca PyAutoGUI.

Os dados são carregados a partir de um arquivo CSV contendo informações de funcionários. Para cada registro, o sistema navega pelos campos do formulário utilizando o teclado, insere os valores correspondentes e realiza o cadastro automaticamente.

**A atividade foi desenvolvida com fins educacionais para demonstrar conceitos de automação de interface gráfica (GUI Automation), manipulação de arquivos CSV e integração entre diferentes tecnologias.**

---

## Tecnologias Utilizadas

- Python 3
- PyAutoGUI
- CSV (biblioteca padrão do Python)

## Estrutura do Projeto

```text
projeto/
│
├── database/
│   └── banco_funcionarios_ficticio_1000.csv
│
├── javascript/
│   └── index.html
│   └── app.js
└── automacao.py
```

## Funcionamento

O script executa as seguintes etapas:

1. Abre a janela "Executar" do Windows (Win + R).
2. Carrega a página HTML contendo o formulário.
3. Aguarda o carregamento da interface.
4. Lê os registros presentes no arquivo CSV.
5. Preenche os campos do formulário automaticamente.
6. Aciona o botão de cadastro.
7. Retorna o foco para o primeiro campo.
8. Repete o processo até o término dos registros.

## Estrutura Esperada do CSV

O arquivo CSV deve possuir os campos separados por ponto e vírgula (;).

Exemplo:

```csv
João Silva;Analista de Sistemas;TI;5500.00;São Paulo;SP;2024-01-15
Maria Souza;Gerente de Projetos;Gestão;8200.00;Campinas;SP;2023-08-10
```

Os sete primeiros campos de cada linha serão utilizados para preencher o formulário.

## Instalação

Instale a dependência necessária:

```bash
pip install pyautogui
```

## Execução

Ajuste os caminhos dos arquivos no script:

```python
caminho_navegador = "caminho/para/index.html"
dados = "caminho/para/banco_funcionarios_ficticio_1000.csv"
```

Execute o programa:

```bash
python automacao.py
```

## Observações

- Não utilize o teclado ou mouse durante a execução da automação.
- A página HTML deve estar preparada para receber navegação via tecla TAB.
- O tempo de carregamento pode variar de acordo com o computador. Caso necessário, aumente o valor do comando:

```python
auto.sleep(4)
```

---

##### Idealizadores: _profº Luiz Henrique e profº Marcos Paulo_
