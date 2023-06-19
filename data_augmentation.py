import os 
import cv2

dir_list = os.listdir("train")
# print(dir_list)
count = 351
for j in dir_list:
    img = cv2.imread(f"train/{j}")
    # cv2.imshow("window", img)
    # cv2.waitKey(0)
    rotate_90_clk = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    rotate_180 = cv2.rotate(img, cv2.ROTATE_180)
    rotate_90_anticlk = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imwrite(f"train/train_img_{count}.jpg", rotate_90_clk)
    count = count + 1
    cv2.imwrite(f"train/train_img_{count}.jpg", rotate_180)
    count = count + 1
    cv2.imwrite(f"train/train_img_{count}.jpg", rotate_90_anticlk)
    count = count + 1
    print("Done!!!")


# img = cv2.imread("train/train_img_1.jpg")
# cv2.imshow("window", img)
# cv2.waitKey(0)
# update_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.imwrite("update_imgae.jpg", update_90)