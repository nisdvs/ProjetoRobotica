import cv2
import tkinter as tk
from PIL import Image, ImageTk
import pandas as pd

def compare_images(frame, reference_image):
    # Inicializa o detector SURF
    surf = cv2.SURF_create()

    # Detecta e calcula descritores de características para o frame e a imagem de referência
    kp1, des1 = surf.detectAndCompute(frame, None)
    kp2, des2 = surf.detectAndCompute(reference_image, None)

    # Inicializa o objeto correspondência de características
    bf = cv2.BFMatcher()

    # Realiza a correspondência de características entre os descritores de características do frame e da imagem de referência
    matches = bf.knnMatch(des1, des2, k=2)

    # Aplica o teste de razão de Lowe para obter as correspondências válidas
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # Retorna True se houver um número suficiente de correspondências válidas, senão False
    return len(good_matches) > 10  # Ajuste este valor conforme necessário


def load_csv_data(csv_file):
    images = []
    with open(csv_file, 'r') as f:
        for line in f:
            image_path = line.strip().strip('"')  # Remover aspas duplas extras
            image = Image.open(image_path)
            image_data = np.array(image)
            images.append(image_data)  # Mensagem de erro
    return images


Lista_images = load_csv_data('imagens.csv')
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)

        # Comparar a imagem capturada com as imagens de maçãs
        found_images = False
        for image in Lista_images:
            similarity = compare_images(frame, image)
            if similarity:
                found_images = True
                break

        print(found_images)

    label.after(10, update_frame)

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Webcam")

label = tk.Label(root)
label.pack()

update_frame()

root.mainloop()

cap.release()
