import cv2

cap = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\OpenCV dersleri\\videos\\video.mp4")
# webcam'den görüntü almak için 0 yazıyoruz.
# mesela bir video çalıştırmak isteseydik 0 yerine o videonun yolunu yazardık.
# örnek: cap = cv2.VideoCapture("C:\\Users\\Administrator\\Desktop\\OpenCV dersleri\\videos\\video.mp4")

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 0)
    # çıkan çıktı ters gözükür normalde. onun için cv2.flip kullanıyoruz.

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # burda ise frame'i yani cap'te okunan görüntü frame olduğu için frame'yi işledik mesela gri yaptık.

    cv2.imshow("webcam", gray_frame)
    cv2.imshow("webcam", hsv_frame)



    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
# video ile işim bitti, serbest bırak demek istiyorum burda.
cv2.destroyAllWindows()




