# DavMerger 0.1.0

DavMerger foi criado com o objetivo de facilitar a concatenação de vídeos gravados por sistemas de vigilância de circuito fechado em formato `.DAV` (ou outros). Após sua execução é gerada a concatenação de todos os vídeos em um único vídeo `.MP4`, permitindo aceleração do vídeo em quantas vezes for necessário.

### Como Instalar

É necessário ter o [Python](https://www.python.org/downloads/) na versão 3.11+
```py
python ^= 3.11
```

Realize o clone do repositório e acesse o diretório da aplicação
```
git clone https://github.com/edvitor13/davmerger
```
```
cd davmerger
```

No diretório clonado do projeto instale via PIP o arquivo de `requirements.txt`
```py
python -m pip install -r requirements.txt
```

Ou caso tenha [Poetry](https://python-poetry.org/docs/)
```py
poetry install
```

### Dependências

O DavMerger necessita que o `FFMPEG` esteja instalado em sua máquina.

FFmpeg é um software livre e de código aberto usado para converter e manipular arquivos de áudio e vídeo via linha de comando.

Link de Download: https://ffmpeg.org/download.html

Como instalar no `Windows`: https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows
Como instalar no `Linux`: https://www.hostinger.com.br/tutoriais/como-instalar-ffmpeg
Como instalar no `MacOS`: https://www.youtube.com/watch?v=8nbuqYw2OCw

Para verificar se realmente está instalado envie o seguinte comando no terminal:

```python
ffmpeg -version
```

### Como utilizar

1. Com tudo devidamente instalado, no diretório da aplicação envie o comando:

    ```py
    python main.py
    ```

2. Será aberta uma janela solicitando que você selecione quais vídeos deseja gerar um arquivo único `.MP4`

    ![Selecione as gravações](https://media.discordapp.net/attachments/962716686870511689/1084649816535076875/tutorial_1.png?width=692&height=545)
    
3. Após escolher os vídeos, será solicitado que você escolha o local e o nome do vídeo que será salvo

    ![Salvar arquivo como](https://media.discordapp.net/attachments/962716686870511689/1084651107923529748/image.png)
    
4. Será aberta uma janela, caso você queira ajustar as configurações default do vídeo que será salvo ou se deseja cancelar

    ![Editar configurações do vídeo](https://media.discordapp.net/attachments/962716686870511689/1084651610090770482/image.png)
    
5. Ao clicar em `Iniciar` a janela será fechada e no terminal da aplicação será exibida a renderização que está sendo realizada via `FFMpeg`
    
    ![Salvando vídeo](https://media.discordapp.net/attachments/962716686870511689/1084652085338984448/image.png?width=914&height=495)
