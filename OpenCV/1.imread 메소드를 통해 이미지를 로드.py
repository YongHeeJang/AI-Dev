# imread() 메소드를 통해 이미지를 로드

import cv2
import numpy as np

img_path = "./cat.jpg"
img = cv2.imread(img_path)

# image type & size 확인

print("이미지 타입 : ", type(img))
print("이미지 크기 : ", img.shape)

h, w, _ = img.shape
print(f"이미지 높이 {h}, 이미지 넓이 {w}")


cv2.imshow("image show", img)
cv2.waitKey(0)
