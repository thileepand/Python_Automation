import pytest
import  cv2
from scipy import ndimage


#@pytest.mark.run(order=1)
img = cv2.imread('/home/thileepan/Downloads/valid Images/204106_461_400_0_20170711.jpg')

imgR = ndimage.rotate(img, 90, reshape=True)
imgR1 = ndimage.rotate(img, 180, reshape=True)
imgR2 = ndimage.rotate(img, 270, reshape=True)

cv2.imwrite('/home/thileepan/Downloads/img/204106_461_400_0_20170711.jpg',img)
cv2.imwrite('/home/thileepan/Downloads/img/204106_461_400_0_20170711_r1.jpg',imgR)
cv2.imwrite('/home/thileepan/Downloads/img/204106_461_400_0_20170711_r2.jpg',imgR1)
cv2.imwrite('/home/thileepan/Downloads/img/204106_461_400_0_20170711_r3.jpg',imgR2)
