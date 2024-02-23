import cv2
from cv2 import imread as baca
from cv2 import imshow as tampil

gambar = baca('luffy.png',3)

tampil ('gambar luffy ', gambar)

k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
