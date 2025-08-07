# Baba AABB - Gera Cartões

Esse projeto foi desenvolvido utilizando _Django_ _Python_.
O objetivo da aplicação é gerar cartões de acesso individuais a partir de um arquivo (_.pdf)
que pode 30, 40 ou 50 cartões.
A aplicação gera cartões individuais de acord com os nomes da lista de presença (_.txt)

## Pré-requisitos

É necessário ter instalado na sua máquina:

- **Python**
  Você pode verificar a versão do Python com o seguinte comando:

```
$ python3 --version
```

- **pip**
  Você pode verificar a versão do pip com o seguinte comando:

```
$ pip --version
```

- **virtualenv**
  Você pode verificar a versão do virtualenv com o seguinte comando:

```
$ virtualenv --version
```

- **GIT**

- **VSCode**(ou a IDE de sua preferência)

## Como rodar localmente

#### 1.0 - Clone o projeto em seu sistema local

- Acesse o repositório: [baba-aabb](https://github.com/spvmarcus/baba-aabb/tree/main)

- Clique em **clone** no canto superior direito e copie o comando de clonagem.

- Abra o **terminal** no diretório onde deseja clonar o projeto e **cole** o comando.

#### 2.0 - Configuração do Ambiente Virtual

Recomenda-se o uso de um ambiente virtual para isolar as dependências da aplicação. Siga estas etapas para criar e ativar um ambiente virtual:

1. Abra o terminal ou prompt de comando.

2. Navegue até a pasta raiz da sua aplicação.

3. Execute o seguinte comando para criar um ambiente virtual:

```
$ python3 -m virtualenv .venv
```

4. Ative o ambiente virtual:

- No Windows:

```
.venv\Scripts\activate
```

- No macOS e Linux:

```
$ source .venv/bin/activate
```

#### 3.0 - Instale as dependências

- Após ativar o ambiente virtual, você pode instalar as dependências do arquivo requirements.txt usando o seguinte comando:

```
$ pip install -r requirements.txt
```

#### 4.0 - Execute a aplicação

- Após instalar as dependências, navega paara a pasra src e cole o seguinte comando no terminal:

  ```
  /src$ python3 manage.py runserver
  ```

- A API estará rodando na sua completude quando você visualizar no terminal as informações abaixo:

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 4.2.3, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Após iniciada a API, esta poderá ser consumida através da porta **8000**. [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

#### 5.0 - Execute a aplicação via docker

```
/src$ docker compose up -d
```
