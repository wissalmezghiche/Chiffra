import cv2
import os
import numpy as np
import math
from itertools import product

class TraitementImage:
    def Binarisation(self):
        raise NotImplementedError("Please Implement this method")
    def Normalisation(self):
        raise NotImplementedError("Please Implement this method")


class Dataset(TraitementImage):

    def __init__(self, path):
        self.path = path

    def Normalisation(self):
        resized_img = np.zeros((64, 64, 3))
        for image in os.listdir(self.path):
            dim = (64, 64)
            imgPath = os.path.join(self.path, image)
            img = cv2.imread(imgPath)
            img = cv2.GaussianBlur(img, (3, 3), 0)
            edge = cv2.Canny(img, 50, 200)
            contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
            for (i, c) in enumerate(sorted_contours):
                x, y, w, h = cv2.boundingRect(c)
                resized_img = img[y:y + h, x:x + w]
            resized_img = cv2.resize(resized_img, dim, interpolation=cv2.INTER_AREA)
            cv2.imwrite(imgPath, resized_img)

    def Binarisation(self):
        for image in os.listdir(self.path):
            imgPath = os.path.join(self.path, image)
            img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)  # grey image
            (thresh, bin_img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # binary image
            imgArray = np.array(bin_img)
            edge = cv2.Canny(bin_img, 50, 200)  # number's edges
            contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
            x = sorted_contours[0][0][0][0]
            y = sorted_contours[0][0][0][1]
            cv2.imwrite(imgPath, bin_img)  # save l'image
            if imgArray[0][0] == 0 and imgArray[63][63] == 0:  # we check a point of the img edge, if it's white so the bg is black
                bin_img = cv2.imread(imgPath)
                # make mask of white pixels / black pixels
                black = np.where((bin_img[:, :, 0] == 0) & (bin_img[:, :, 1] == 0) & (bin_img[:, :, 2] == 0))
                white = np.where((bin_img[:, :, 0] == 255) & (bin_img[:, :, 1] == 255) & (bin_img[:, :, 2] == 255))
                # Turn black pixels to white and vice versa
                bin_img[black] = (255, 255, 255)
                bin_img[white] = (0, 0, 0)
                cv2.imwrite(imgPath, bin_img)  # save image


class Image(TraitementImage):

    def __init__(self,path):
        self.path = path

    def Binarisation(self):
        img = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)  # grey image
        (thresh, bin_img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # binary image
        cv2.imwrite(self.path, bin_img)  # save the image

    def Normalisation(self, width, height):
        dim = (width, height)
        img = cv2.imread(self.path) # read image
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA) # resize image
        cv2.imwrite(self.path, resized_img) # save image

    def imgToMatrix(self):
        img = cv2.imread(self.path,mode='RGB')
        return img

    def img_moyen(self):
        matrix = self.imgToMatrix(self.path)
        dim = np.shape(matrix)
        w = dim[0]
        h = dim[1]
        nbpixels = w * h
        somme = 0
        for i in range(h):
            for j in range(w):
                pixel = ( (matrix[i][j][0] + matrix[i][j][1] + matrix[i][j][2])/3 ) #RGB format
                somme += pixel
        return (somme / nbpixels)

    def img_ecart(self):
        moyenne = self.img_moyen(self.path)
        matrix = self.imgToMatrix(self.path)
        dim = np.shape(matrix)
        w = dim[0]
        h = dim[1]
        nbpixels = w * h
        somme = 0
        for i in range(h):
            for j in range(w):
                pixel = ( (matrix[i][j][0] + matrix[i][j][1] + matrix[i][j][2])/3 )
                somme += (pixel*pixel)
        moyenneCarre = ( somme / nbpixels )
        return (math.sqrt(moyenneCarre - (moyenne * moyenne)))

    def img_Centree(self):
        img_matrix = self.imgToMatrix(self.path)
        dim = np.shape(img_matrix)
        w = dim[0]
        h = dim[1]
        imgCentre = np.ones((h, w, 1))
        moy = self.img_moyen(self.path)
        ecart = self.img_ecart(self.path)
        for i in range(h):
            for j in range(w):
                pixels = ( ( img_matrix[i][j][0] + img_matrix[i][j][1] + img_matrix[i][j][2] ) / 3 )
                imgCentre[i][j][0] = ((pixels - moy) / ecart)
        return imgCentre

    def matrix_moyen(self,matrix):
        dim = np.shape(matrix)
        w = dim[0]
        h = dim[1]
        nbpixels = w * h
        somme = 0
        for i in range(h):
            for j in range(w):
                pixel = matrix[i][j][0]
                somme += pixel
        return (somme / nbpixels)

