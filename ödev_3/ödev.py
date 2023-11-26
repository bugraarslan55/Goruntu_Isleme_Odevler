import cv2
import numpy as np

# Resmi yükleyin
image_path = "rice.jpg"
image = cv2.imread(image_path)

# Görüntüyü gri seviyeye dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Eşikleme uygula
_, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler uygula
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Bağlantı bileşenlerini etiketle
_, labels, stats, _ = cv2.connectedComponentsWithStats(opening, connectivity=8)

# Pirinç sayısını bul
rice_count = len(stats) - 1  # İlk etiket, arka planı temsil eder, bu yüzden çıkarılır

# Sonuçları ekrana yazdır
print("Pirinç Sayısı:", rice_count)

# Etiketli bileşenleri renklendir
result = cv2.cvtColor(opening, cv2.COLOR_GRAY2BGR)
for i in range(1, len(stats)):
    color = tuple(np.random.randint(0, 255, 3).tolist())
    cv2.putText(result, str(i), (stats[i][0], stats[i][1] - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    cv2.rectangle(result, (stats[i][0], stats[i][1]),
                  (stats[i][0] + stats[i][2], stats[i][1] + stats[i][3]), color, 2)

# Görüntüleri ekrana göster
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresh)
cv2.imshow('Morphological Operations', opening)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
