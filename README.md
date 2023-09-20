# Como rodar a imagem docker

Com o docker instalado na sua maquina, entre no diretorio raiz do projeto e execute:

```bash

docker build -t ifbucks/backend .
```

Aguarde o build da imagem docker.

Agora rode a imagem docker com o seguinte comando:

```bash

docker run -p 8000:8000 ifbucks/backend
```

Agora se voce acessar http://localhost:8000 seu backend está rodando,
