import os
from PIL import Image


def getSortedFiles(dirPath: str):
    lst = [[i.zfill(7), i] for i in os.listdir(dirPath)
           if (i.endswith(".jpg") or i.endswith(".jpeg") or i.endswith(".png"))]
    lst.sort()
    return [val for (sor, val) in lst]


def dir2pdf(dirPath: str, outDir: str):
    image_list = []
    fullPath = "{}/{}".format(rootDir, dirPath)
    for imgName in getSortedFiles(fullPath):
        image_list.append(Image.open(
            '{}/{}'.format(fullPath, imgName)).convert('RGB'))
    im1 = image_list[0]
    image_list.pop(0)
    im1.save(r'{}/{}.pdf'.format(outDir, dirPath),
             save_all=True, append_images=image_list)


def getDirNames(rootDir):
    dirNames = []
    for root, dirnames, filenames in os.walk(rootDir):
        dirNames = dirnames
        break
    dirNames = [[i.zfill(4), i] for i in dirNames]
    dirNames.sort()
    dirNames = [val for (sor, val) in dirNames]
    return dirNames


currentDirs = getDirNames(".")
for i in range(len(currentDirs)):
    print(i, " - ", currentDirs[i])
rootDir = currentDirs[int(input("Enter dir No. : "))]

os.mkdir("{}/Output".format(rootDir))
outDir = "{}/Output".format(rootDir)

for dirPath in getDirNames(rootDir):
    print("-- Start : {}".format(dirPath))
    dir2pdf(dirPath, outDir)
