# OCR com OpenCV e Tesseract

Este projeto utiliza o Tesseract OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens, com pré-processamento feito usando OpenCV para melhorar a precisão do OCR. O código lê uma imagem, aplica alguns métodos de pré-processamento para otimizar a qualidade da imagem, e extrai o texto da imagem, salvando-o em um arquivo `.txt`.

## Tecnologias e Bibliotecas Utilizadas

- **Python 3.x**
- **Pillow** (`PIL`) - Para trabalhar com imagens.
- **OpenCV** (`cv2`) - Para aplicar técnicas de pré-processamento na imagem.
- **Tesseract OCR** - Para realizar o reconhecimento de texto na imagem.
- **Pytesseract** - Interface do Python para o Tesseract OCR.

## Como Funciona

O script segue os seguintes passos:

1. **Carregamento da Imagem**: A imagem é carregada usando o OpenCV.
2. **Pré-processamento da Imagem**:
    - A imagem é convertida para escala de cinza.
    - O método CLAHE (Equalização Adaptativa de Histograma Local) é aplicado para melhorar o contraste da imagem.
    - A imagem é redimensionada para ampliar os detalhes, facilitando o processo de OCR.
    - Um desfoque Gaussiano é aplicado para suavizar ruídos e melhorar a clareza da imagem.
3. **Extração de Texto**: O Tesseract OCR é utilizado para extrair o texto da imagem pré-processada.
4. **Salvamento do Texto**: O texto extraído é salvo em um arquivo `.txt`.

## Instalação

Antes de rodar o código, você precisa instalar as bibliotecas necessárias. Você pode usar `pip` para instalá-las.

### 1. Instalar as Bibliotecas

```bash
pip install pytesseract
pip install opencv-python
pip install pillow
```

### 2. Instalar o Tesseract OCR

O **Tesseract OCR** precisa ser instalado separadamente. Siga as instruções de instalação abaixo, de acordo com o seu sistema operacional.

#### Para Windows:
- Baixe o instalador do Tesseract [aqui](https://github.com/UB-Mannheim/tesseract/wiki).
- Após a instalação, adicione o caminho do Tesseract à variável de ambiente do sistema. O caminho normalmente será algo como:
  ```
  C:\Program Files\Tesseract-OCR\tesseract.exe
  ```

#### Para Linux:
- Use o seguinte comando para instalar o Tesseract:
  ```bash
  sudo apt-get install tesseract-ocr
  ```

#### Para macOS:
- Instale o Tesseract usando o Homebrew:
  ```bash
  brew install tesseract
  ```

### 3. Configuração do Tesseract no Python

No seu código Python, você precisará configurar o caminho para o executável do Tesseract, se ele não estiver no caminho padrão. Adicione a seguinte linha ao início do código:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows
# ou para Linux/macOS:
# pytesseract.pytesseract.tesseract_cmd = "/usr/local/bin/tesseract"
```

## Uso

1. Coloque sua imagem no mesmo diretório do script, ou altere o caminho da imagem no código.
2. Execute o script Python:

```bash
python seu_script.py
```

O código irá processar a imagem e salvar o texto extraído em um arquivo `.txt` chamado `texto_extraido.txt`.

## Exemplo de Saída

O texto extraído da imagem será salvo em um arquivo de texto chamado `texto_extraido.txt`.

**Nota**: O desempenho do OCR pode variar dependendo da qualidade da imagem. O pré-processamento é feito para melhorar a precisão, mas imagens de baixa qualidade podem ainda assim produzir resultados imprecisos.

## 