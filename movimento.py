import cv2
import time
from playsound import playsound
import os


webcam = cv2.VideoCapture(0)

webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

frame_referencia = None

ultimo_disparo = 0
intervalo_alarme = 3

detectou_movimento = False

print ("iniciando")

while True:
    sucesso, frame = webcam.read()
    
    if not sucesso:
        break


    #deixa a imagem cinza
    frame_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #deixa a imagem blur
    frame_cinza = cv2.GaussianBlur(frame_cinza, (21, 21),0)

    if frame_referencia is None:
        frame_referencia = frame_cinza
        continue

    diferenca = cv2.absdiff(frame_referencia, frame_cinza)

    _, delta_thresh = cv2.threshold(diferenca, 30, 255, cv2.THRESH_BINARY)

    delta_thresh = cv2.dilate(delta_thresh , None, iterations=2)


    contornos, _ = cv2.findContours(delta_thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    for contorno in contornos:
        if cv2.contourArea(contorno) < 1000:
            continue

        (x, y, w ,h) = cv2.boundingRect(contorno)

        cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),2)
        #print("alarme")
        #print(x, y, w, h)
        detectou_movimento = True

    cv2.imshow("movimento", frame)


    if detectou_movimento:
        agora = time.time()
        if agora - ultimo_disparo > intervalo_alarme:
            try:
                playsound('som.mp3', block= False)
            except:
                print("erro",agora)
                os.system('spd-say "I see you" &')
            ultimo_disparo = agora
            
    #cv2.imshow("diferença", delta_thresh)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows