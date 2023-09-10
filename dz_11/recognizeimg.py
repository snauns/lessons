import cv2
from PIL import Image
class RecognizeImg:
    def __init__(self, path:str):
        self.Path = path
        self.Image = cv2.imread(self.Path)
        self.MultiScale = []
    def ShowImg(self, winName:str):
        cv2.imshow(winName, self.Image)
        cv2.waitKey()
    def GetCoordinates(self, fileName:str):
        cascade = cv2.CascadeClassifier(fileName)
        self.MultiScale = cascade.detectMultiScale(self.Image)
    def HighLight(self):
        for (x, y, w, h) in self.MultiScale:
            cv2.rectangle(self.Image, (x,y), (x+w, y+h), (0, 0, 255), 3)
    def AddImage(self, path:str, newPhotoPath:str):
        try:
            fLayout = Image.open(self.Path)
            sLayout = Image.open(path)
            fLayoutConverted = fLayout.convert('RGBA')
            sLayoutConverted = sLayout.convert('RGBA')
            for (x, y, w, h) in self.MultiScale:
                resizeRation  = fLayout.width / w
                sLayoutConverted = sLayoutConverted.resize((w, int(h/resizeRation)))
                fLayoutConverted.paste(sLayoutConverted, (x, int(y + h/(4*resizeRation))), sLayoutConverted)
                fLayoutConverted.save(newPhotoPath)
                self.Image = cv2.imread(newPhotoPath)
        except Exception as ex:
            print(ex)