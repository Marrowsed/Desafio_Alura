![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Desafio_Alura
Alura Challenge Back-End 2

<h1> Tecnologias Usadas</h1>
<img src="https://www.django-rest-framework.org/img/logo.png" alt="Django Rest Framework">
<ul>
<li><a href="https://www.djangoproject.com/" target="_blank">Django</a> - O propósito do Django está no desenvolvimento de aplicações web e sites.</li>
<li><a href="https://www.django-rest-framework.org/" target="_blank">Django Rest Framework</a> - Desenvolvimento de web API'S de forma simples e ágil.</li>
</ul>


<h1>Controle Financeiro</h1>
Uma API onde você controla seu controle financeiro separado por:
<ul>
  <li><a href="#receitas">Receitas</a></li>
  <li><a href="#despesas">Despesas</a></li>
</ul>

<h1>Métodos Disponíveis</h1>
<ul>
  <li>GET - Retornando Informações</li>
  <li>POST - Inserir Informações</li>
  <li>PUT - Atualizar Informações</li>
  <li>DELETE - Deletar Informações</li>
</ul>

<h1>Endpoints</h1>

<h2>Cadastro</h2>
<b>Necessário para utilizar todos os endpoints !</b>
<ul>
  <li>/registro [POST]</li>
</ul>  
<b> Exemplo de Envio</b>

  ```json
{
	"username": "Usuário",
	"password": "Senha",
	"password2": "Senha",
	"email": "E-mail",
	"first_name": "Nome",
	"last_name": "Sobrenome"
}
```

<b>Exemplo de Sucesso</b>

```json
{
	"username": "Usuário",
	"email": "E-mail",
	"first_name": "Primeiro Nome",
	"last_name": "Último Nome"
}
```

<b>Exemplo de Erro</b>
 
 ```json
{
	"password": [
		"Senhas não conferem"
	]
}

 ```

<h2 id="receitas">Receitas [GET/POST/PUT/DELETE]</h2>
<ul><b>Basic Auth</b>
  <li>username</li>
  <li>password</li>
</ul>  

<ul>
  <li>/receitas [GET]</li>
  <b>Lista as Receitas</b>
  <li>/receitas/ [POST]</li>
  <b>Adiciona uma Receita nova</b>
  <li>/receitas/{pk}/ [PUT/PATCH/DELETE]</li>
  <b>Edita / Deleta uma Receita</b>
  <li>/receitas/{ano}/{mês} [GET]</li>
  <b>Todas as Receitas por Ano e Mês</b>
  <li>/receitas/?descricao= [GET]</li>
  <b>Todas as Receitas por Descrição</b>
</ul>

<b> Exemplo de Retorno Positivo: </b>
  ```json
  [
	{
		"id": "ID da Receita",
		"descricao": "Descrição da Receita",
		"valor": "Valor da Receita (Ex: 1000)",
		"data": "Data da Receita (Ex: 25-12-2000)"
	},
  ]
  ```
<b> Exemplo de Retorno Negativo: </b>
```json
{
	"detail": "As credenciais de autenticação não foram fornecidas."
}
```
```json
{
	"descricao": [
		"Este campo é obrigatório."
	],
	"valor": [
		"Este campo é obrigatório."
	],
	"data": [
		"Este campo é obrigatório."
	]
}
```

<h2 id="despesas">Despesas [GET/POST/PUT/DELETE]</h2>
<ul><b>Basic Auth</b>
  <li>username</li>
  <li>password</li>
</ul>  

<ul>
  <li>/despesas [GET]</li>
  <b>Lista as Despesas</b>
  <li>/despesas/ [POST]</li>
  <b>Adiciona uma Despesa nova</b>
  <li>/despesas/{pk}/ [PUT/PATCH/DELETE]</li>
  <b>Edita / Deleta uma Despesa</b>
  <li>/despesas/{ano}/{mês} [GET]</li>
  <b>Todas as Despesas por Ano e Mês</b>
  <li>/despesas/?descricao= [GET]</li>
  <b>Todas as Despesas por Descrição</b>
</ul>
<b> Exemplo de Retorno Positivo:</b>

  ```json
  [
	{
		"id": "ID da Despesa",
		"descricao": "Descrição da Despesa",
		"categoria": "Categoria da Despesa",
		"valor": "Valor da Despesa (Ex: 1000)",
		"data": "Data da Despesa (Ex: 25-12-2000)"
	}
  ]
  ```

<b> Exemplo de Retorno Negativo: </b>
```json

{
	"detail": "As credenciais de autenticação não foram fornecidas."
}

```

```json
{
	"descricao": [
		"Este campo é obrigatório."
	],
	"valor": [
		"Este campo é obrigatório."
	],
	"data": [
		"Este campo é obrigatório."
	]
}
```

<h2>Resumo [GET]</h2>
<p>Resumo do Saldo Total com Receita por Mês, Despesa por Mês, Despesas de Categoria por Mês, e Saldo Final</p>
<ul><b>Basic Auth</b>
  <li>username</li>
  <li>password</li>
</ul>  
<ul>
  <li>/resumo/{ano}/{mês} [GET]</li>
</ul>
<b> Exemplo de Retorno Positivo:</b>

  ```json
{
	"Receita/Mês": "Somatória das Receitas por Mês",
	"Despesa/Mês": "Somatória das Despesas por Mês",
	"Categoria/Mês": [
		{
			"categoria": "Nome da Categoria",
			"valor": "Somatória da Categoria por Mês"
		}
	],
	"Saldo Final/Mês": "Subtração de Receitas por Mês com Despesas por Mês"
}
  ```
  
<b> Exemplo de Retorno Negativo: </b>
```json

{
	"detail": "As credenciais de autenticação não foram fornecidas."
}

```

<h1> Instalação </h1>
É necessária a Instalação mais recente do <a href="https://www.python.org/downloads/" target="_blank">Python</a>

<h2> Dependências</h2>

````sh
pip install -r requirements.txt
````

<h1> Configuração </h1>
<ol>
  <li> Crie um arquivo `.env` na mesma pasta onde está o arquivo `migrate.py`.</li>
  <li>No seu terminal com o ambiente virtual ativado, execute o comando `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'` para gerar uma chave secreta.</li>
  <li>Substitua a chave secreta no arquivo `.env` com a chave gerada na variável `SECRET_KEY`.</li>
  <li>Substitua o endereço do banco de dados no arquivo `.env` com o endereço do banco de dados que você deseja utilizar na variável `DATABASE_URL`.</li>
  <li>Execute o comando `python manage.py migrate` para criar as tabelas do banco de dados.</li>
</ol>

<h1>Rodando o projeto</h1>

```sh
python manage.py runserver
```

O servidor está rodando, visite http://127.0.0.1:8000/ no seu navegador de internet
