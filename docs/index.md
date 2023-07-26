# Documentação das Tarefas

### Tarefa 1: Variável de Ambiente

**Modificar a aplicação para consumir uma variável de ambiente chamada `NAME` e, no lugar de "World", exibir o valor dessa variável.**

Para a aplicação consumir a variável de ambiente `NAME`, basta usar o módulo `os` nativo do Python. O método `os.environ.get()` recebe duas strings de argumento. A primeira refere-se ao nome da variável de ambiente. Se ela existir, então a função retorna seu valor, senão, retorna o segundo argumento passado.

    @app.route("/")
    def hello_world():
    name = os.environ.get("NAME", "World")
    return f"Hello, {name}!"

### Tarefa 2: .gitignore

**Modificar o arquivo `.gitignore` para que seja adequado a uma aplicação Python.**

No arquivo `.gitignore`, faz-se referência a arquivos/diretórios com as seguintes características:

- Arquivos otimizados / binários
- Ambientes virtuais Python (`venv`)
- Arquivos específicos do IDE
- Arquivos de Log

entre outros.

### Tarefa 3: Fluxo de Desenvolvimento

**Elaborar, implementar e reforçar o fluxo de desenvolvimento do repositório.**

Sugestão de fluxo de desenvolvimento com o seguinte padrão de criação/merge de branches:

- Branches Principais:
    - `master`: Representa a versão estável e pronta para produção da aplicação.
    - `develop`: Serve como branch de integração para o desenvolvimento contínuo.

- Branches de Funcionalidades:
    - Para cada nova funcionalidade ou tarefa, crie uma nova branch a partir da `develop`.
    - Dê um nome descritivo à branch de funcionalidade, como `feature/user-authentication`.

- Hotfix:
    - Se houver um bug crítico na versão de produção, crie uma branch de Hotfix a partir da `master`.
    - Dê um nome descritivo à branch de Hotfix, como `hotfix/fix-login-issue`.

- Branches de Lançamento (Release):
    - Quando a branch `develop` atingir um ponto estável para um lançamento, crie uma branch de release a partir dela.
    - Dê um nome da branch com base no número da versão, como `release/1.0`.

- Merging:
    - Faça merge nas branches de funcionalidades de volta à `develop` assim que as funcionalidades estiverem concluídas e testadas.
    - Faça merge nas branches de release tanto na `develop` quanto na `master` após testar e garantir a estabilidade.
    - Faça merge nas branches de Hotfix tanto no `develop` quanto no `master` para aplicar correções críticas à versão de produção.
    - Sempre usar *Pull Requests* para as branches principais (branches protegidas).

- Tagging:
    - Sempre que dar merge numa branch de release na `master`, crie uma tag para a versão específica. Isso facilita o rastreamento dos lançamentos.

Mensagens de commits devem deve ser estruturada seguindo o padrão [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) `v1.0.0`:

A especificação Conventional Commits fornece um conjunto simples de regras para criar um histórico de commits explícito, o que facilita a escrita de ferramentas automatizadas por cima dele. Essa convenção se alinha com o SemVer, descrevendo as funcionalidades, correções e mudanças que quebram compatibilidade presentes nas mensagens de commit.

    <tipo>[escopo opcional]: <descrição>

    [corpo opcional]

    [rodapé(s) opcional(is)]

### Tarefa 4: Boas Práticas no Repositório

**Consolidar boas práticas no repositório através de ferramentas de análise estática, hooks de pré-commit, etc. a seu critério.**

Foram usadas as seguintes ferramentas com o intuito de consolidar boas práticas no repositório:

