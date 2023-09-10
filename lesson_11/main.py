from recognizeimg import RecognizeImg
path = 'img\cat.jpg'
winname = 'Cat'
fileName = 'haarcascade_frontalcatface_extended.xml'
rec = RecognizeImg(path)
#rec.ShowImg(winname)
rec.GetCoordinates(fileName)#[[100  65  99  99]]
#print(rec.MultiScale)
#rec.HighLight()
newPath = 'img\glasses.jpg'
newPhotoPath = 'img\cat_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg(winname)