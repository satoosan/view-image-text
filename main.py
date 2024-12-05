from PIL import Image
import pytesseract
import cv2

# Caminho para a imagem enviada pelo usuário
image_path = 'teste.png'

# Carregar a imagem usando OpenCV
img = cv2.imread(image_path)

# Conversão para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Aplicar CLAHE (Equalização Adaptativa)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
enhanced = clahe.apply(gray)

# Ampliar a imagem para melhorar OCR
scale_percent = 200  # Aumentar 200%
width = int(enhanced.shape[1] * scale_percent / 100)
height = int(enhanced.shape[0] * scale_percent / 100)
dim = (width, height)
resized = cv2.resize(enhanced, dim, interpolation=cv2.INTER_CUBIC)

# Aplicar um leve desfoque (apenas para suavizar ruídos)
blurred = cv2.GaussianBlur(resized, (3, 3), 0)

# Salvar a imagem pré-processada temporariamente
preprocessed_image_path = 'preprocessed_image.png'
cv2.imwrite(preprocessed_image_path, blurred)

# Abrir a imagem pré-processada com PIL
img_pil = Image.open(preprocessed_image_path)

# Usar OCR para extrair texto da imagem
extracted_text = pytesseract.image_to_string(img_pil, lang='por')

# Nome do arquivo onde o texto será salvo
output_file = 'texto_extraido.txt'

# Criar e salvar o texto extraído no arquivo
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(extracted_text)

print(f"Texto extraído foi salvo no arquivo: {output_file}")
