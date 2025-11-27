import cv2

webcam = cv2.VideoCapture(0)
 
if not webcam.isOpened():
    print("Erro")
    exit()

print("Camera ligada")

while True:
    sucesso,frame = webcam.read()

    if not sucesso:
        print("erro de leitura")
        break

    cv2.imshow("minha camera", frame)

    if cv2.waitKey(1) == ord ('q'):
        break

webcam.release()
cv2.destroyAllWindows()