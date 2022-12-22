# 기본적인 이미지 처리 기술을 이용한 이미지 선명화

# 이미지 읽기 블러 처리
# 출력 이미지가 흐릿할 경우, 이미지를 선명하게 하기 위해서,이미지를 매끄럽게 만들어서 노이즈를 제거한다.


import cv2
import numpy as np

img = cv2.imread('./car.jpg', 0)
print(img.shape)
img_rsize = cv2.resize(img, (320, 240))

blurred_1 = np.hstack([
    cv2.blur(img_rsize, (3, 3)),
    cv2.blur(img_rsize, (5, 5)),
    cv2.blur(img_rsize, (9, 9))
])

cv2.imshow("show", blurred_1)
cv2.waitKey(0)
