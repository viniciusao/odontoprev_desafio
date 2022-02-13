## odontoprev_desafio
Desafio técnico Arquiteto de soluções.

### Requisitos
1. *Python versão maior ou igual a **3.8***.
2. *Linux*.

### Usage

1. *git clone <este_repo> && cd <este_repo_dir>*
2. *./setup_hml.sh*

### Rationale
* **Assunções**:
    * Por questões de **tempo** e se tratar dum *teste*, 
      a solução concebida tem pouquíssimas dependências 
      externas, portanto,  a execução e validação é 
      simples e rápida. [1]
    <br>
    <br>
    * Foi-se implementado componentes e funcionalidades 
      da solução em somente algumas partes da aplicação 
      devido ao ponto *[1]*, e no documento _.pdf_ do 
      desafio na seção **cenário** há o seguinte trecho: 
      *“O seu desafio como Arquiteto de Solução (...) 
      desenvolver uma parte da proposta de solução técnica (...)”*.
    <br>
    <br>
    * Também não desenhos/diagramas da arquitetura da aplicação
      devido ao ponto *[1]*, e por ser _**opcional**_ segundo o 
      documento _.pdf_ do desafio na seção _**cenário**_.
<br>
<br>
* **Endpoints**:
    * Premissas:
        * */eventos*: A propriedade `código` é do tipo `inteiro`. 
          Por causa da descrição do `motor de regras` no *.pdf* do desafio.
<br>
<br>
* **Arquitetura**:
    * **Implementação**:
        * Banco de dados: _**sqlite**_.
        * Lógica backend/endpoint: _**AWS Chalice**_ (_framework_),
          _**marshmallow**_.
            * O framework acima é excelente para _**POC’s**_, 
              além de possuir muitas funcionalidades úteis, 
              _middlewares e.g_, também vem com um _light built-in http server_ 
              para testes nos _endpoints_ desenvolvidos.
        
        * Métodologia de desenvolvimento (_parcial_): _**TDD**_
    <br>
    <br>
    * **Análise**:
        <p>Um dos primeiros passos é mapear os `endpoints`: 
        construir `schemas` a partir da especificação, 
        relações com outros endpoints, etc. Um pacote
        no `python` que auxilia bastante nisso é o `marshmallow`, 
        pois este permite validar `input data`. 
        Fora notadas algumas relações e requisitos 
        compartilhados entre os `endpoints` neste desafio, 
        logo, definiu-se alguns `schemas` para validação no 
        diretório: /endpoints/schemas. Por meio do 
        `pytest + TDD`, desenvolveu-se esses `schemas`.</p>
        <br>
        <p>Em seguida, fora percebido que os `endpoints` 
        4 (Guia de Tratamento Odontológico), 5 (Prontuário Virtual) 
        e 6 (Motor de regras) são condicionais a informações 
        registradas no banco de dados através de cadastro nos 
        `endpoints` 1 (Beneficiário), 2 (Dentista) e 3 (Evento). 
        Quanto aos endpoints 4 e 6, `middlewares` auxiliarão.</p>
      <br>
    * **Componentes**:
        * _Schemas_: Responsável por validar os dados que o _endpoint_ recebe.
        * _Cli_: Responsável por fazer o _setup_ da aplicação antes de iniciar.
        * _Middlewares_: Responsável por validações posteriores na execução da lógica codada nos _endpoints_.
        * _Interfaces_:
            * **Cursor**: Permite a realização de _queries_ no banco de dados a partir de qualquer componente da aplicação.
            * **Motor de regras**: Regras de negócios da aplicação, as quais as _middlewares_ validarão.
        * _Helpers_: Alguns componentes possuem operações muito frequentemente usadas, portanto, este é responsável por desacoplar e abstrair a complexidade dessas.
        * _Chalice views_: Onde define-se os endpoints e suas lógicas, as quais se utilizam de outros componentes.
    <br>
    <br>
    * **Comentários**:
    A partir da Análise citada nesta seção, também foi interessante perceber
    as relações entre os _endpoints_, e a partir disso, tentar o máximo
    reduzir a complexidade em componentes frequentemente usados como foi o caso
    das operações: Cadastrar e Get. Todas as views da aplicação executam os dois,
    assim, fora definidos funções helpers para tal função, mantendo o principio _KISS_.
    Além disso, as interfaces foram desenvolvidas com os principios _SOLID_ em mãos.
    Não obstante, o _design pattern_ utilizado foi o que o próprio framework
    aconselha como melhores práticas: _Modularização por meio de blueprints_.
    <br>
    <br>
    * **Poréns**: A solução é adequada para uma _**POC**_, e passível de escalar alterando
      somente as ferramentas utilizadas, o código si se mantém.
      Um dos primeiros pontos é o _sqlite_ que não é assincrono e
      e seus _datatypes_ são reduzidos, apesar das precauções quanto a _deadlocks_,
      em um ambiente altamente requisitado não se manteria, uma alternativa seria uma
      solução _cloud_ como _**DynamoDB**_ da _AWS_. Pensando nisto, utilizou-se o framework
      _**aws chalice**_ que também é performático em produção. Outro ponto também é quanto
      a validação de _input data_, o ideal seria o _gateway_ da _API_ realizar, como é feito
      em alguns ambientes _cloud_ que disponibilizam serviços de _**REST API**_.
    

### TODO

- **Componentes**:
    * [x] *Schemas*
        * [x] Compartilhado
        * [x] Beneficiário
        * [x] Dentista
  
    * [x] *CLI*
        * [x] Criar banco de dados e tabelas

    * [x] *Middlewares*
        * [x] Simular sistemas distribuídos (`requests`)
    
    * [x] *Interfaces*
        * [x] Cursor (*Banco de dados*)
        * [x] Motor de regras
    
    * [x] *Helpers*
    * [x] *Chalice views*
        * [x] beneficiários
        * [x] dentistas
        * [x] eventos
        * [x] guias