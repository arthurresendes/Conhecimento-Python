import cv2
import os

# 1. Configurar o diretório de saída
pasta_destino = "imagens"
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# 2. Inicializar a câmera (0 é o padrão)
cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Erro: Não foi possível abrir a câmera.")
    exit()

print("Pressione ENTER para salvar a foto ou 'q' para sair.")

while True:
    # Capturar frame por frame
    ret, frame = cam.read()
    
    if not ret:
        print("Erro: Não foi possível capturar o frame.")
        break

    # Exibir o vídeo em tempo real
    cv2.imshow("Câmera", frame)

    # 3. Aguardar comandos do teclado
    key = cv2.waitKey(1)
    
    # Se pressionar 'ENTER', salva a foto
    if key == 13:
        nome_foto = os.path.join(pasta_destino, "foto.jpg")
        cv2.imwrite(nome_foto, frame)
        print(f"Foto salva em: {nome_foto}")
        break
        
    # ESC
    elif key == 27:
        break

# 4. Liberar a câmera e fechar janelas
cam.release()
cv2.destroyAllWindows()