- **Poetry**: ferramenta de gerenciamento de dependências e empacotamento de projetos Python. Com `poetry.lock` garante um snapshot das dependencias podendo ser facilmente replicado em outras instâncias.
- **Semgrep**:  ferramenta de análise estática de código que permite encontrar e corrigir problemas de segurança, bugs e más práticas em seus projetos de código-fonte. Ele usa regras de análise baseadas em padrões e expressões regulares para identificar possíveis vulnerabilidades e problemas no código.
- **Black**: garante que o código siga um estilo de formatação consistente e padronizado, tornando-o mais legível e mantendo uma aparência uniforme em projetos compartilhados por várias pessoas.
- **Isort**: ferramenta de ordenação de importações em código fonte Python. Ele reorganiza as declarações de importação em ordem alfabética e agrupa-as de forma coerente, tornando o código mais organizado.
- **Flake8**: combina várias ferramentas populares, como o PyFlakes (verificador de erros estáticos) e o pycodestyle (verificador de conformidade de estilo PEP 8), além de verificar a complexidade do código com o mccabe. O Flake8 ajuda a identificar problemas potenciais no código, como erros de sintaxe, problemas de estilo e complexidade excessiva.
- **MKDocs**: ferramenta de criação de documentação estática em Markdown. Ele possui várias facilidades como o comando `mkdocs serve` que inicia um servidor local em que você pode visualizar a documentação no navegador em tempo real enquanto faz alterações no conteúdo ou no estilo. Além do comando `mkdocs gh-deploy`, que compila a documentação e a implanta na branch "gh-pages" do repositório do GitHub, tornando-a publicamente acessível em um URL específico do GitHub Pages.
- **PyTest**: oferece recursos poderosos, como detecção automática de testes e testes parametrizados. Com PyTest-cov foi possível intregá-lo com a ferramente descrita a seguir.
- **Coverage**: com essa ferramenta é possível medir a cobertura de código do projeto, ou seja, quantas linhas de código foram executadas durante a execução dos testes. Com o comando `coverage html` ele gera uma aplicação web local (hospedada por padrão na porta `8000`) contendo relatórios detalhados que mostram quais partes do código não foram cobertas pelos testes.
- **TaskiPy**: diminui o quanto digitamos para usar as ferramentas que foram descritas até então. A ideia é definir as tarefas numa sessão do `pyproject.toml`, e estas são executadas com um comando simples (`task <nome do comando>`).

        [tool.taskipy.tasks]
        ...
        lint = "semgrep scan --verbose --config auto && black . && isort . && flake8 ."
        docs = "mkdocs serve"
        docs_deploy = "mkdocs gh-deploy"
        test = "pytest -s -x --cov=src"
        cov = "coverage html"

- **pre-commit**: permite configurar *pre-commit hooks* que são executados antes de um commit ser realizado. Neste caso, foi incluido a `task test` definido com o Taskipy além da checagem estática com o semgrep, black, isort e flake8, além de verificar marcador de ordem de byte UTF-8, corrigir pragma de codificação do Python, remover espaços em branco no final de cada linha, não permitir fazer commit em branches protegidas e verificar se arquivos grandes foram adicionados.

- **Code Owners**: recurso que permite atribuir revisores específicos para determinados arquivos ou pastas em um repositório do GitHub. Ao definir um arquivo CODEOWNERS na pasta .github, é especificado os proprietários responsáveis por revisar e aprovar as alterações em determinados caminhos do código-fonte. Neste projeto exemplo, apenas meu usuário foi definido como revisor Default de todas as mudanças.

### Tarefa 5: Ambiente de Produção

**Preparar a aplicação para que seja production-ready.**

Embora o Flask seja um excelente framework para criar aplicativos web em Python de forma rápida e simples, ele não é considerado "production ready" por si só. O servidor embutido no Flask é adequado apenas para fins de desenvolvimento e testes. Ele não é projetado para lidar com cargas de tráfego significativas ou oferecer recursos de alta disponibilidade.

Com isso, foi escolhido o **Guonicorn** (Green Unicorn) como ferramenta para tal: um servidor HTTP WSGI (Web Server Gateway Interface) que permite que a aplicação atenda a mais solicitações ao mesmo tempo.

### Tarefa 6: Containerização

