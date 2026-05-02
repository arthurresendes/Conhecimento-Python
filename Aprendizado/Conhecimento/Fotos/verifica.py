import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # Remove avisos inúteis do terminal
import cv2
from deepface import DeepFace

PASTA_IMAGENS = "imagens"
MODELO = "VGG-Face"

def verificar_acesso(frame_camera):
    frame_pequeno = cv2.resize(frame_camera, (0, 0), fx=0.5, fy=0.5)
    
    arquivos = [f for f in os.listdir(PASTA_IMAGENS) if f.endswith(('.jpg', '.png', '.jpeg'))]
    for arquivo in arquivos:
        caminho_foto = os.path.join(PASTA_IMAGENS, arquivo)
        try:
            resultado = DeepFace.verify(img1_path = frame_pequeno, 
                                       img2_path = caminho_foto, 
                                       model_name = MODELO,
                                       enforce_detection = False)
            if resultado["verified"]:
                return True, arquivo
        except:
            continue
    return False, None

cap = cv2.VideoCapture(0)
status_texto = "INICIANDO..."
cor_status = (255, 255, 255)
contador_frames = 0

while True:
    ret, frame = cap.read()
    if not ret: break

    if contador_frames % 30 == 0:
        autorizado, nome_arquivo = verificar_acesso(frame)
        if autorizado:
            status_texto = f"ACESSO LIBERADO"
            cor_status = (0, 255, 0)
        else:
            status_texto = "ACESSO NEGADO"
            cor_status = (0, 0, 255)

    contador_frames += 1

    cv2.putText(frame, status_texto, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, cor_status, 2)
    cv2.imshow("Acesso Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
