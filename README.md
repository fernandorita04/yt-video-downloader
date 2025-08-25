# Downloader de Vídeos do YouTube utilizando Python

Aplicação em **Python** para baixar vídeos do YouTube em alta qualidade, com interface gráfica simples utilizando **Tkinter**.  
O sistema baixa o vídeo e o áudio separadamente na melhor qualidade disponível e depois une os dois em um único arquivo com o **FFmpeg**.

---

## Funcionalidades
- Baixar vídeos do YouTube em alta qualidade.
- Download de vídeo e áudio separados para garantir máxima qualidade.
- Mesclagem automática via **FFmpeg**.
- Interface gráfica amigável feita em **Tkinter**.
- Escolha do diretório de destino para salvar os vídeos.
- Remoção automática de arquivos temporários após a mesclagem.

---

## Tecnologias Utilizadas
- [Python 3.10+](https://www.python.org/)  
- [pytubefix](https://pypi.org/project/pytubefix/)  
- [FFmpeg](https://ffmpeg.org/download.html)  
- [Tkinter](https://docs.python.org/3/library/tkinter.html)  

---

## Instalação
Clone o repositório:
```bash
git clone https://github.com/fernandorita04/yt-video-downloader.git
cd yt-video-downloader
```
Crie e ative um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
Instale as dependências:
```bash
pip install pytubefix
```
Certifique-se de que o FFmpeg está instalado e configurado no PATH do seu sistema:
```bash
ffmpeg -version
```
Caso o FFmpeg não esteja instalado, siga os seguintes passos:
### Windows
1. Acesse o site oficial: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)  
2. Baixe a versão **release full** (arquivo `.zip`).  
3. Extraia o conteúdo para um diretório, por exemplo:  
C:\ffmpeg

Dentro dessa pasta haverá uma subpasta `bin` com o arquivo `ffmpeg.exe`.

4. Adicione o FFmpeg ao **PATH do sistema**:
- Pressione `Win + R`, digite `sysdm.cpl` e pressione Enter.
- Vá até **Avançado → Variáveis de Ambiente**.
- Localize a variável **Path**, edite e adicione:
  ```
  C:\ffmpeg\bin
  ```
- Salve e reinicie o terminal.

5. Teste no Prompt de Comando:
```bash
ffmpeg -version
```
### Ubuntu/Debian
No terminal, execute:
```bash
sudo apt update
sudo apt install ffmpeg -y
```
Verifique a instalação:
```bash
ffmpeg -version
```

## Como usar
Execute o programa:
```bash
python script_download_youtube.py
```
1. Cole a URL do vídeo do YouTube.
2. Escolha a pasta de destino.
3. Clique em "Baixar".
4. Aguarde o download e a mesclagem automática.
5. O vídeo estará disponível na pasta escolhida.
