import cv2
import numpy as np

def find_red_object(frame):
    # Giriş görüntüsünü HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını belirle (düşük ve yüksek değerler)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Belirtilen renk aralığındaki nesneleri maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntüdeki sadece kırmızı nesneleri göster
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result

# Kamera bağlantısını aç
cap = cv2.VideoCapture(0)

while True:
    # Kameradan bir çerçeve al
    ret, frame = cap.read()

    # Kırmızı nesneleri tespit et
    result_frame = find_red_object(frame)

    # Görüntüleri ekranda göster
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Red Objects', result_frame)

    # Çıkış için 'q' tuşuna basılmasını kontrol et
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()
cv2.destroyAllWindows()
