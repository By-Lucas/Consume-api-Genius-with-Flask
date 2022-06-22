# CONSUMIR API GENIUS COM PYTHON(FLASK)

## Instalar criar e ativar ambiente virtual
~~~ shell
pip install virtualenv
~~~
~~~ shell
python -m venv venv
~~~
~~~ shell
venv/scripts/activate
~~~

## Instalar Bibliotecas
~~~ shell
pip install -r requirements.txt
~~~

## Instalar Cache Redis no windows
**Instalar o executavel `Redis-x64-3.0.504.msi` que está dentro da pasta files e seguir com passo a passo abaixo.**
*Se utiliza outro sistema operacional, o link dos arquivos necessarios + informações: https://github.com/microsoftarchive/redis*

## Rodar aplicação e informações
**No arquivo `teste.env` voce deve alterar-lo para `.env` e colocar as dependências dentro.**
- `Criar Token no Genius e adcionar na parte GENIUS_TOKEN=`
- `Criar iD de segurança na AWS e adcionar no campo AWS_ACCESS_KEY_ID=`
- `pegar a  chave de acesso na AWS e adcionar no campo AWS_SECRET_ACCESS_KEY=`
- *O arquivo .env mantém as informações dentro de sí mais seguras, por isso recomendado usar alguns métodos como `(Decouple, os.getenv(), os.environ.get().`*

**Se tudo estiver OK, é só rodar o comando abaixo no terminal.**
~~~ shell
python -m run
~~~

## Consultar diretamente da api

**basta usar da forma mostrada abaixo.**

~~~ shell
http://127.0.0.1:5000/artista/Nome_do_artista
~~~

