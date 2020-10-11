import glob
import os
import shutil

import cv2


def func():
    path_list = glob.glob(os.path.join('assets', '*.*'))
    # path_list = sorted(path_list)

    path_dir = 'sorted'

    path_save = os.path.join(path_dir, 'misc')
    os.makedirs(path_save, exist_ok=True)

    for i in range(len(path_list)):
        # for i in range(1000):
        path = path_list[i]
        try:
            img = cv2.imread(path)
            # if img.shape == (224, 134, 3) or img.shape == (224, 202, 3) or img.shape == (224, 202, 3):
            if img.shape[0] == 224:
                imtype = 'SD_Standing'
            elif img.shape == (54, 54, 3):
                imtype = 'SD_Head'
            elif img.shape == (464, 250, 3):
                imtype = 'Standing'
            elif img.shape == (640, 1136, 3):
                imtype = 'Illust'
            elif img.shape == (96, 96, 3):
                imtype = 'Icon_Card'
            elif img.shape == (148, 148, 3):
                imtype = 'Icon_Clothes'
            elif img.shape == (50, 50, 3):
                imtype = 'Icon_Character'
            elif img.shape == (44, 44, 3):
                imtype = 'Icon_Small'
            elif img.shape == (86, 212, 3):
                imtype = 'Banner'
            elif img.shape == (164, 186, 3):
                imtype = 'Img_Head'
            elif img.shape == (304, 426, 3):
                imtype = 'Sign'
            elif img.shape == (1024, 1024, 3):
                imtype = 'Parts'
            elif img.shape == (198, 444, 3):
                imtype = 'CardName'
            else:
                imtype = 'img_misc'
            # if imtype == 'img_misc':
            #     print(i, img.shape, path)
            #     cv2.imshow(str(i), img)
            #     cv2.waitKey(0)
            #     cv2.destroyAllWindows()
            # pass

            path_save = os.path.join(path_dir, imtype)
            os.makedirs(path_save, exist_ok=True)
            shutil.copy2(path, os.path.join(path_dir, imtype, path.split('\\')[-1]))
            # os.replace(path, os.path.join(path_dir, imtype, path))

        except Exception as e:
            print(f'error occurred while handling file {path}')
            print(e)
            # os.replace(path, os.path.join(path_dir, 'misc', path))
            shutil.copy2(path, os.path.join(path_dir, 'misc', path.split('\\')[-1]))


if __name__ == '__main__':
    func()