**Criar arquivos e scripts para que a aplicação possa ser executada em um container.**

Foi criado um **Dockerfile** que copia somente os arquivos necessários para que o container instale as dependências do projeto (`poetry.lock` e `pyproject.toml`), e rode a aplicação (conteúdo do diretório `src/`). Isso é feito com o auxílio de um arquivo `.dockerignore`.

Como `ENTRYPOINT`, o container executa o script `scope.sh` que roda a aplicação com o servidor do próprio flask caso exista uma variável de ambiente `LOCAL=True` . Caso contrário, o Guonicorn é usado.

### Tarefa 7: Desenvolvimento Local

**Elaborar um modelo de desenvolvimento que permita a execução da aplicação em um ambiente de desenvolvimento local.**

O modo Debug do Flask, além de fornecer informações detalhadas sobre erros e exceções que ocorrem durante a execução, também ativará o recurso de "auto-reload", que fará com que a aplicação seja recarregada automaticamente sempre que ocorrer uma alteração no código.

Com um arquivo `docker-compose.yml`, definimos a criação de um container na nossa máquina local que terá a variável de ambiente `LOCAL=True`, que ativa o modo Debug do Flask e roda a aplicação sem o Guonicorn.

Além disso, é usado um Volume mapeando o repositório local ao diretório da aplicação no container. Com isso, toda modificação do código fonte também é alterado dentro do container, e com a função DEBUG, podemos ver as modificações sem precisar rebuildar a imagem.

Para subir o container localmente, basta usar a task definida no Taskipy `task up` (subir o container) `task down` (parar)

    [tool.taskipy.tasks]
    up = "docker compose up -d --build --force-recreate"
    down = "docker compose down --rmi local"

### Tarefa 8: CI/CD

**Construir pipelines de CI/CD para a aplicação utilizando GitHub Actions. Esse item possui forte relação com o fluxo de desenvolvimento, pois deve compreender o deployment em dois ambientes diferentes: homologação e produção. O deployment da aplicação deve ser realizado em um serviço serverless da Google Cloud Platform.**

GitHub Actions é um serviço de automação oferecido pelo GitHub para facilitar a criação de fluxos de trabalho automatizados. Por meio de arquivos yaml na pasta `.github/workflow` do repositório, pode-se definir e configurar tarefas personalizadas que são acionadas por eventos, como push de código, abertura de pull requests ou outros eventos do repositório.

- **docs.yml**: com todo "push" na `main` (apenas por meio de um *Pull Request* aceito) o site de documentação gerado pelo MKDocs é implantada na plataforma GitHub Actions.

- **lint.yml**: com todo *Pull Request*, a task de "lint code" com as ferramentas Semgrep para seguir boas práticas de segurança e Black, Isort e Flak8 para garantir a boa formatação do código Python. Além da ferramente hadolint, por meio de uma action para a devida formatação do Dockerfile seguindo especificações formais.

- **cd.yml**: com todo "push" na `main` (apenas por meio de um *Pull Request* aceito) a imagem Docker da aplicação é buildada para o Container Registry da Google, e depois é implantada no Google Run. A autorização é feita passando a Json Service Account Access Key por meio de um secret do repositório. Além disso, há um arquivo `cd-dev.yml` seguindo o mesmo fluxo, mas para a implantação de homologação.

    Obs: A recomendação da Cloud Run é que os sistemas de CI/CD não definam nem alterem configurações para permitir "invocações" não autenticadas. Novas implantações são automaticamente configuradas como serviços privados, enquanto a implantação de uma revisão de um serviço público (não autenticado) preservará a configuração de IAM como pública (não autenticada). Sendo assim, depois da primeira implantação, deve-se realizar o seguinte comando num ambiente com autenticação para deixar a aplicação de produção pública.

        gcloud run services add-iam-policy-binding [SERVICE_NAME] \
            --member="allUsers" \
            --role="roles/run.invoker"