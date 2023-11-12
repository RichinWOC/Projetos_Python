import cv2
import imutils
import numpy as np
import os
aluno = 0
lista_nota_alunos = {}
arquivos = os.listdir(fr"C:\Users\richa\Desktop\Cursos\Curso-Pthon-HeitorLima\Curso-PythonHL\Gabaritos")
for imagem in arquivos:
    img1 = cv2.imread(fr"Gabaritos\{imagem}")
    img1 = cv2.resize(img1, (500, 600))
    img2 = cv2.imread(fr"GabaritoO.jpg")
    img2 = cv2.resize(img2, (500, 600))

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(gray1, gray2)

    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # cv2.imshow("Threshold", thresh)

    kernel = np.ones((5, 5), np.uint8)
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    contours = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    erros = 0

    for contour in contours:
        if cv2.contourArea(contour) > 100:
            erros += 1
    errosC = erros/2
    nota = 4-errosC
    aluno += 1
    lista_nota_alunos[f"aluno{aluno}"] = nota
    # cv2.imshow("Imagem Original", img1)
    # cv2.imshow("Editado", img2)
for aluno, nota in lista_nota_alunos.items():
    print(f"O {aluno} tirou nota {nota}")