# Consumindo API com Flask

Instale, crie e ative a virtualenv em sua máquina e instale as bibliotecas.

Para fazer a instalação use o comando: `pip install -r requirements.txt`

Existe um arquivo chamado exemple.env. Edite esse arquivo com suas credenciais AWS e Genius e renomei para apenas `.env`. Esse arquivo é o responsavel por deixar suas chaves de acesso seguras!

Para rodar a aplicação, use `python -m run`

## consulta get

Para fazer uma consulta buscando por nome do artista:

`http://127.0.0.1:5000/artista/Nome Artista`

