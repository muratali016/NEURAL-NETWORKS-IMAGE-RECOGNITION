import cv2
import face_recognition
from playsound import playsound
from gtts import gTTS
import os
import random
import tkinter as tk

import tkinter as tk



def face():
    def speak(string):
        tts=gTTS(string )
        rand =random.randint(1,10000)
        file='audio-'+str (rand)+'.mp3'
        tts.save(file)
        playsound(file)
        os.remove(file)

    camera = cv2.VideoCapture(0)
    return_value,image = camera.read()
    cv2.imwrite('yuz_fotografi.jpg',image)
    camera.release()
    cv2.destroyAllWindows()

    murat=face_recognition.load_image_file("murat.jpg")

    murat_yuzkodları=face_recognition.face_encodings(murat)[0]

    bilinenyuzler=[
        murat_yuzkodları
    ]

    gelenyuz=face_recognition.load_image_file("yuz_fotografi.jpg")

    gelenyuz_kodları=face_recognition.face_encodings(gelenyuz)

    print(gelenyuz_kodları)
    if gelenyuz_kodları==[]:
        speak("found no face")

    for yeniyuz in gelenyuz_kodları :
        sonuclar=face_recognition.compare_faces(murat_yuzkodları,gelenyuz_kodları)
        name=""
        if sonuclar[0]:
            name = "Murat"
            speak(f" welcome {name} !")
        else :
            print("unknowned person")


def çıkış():
    etiket['text'] = 'EXITING'

    face()
    pencere.after(2000, pencere.destroy)

pencere = tk.Tk()
pencere.geometry("250x250+10+10");






etiket = tk.Label(text='PRESS THE FACE RECOGNITION')
etiket.pack()

düğme = tk.Button(text='Face_recogniton', command=çıkış)
düğme.pack()

pencere.protocol('WM_DELETE_WINDOW', çıkış)

pencere.mainloop()
