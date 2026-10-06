import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

# Configuración del reconocedor de gestos
base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)

# Diccionario para mapear los gestos a los comandos seriales
gesture_map = {
    "Closed_Fist": "A", # 30% Amarillo
    "Victory": "B",     # 70% Azul
    "Open_Palm": "C",   # 100% Rojo
    "Thumb_Down": "D",  # Secuencia 1
    "Thumb_Up": "E"     # Secuencia 2
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Convertir la imagen a formato MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    
    # Reconocer gestos
    recognition_result = recognizer.recognize(mp_image)
    
    if recognition_result.gestures:
        top_gesture = recognition_result.gestures[0][0].category_name
        comando = gesture_map.get(top_gesture, None)
        
        if comando:
            # Aquí iría el envío por Serial (ej. serial_port.write(comando.encode()))
            print(f"Gesto: {top_gesture} -> Comando enviado: {comando}")
            
            # Mostrar en pantalla para el video
            cv2.putText(frame, f"Gesto: {top_gesture}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.putText(frame, f"Comando: {comando}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Reconocimiento de Gestos', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()