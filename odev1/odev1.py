import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü oku
image = cv2.imread('ana.jpg', cv2.IMREAD_GRAYSCALE)

# Görüntünün başarıyla okunup okunmadığını kontrol et
if image is None:
    print("Görüntü okunamadı. Lütfen dosya yolunu kontrol edin.")
else:
    # Histogram için boş bir dizi oluştur
    histogram = np.zeros(256)

    # Görüntü boyutlarını al
    height, width = image.shape[:2]  # shape'ın ilk iki elemanı yükseklik ve genişliktir

    # Histogram hesapla
    for v in range(height):
        for u in range(width):
            intensity = image[v, u]
            histogram[intensity] += 1

    # Histogramı görselleştir (isteğe bağlı)
    plt.bar(range(256), histogram, color='gray')
    plt.title('Gri Seviye Histogramı')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Frekans')
    plt.show()
