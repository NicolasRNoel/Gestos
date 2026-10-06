# 🖐️ Control de Iluminación e Interrupciones en ESP32 mediante Reconocimiento de Gestos

Este proyecto implementa un sistema de control de iluminación e interrupciones dinámicas mediante visión artificial. Utiliza **MediaPipe Gesture Recognizer** y **OpenCV** en Python para interpretar gestos manuales en tiempo real y traducirlos en comandos seriales dirigidos a un microcontrolador **ESP32**[cite: 2].

Integrantes: Nicolas Robayo ; Jordan Alejandro Rodriguez ; Camilo Molano.
---

## 📐 Descripción General del Proyecto

El sistema captura el flujo de video desde la cámara web y procesa los fotogramas extrayendo los 21 puntos de referencia (*landmarks*) de la mano con MediaPipe[cite: 2]. Al detectar una postura específica, el script asocia el gesto a un comando caracter de control (`A`, `B`, `C`, `D`, `E`) diseñado para modificar la intensidad PWM de diodos LED o disparar secuencias por interrupción en el ESP32[cite: 2].

---

## 📋 Mapeo de Gestos y Funciones

| Gesto Detectado | Comando Serial | Acción en ESP32 / Salida |
| :--- | :---: | :--- |
|  (Puño Cerrado) | `A` | **30% de Intensidad** (LED Amarillo)[cite: 2] |
|  (Signo de Victoria / V) | `B` | **70% de Intensidad** (LED Azul)[cite: 2] |
|  (Palma Abierta) | `C` | **100% de Intensidad** (LED Rojo)[cite: 2] |
|  (Pulgar Abajo) | `D` | **Primera Interrupción:** Secuencia de luces (Modo 1)[cite: 2] |
|  (Pulgar Arriba) | `E` | **Segunda Interrupción:** Secuencia de luces (Modo 2)[cite: 2] |

---

## 🛠️ Tecnologías y Componentes

### Software
* **Python 3.x**
* **OpenCV (`cv2`):** Captura de video, procesamiento de fotogramas y despliegue gráfico.
* **MediaPipe Tasks (`mediapipe`):** Detección de la malla de la mano (21 puntos de referencia) y clasificación del gesto usando `gesture_recognizer.task`[cite: 2].
* **PySerial:** Transmisión de comandos desde Python hacia el puerto serie del ESP32.

### Hardware
* **Microcontrolador ESP32**[cite: 2].
* **Cámara Web** (USB o integrada).
* **LEDs:** Amarillo, Azul y Rojo[cite: 2].
* Resistencias de protección y cableado en protoboard[cite: 2].

---

## ⚙️ Estructura del Código Principal (`main.py`)

El script `main.py` realiza las siguientes operaciones:

1. **Carga del Modelo:** Inicializa el reconocedor de gestos cargando el archivo ejecutable `gesture_recognizer.task`.
2. **Captura de Video:** Abre el puerto de la cámara (`cv2.VideoCapture(0)`).
3. **Conversión de Formato:** Transforma los fotogramas de BGR a RGB para la compatibilidad con `mp.Image`.
4. **Mapeo y Salida:** Extrae el gesto con mayor nivel de confianza, lo mapea mediante el diccionario `gesture_map` e imprime el comando a enviar[cite: 2].
5. **Interfaz Gráfica:** Superpone el texto del gesto y comando detectado en la ventana de visualización.