class ImageChiffre(Image):

    def __init__(self,path):
        self.path = path

    def Binarisation(self):
        img = cv2.imread(self.path, cv2.IMREAD_GRAYSCALE)  # grey image
        (thresh, bin_img) = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)  # binary image
        imgArray = np.array(bin_img)
        cv2.imwrite(self.path, bin_img)  # save l'image
        sevenwhite = True
        one = True

        for i in range(4, 62):
            if (imgArray[3][i] == 0):
                sevenwhite = False

        for i in range(5, 63):
            if (imgArray[60][i] == 0):
                one = False

        if ((imgArray[0][0] == 0) and (imgArray[63][63] == 0)) or (sevenwhite == True) or (one == True):
            bin_img = cv2.imread(self.path)
            # make mask of white pixels / black pixels
            black = np.where((bin_img[:, :, 0] == 0) & (bin_img[:, :, 1] == 0) & (bin_img[:, :, 2] == 0))
            white = np.where((bin_img[:, :, 0] == 255) & (bin_img[:, :, 1] == 255) & (bin_img[:, :, 2] == 255))
            # Turn black pixels to white and vice versa
            bin_img[black] = (255, 255, 255)
            bin_img[white] = (0, 0, 0)
            cv2.imwrite(self.path, bin_img)  # save image

    def Normalisation(self):
        resized_img=np.zeros((64,64,3))
        dim = (64, 64)
        img = cv2.imread(self.path)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        edge = cv2.Canny(img, 50, 200)
        contours, hierarchy = cv2.findContours(edge.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
        for (i, c) in enumerate(sorted_contours):
            x, y, w, h = cv2.boundingRect(c)
            resized_img = img[y:y + h, x:x + w]
        resized_img = cv2.resize(resized_img, dim, interpolation=cv2.INTER_AREA)
        cv2.imwrite(self.path, resized_img)

    def imgToMatrix(self):
        img = cv2.imread(self.path)
        dim = np.shape(img)
        w = dim[0]
        h = dim[1]
        matrix = np.ones((h, w, 1), dtype="uint8")
        matrix[np.where((img == [0, 0, 0]).all(axis=2))] = [0]
        return matrix

    def img_moyen(self):
        matrix = self.imgToMatrix()
        dim = np.shape(matrix)
        w = dim[0]
        h = dim[1]
        nbpixels = w * h
        somme = 0
        for i in range(h):
            for j in range(w):
                pixel = matrix[i][j][0]
                somme = somme + pixel
        return (somme / nbpixels)

    def img_ecart(self):
        moyenne = self.img_moyen()
        return (math.sqrt(moyenne - (moyenne * moyenne)))

    def img_Centree(self):
        img_matrix = self.imgToMatrix()
        dim = np.shape(img_matrix)
        w = dim[0]
        h = dim[1]
        imgCentre = np.ones((h, w, 1))
        moy = self.img_moyen()
        ecart = self.img_ecart()
        for i in range(h):
            for j in range(w):
                if (ecart == 0):
                    ecart = 1
                imgCentre[i][j][0] = ((img_matrix[i][j][0] - moy) / ecart)
        return imgCentre

    def matrix_moyen(self,matrix):
        dim = np.shape(matrix)
        w = dim[0]
        h = dim[1]
        nbpixels = w * h
        somme = 0
        for i in range(h):
            for j in range(w):
                pixel = matrix[i][j][0]
                somme = somme + pixel
        return (somme / nbpixels)

    def correlation(self, DatasetPath):
        self.Normalisation()
        self.Binarisation()
        imgG = self.img_Centree()
        corrMatrix = np.ones((12, 12, 1))
        moyenneMax = []
        stop = False
        jump = False
        cpt = 0
        MAXmoy = 0
        for image in os.listdir(DatasetPath):
            if stop == False:
                reffPath = os.path.join(DatasetPath, image)
                imageDataset = ImageChiffre(reffPath) # image from Dataset
                cor = 0
                cpt += 1
                if jump == False:
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-6, 6), range(-6, 6)):
                        for i, j in product(range(10, 48), range(10, 48)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                if MAXmoy < moy:
                    MAXmoy = moy
                if MAXmoy > 4:
                    stop = True
                    moyenneMax.append(MAXmoy)
                if moy < 0:
                    jump = True
                if (cpt == 6):
                    jump = False
                    moyenneMax.append(MAXmoy)
                    cpt = 0
                    MAXmoy = 0
        MAX = max(moyenneMax)
        self.taux = MAX
        index = moyenneMax.index(MAX)
        if (MAX == 0):
            return -1
        elif ( index == 0 or index == 6 ):
            cpt = 0
            MAXmoy = -1
            moyenneMax = [] # reinitialiser à vide
            path = "Dataset/zeroonesixeight"
            for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-4, 4), range(-2, 2)):
                        for i, j in product(range(15,35), range(32,58)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = -1
            MAX = max(moyenneMax)
            self.taux = MAX
            index = moyenneMax.index(MAX)
            if(index == 0):
                cpt = 0
                MAXmoy = -1
                moyenneMax = []  # reinitialiser à vide
                path = "Dataset/09"
                for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-6,6), range(-6,6)):
                        for i, j in product(range(20,38), range(20, 38)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = -1
                MAX = max(moyenneMax)
                self.taux = MAX
                index = moyenneMax.index(MAX)
                if(index == 0):
                    return 0
                else:
                    return 9
            if(index == 1):
                cpt = 0
                MAXmoy = -1
                moyenneMax = []  # reinitialiser à vide
                path = "Dataset/12"
                for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-2,2), range(-6,6)):
                        for i, j in product(range(52,58), range(10,48)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = -1
                MAX = max(moyenneMax)
                self.taux = MAX
                index = moyenneMax.index(MAX)
                if (index == 0):
                    return 1
                else:
                    cpt = 0
                    MAXmoy = -1
                    moyenneMax = []  # reinitialiser à vide
                    path = "Dataset/28"
                    for image in os.listdir(path):
                        reffPath = os.path.join(path, image)
                        imageDataset = ImageChiffre(reffPath)  # image from Dataset
                        cor = 0
                        cpt += 1
                        imgF = imageDataset.img_Centree()
                        for k, L in product(range(-4,4 ), range(-4, 4)):
                            for i, j in product(range(10,20), range(20,40)):
                                cor += (imgF[i][j]) * (imgG[i - k][j - L])
                            cor = (cor / (13 * 13))
                            corrMatrix[k + 6][L + 6] = cor
                        moy = self.matrix_moyen(corrMatrix)
                        if MAXmoy < moy:
                            MAXmoy = moy
                        if (cpt == 6):
                            moyenneMax.append(MAXmoy)
                            cpt = 0
                            MAXmoy = -1
                    MAX = max(moyenneMax)
                    self.taux = MAX
                    index = moyenneMax.index(MAX)
                    if (index == 0):
                        return 2
                    else:
                        return 8
            if(index == 2):
                return 6
            else:
                return 8
        elif (index == 5):
            cpt = 0
            MAXmoy = 0
            moyenneMax = [] # reinitialiser à vide
            path = "Dataset/fiveeight"
            for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-6, 6), range(-6, 6)):
                        for i, j in product(range(6, 32), range(50, 58)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = 0
            MAX = max(moyenneMax)
            self.taux = MAX
            index = moyenneMax.index(MAX)
            if(index == 0):
                return 5
            else:
                return 8
        elif (index == 4):
            cpt = 0
            MAXmoy = 0
            moyenneMax = [] # reinitialiser à vide
            path = "Dataset/foursix"
            for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-6, 6), range(-6, 6)):
                        for i, j in product(range(48, 58), range(10,48)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = 0
            MAX = max(moyenneMax)
            self.taux = MAX
            index = moyenneMax.index(MAX)
            if(index == 0):
                return 4
            else:
                return 6
        elif (index == 3):
            cpt = 0
            MAXmoy = 0
            moyenneMax = [] # reinitialiser à vide
            path = "Dataset/onethreeseven"
            for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-6, 6), range(-6, 6)):
                        for i, j in product(range(6,58), range(50,58)):
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = 0
            MAX = max(moyenneMax)
            self.taux = MAX
            index = moyenneMax.index(MAX)
            if(index == 0):
                cpt = 0
                MAXmoy = -1
                moyenneMax = []  # reinitialiser à vide
                path = "Dataset/13"
                for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-4, 4), range(-4, 4)):
                        for i, j in product(range(52,58), range(10,48)): #######################################################################
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = -1
                MAX = max(moyenneMax)
                self.taux = MAX
                index = moyenneMax.index(MAX)
                if (index == 0):
                    return 1
                else:
                    return 3
            if (index == 1):
                return 3
            else:
                return 7
        elif ( index == 1 ):
            cpt = 0
            MAXmoy = -1
            moyenneMax = []  # reinitialiser à vide
            path = "Dataset/oneseven"
            for image in os.listdir(path):
                reffPath = os.path.join(path, image)
                imageDataset = ImageChiffre(reffPath)  # image from Dataset
                cor = 0
                cpt += 1
                imgF = imageDataset.img_Centree()
                for k, L in product(range(-2, 2), range(-2, 2)):
                    for i, j in product(range(1,5), range(10, 48)):
                        cor += (imgF[i][j]) * (imgG[i - k][j - L])
                    cor = (cor / (13 * 13))
                    corrMatrix[k + 6][L + 6] = cor
                moy = self.matrix_moyen(corrMatrix)
                if MAXmoy < moy:
                    MAXmoy = moy
                if (cpt == 6):
                    moyenneMax.append(MAXmoy)
                    cpt = 0
                    MAXmoy = -1
            MAX = max(moyenneMax)
            self.taux = MAX
            index = moyenneMax.index(MAX)
            if (index == 0):
                cpt = 0
                MAXmoy = -1
                moyenneMax = []  # reinitialiser à vide
                path = "Dataset/13"
                for image in os.listdir(path):
                    reffPath = os.path.join(path, image)
                    imageDataset = ImageChiffre(reffPath)  # image from Dataset
                    cor = 0
                    cpt += 1
                    imgF = imageDataset.img_Centree()
                    for k, L in product(range(-4, 4), range(-4, 4)):
                        for i, j in product(range(52, 58), range(10,
                                                                 48)):  #######################################################################
                            cor += (imgF[i][j]) * (imgG[i - k][j - L])
                        cor = (cor / (13 * 13))
                        corrMatrix[k + 6][L + 6] = cor
                    moy = self.matrix_moyen(corrMatrix)
                    if MAXmoy < moy:
                        MAXmoy = moy
                    if (cpt == 6):
                        moyenneMax.append(MAXmoy)
                        cpt = 0
                        MAXmoy = -1
                MAX = max(moyenneMax)
                self.taux = MAX
                index = moyenneMax.index(MAX)
                if (index == 0):
                    return 1
                else:
                    return 3
            else:
                return 7
        elif (index==7):
            return 9
        else:
            return index
    def decisionChiffre(self, DatasetPath):
        nombre = self.correlation(DatasetPath)
        if nombre != -1:
            print("Le chiffre est: ", nombre)
        else:
            print("Ce n'est pas un chiffre!")
#dataset = Dataset("C:/Users/Snow/PycharmProjects/pythonProject/Dataset/ALL")
#image = ImageChiffre("C:/Users/Snow/PycharmProjects/pythonProject/Test/6_ArialBlack_Bold_Italique.png")
#image.decisionChiffre(dataset.path)
