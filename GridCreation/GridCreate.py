import numpy as np
import cv2 as cv
x="count_"+input("Enter image number")+".jpg"
img = cv.imread(x, 0)
rows, cols = np.shape(img)
new = np.zeros((rows, cols), dtype=np.uint16)

img = img > 50
count = 0
list1 = np.array([0], dtype=np.uint16)
for i in range(rows):
    for j in range(cols):
        if img[i, j]:
            if img[i, j - 1]==0 and img[i - 1, j]==0 and img[i - 1, j - 1] == 0:
                count += 1
                new[i, j] = count
                list1 = np.append(list1, count)
            elif img[i, j - 1] == img[i - 1, j] and img[i, j - 1] != 0:
                if new[i, j - 1] != new[i - 1, j]:
                    low = min(list1[new[i, j - 1]], list1[new[i - 1, j]])
                    high = max(list1[new[i, j - 1]], list1[new[i - 1, j]])
                    for q in range(len(list1)):
                        if list1[q] == high:
                            list1[q] = low
                new[i, j] = new[i - 1, j]
            else:
                if img[i - 1, j]:
                    new[i, j] = new[i - 1, j]
                elif img[i, j - 1]:
                    new[i, j] = new[i, j - 1]
                elif img[i - 1, j - 1]:
                    new[i, j] = new[i - 1, j - 1]

for i in range(rows):
    for j in range(cols):
        new[i, j] = list1[new[i, j]]

highest = np.amax(list1)
compare_list = np.array(range(1, highest + 1))
found_list = np.intersect1d(list1, compare_list)
print("The number of objects are", len(found_list))
x=input("Press Enter to exit")
