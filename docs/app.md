# Documentação da Aplicação

Foi implementado uma apresentação um pouco mais amigável aos olhos com o framework **Jinja2**. O Jinja é um mecanismo de modelo (template engine) em Python que permite incorporar lógica e dados dinâmicos em modelos estáticos.

Além disso, foi implementado, ao caminho `/word` do serviço, uma tela de geração de Word Art de diferentes tipos. O Word Art é uma forma de arte textual que utiliza caracteres ASCII para criar representações visuais de palavras ou frases.

Project tree

        .
        ├── Dockerfile
        ├── README.md
        ├── docker-compose.yaml
        ├── docs
        │   ├── app.md
        │   ├── assets
        │   │   └── logo.png
        │   └── index.md
        ├── mkdocs.yml
        ├── poetry.lock
        ├── pyproject.toml
        ├── scripts
        │   ├── run_isort.sh
        │   ├── run_semgrep.sh
        │   ├── run_test.sh
        │   └── scope.sh
        ├── src
        │   ├── app.py
        │   └── templates
        │       ├── hello.html
        │       └── word_art.html
        └── tests
            └── test_api.py

---
### Procedimentos para contribuir com o desenvolvimento no repositório.

Clonar o repositório

    git clone https://github.com/storino/emd

No ambiente de desenvolvimento, instalar poetry para gerenciamento de dependências

    pip3 install poetry

Instalar as dependências para desenvolvimento

    poetry install

Instalar os hooks de pré-commit

    pre-commit install

Para começar o desenvolvimento, entre no ambiente virtual gerado pelo poetry pelo comando

    poetry shell

Para sair, basta usar o comando

    deactivate

Crie um arquivo `.env` com as seguintes variáveis

    NAME= # Nome para quem dar "Olá" :)
    PORT= # Porta da aplicação
    LOCAL= # Setar ambiente local (Sem Guonicorn e Debug = true)

Inicialize e pare o container local com os comandos

    task up
    task down

Garantir a boas práticas de segurança e a formatação do código com

    task lint

Rode uma instância local da documentação com

    task docs

Rode os testes definidos nos scripts na pasta test/ e veja o quanto os testes atuais cobrem o código com, respectivamente:

    task test
    task cov

Siga as orientações de uso/merge de branches

> Descrição da Tarefa 3: Fluxo de Desenvolvimento