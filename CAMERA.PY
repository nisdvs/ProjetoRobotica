import cv2
import tkinter as tk
from PIL import Image, ImageTk

# Função para capturar frames da webcam e exibir usando Tkinter
def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.config(image=imgtk)
    label.after(10, update_frame)

cap = cv2.VideoCapture(1)

root = tk.Tk()
root.title("Webcam")

label = tk.Label(root)
label.pack()

update_frame()

root.mainloop()

cap.release()
