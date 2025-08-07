# Template Djano API

Esse projeto foi desenvolvido utilizando _Django_ _Python_.pytho

1. Criar pasta para nova aplicação
$ mkdir new_app

2. Setar na nova pasta
$ cd new_app

3. Copiar todo conteúdo da template-django-api para o diretório da nova aplicação
$ cp -r /home/marcus/app/template-django-api/* .
não levou o .gitignore

3. DockerFile
Adiconar a instalção de pacotes necessário a partir da linha 14

5. compose.yaml
substituir a expressão [NEW_APP] pelo nome da nova aplicação
substituir a expressão [NETWORK_NAME] pelo nome da rede

6. install.sh
substituir a expressão [NEW_APP] pelo nome da nova aplicação
executar install.sh = ./install.sh

7. Executar o docker compose
$ docker compose up -d

8. config.sh
substituir a expressão [NEW_APP] pelo nome da nova aplicação
substituir a expressão [NEW_USER] pelo nome do usuário linux
executar o config.sh = ./config.sh

  XX) Criar rotas
  o arquivo install.sh já contém os arquivos default com a primeira rota configurada

  XX) removar pasta temp
  $ rm -rf temp 
 
  XX) Atribuir acesso ao usuário
  Já está no arquivo install.sh == sudo chown marcus:marcus src -R

  XX) Rodar migrations dentro do container
  docker exec -it [NEW-APP] python3 manage.py makemigrations
  docker exec -it [NEW-APP] python3 manage.py migrate

9. Abrir o navegador
  - http://localhost:8080
  Se tudo correu bem vai abrir a página default do Django
  The install worked successfully! Congratulations!

  - http://localhost:8080/api/v1

  - http://localhost:8080/api/v1/projects

10. se o comando acima não funcionar 
$ docker restart [NEW-APP]





11) Abrir o navegador: 
  http://localhost:8080/api/v1
  

12)  Abrir o navegador: http://localhost:8080/api/v1/projects
  OperationalError at /api/v1/projects
  no such table: api_project

13) Rodar migrations
  src$ python3 manage.py makemigrations
  src$ python3 manage.py migrate




Abrir o navegador: http://localhost:8080/api/v1/projects , 
agora deve aparecer na tela Project List
  



XX) Configurar gitignore: copiar do ifc-step-parser


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

- Acesse o repositório: [ifc-otimrota-translator-api](https://bitbucket.org/certi_repos/ifc-otimrota-translator-api/src/master/)

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

#### 4.0 - Instalação de Dependências a partir de um PyPI Server

- A aplicação precisa da instalação de 2 pacotes que estão armazenados no PyPI Server

```
$ pip install --index-url http://34.234.184.104:8070/simple/ ifc_otimrota_translator --trusted-host 34.234.184.104
```
```
$ pip install --index-url http://34.234.184.104:8070/simple/ ifc_step_parser --trusted-host 34.234.184.104
```

#### 5.0 - Execute a aplicação

- Após instalar as dependências, navega paara a pasra src e cole o seguinte comando no terminal:

  ```
  /src$ uvicorn app:app --reload
  ```

- A API estará rodando na sua completude quando você visualizar no terminal as informações abaixo:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

INFO:     Started reloader process [19099] using StatReload

INFO:     Started server process [19101]

INFO:     Waiting for application startup.

INFO:     Application startup complete.

Após iniciada a API, esta poderá ser consumida através da porta **8000**. [http://localhost:8000/](http://localhost:8000/)

---

Para criar rota padrão, já configura substituir os arquivos abaixo, pelos correspondentes na pasta temp
-- src/app/url.py
$ mv temp/src/app/urls.py src/app/urls.py
-- criar arquivo src/api/urls.py
mv temp/src/api/urls.py src/api
-- src/api/views.py
mv temp/src/api/views.py src/api/views.py
-- src/api/models.py
mv temp/src/api/models.py src/api/models.py
-- criar arquivo src/api/serializers.py
mv temp/src/api/serializers.py src/api
-- src/app/settings.py
mv temp/src/app/settings.py src/app/settings.py