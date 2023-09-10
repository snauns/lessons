from recognizeimg import RecognizeImg
path = 'img\cat.jpg'
winname = 'cat_face.jpg'
fileName = 'haarcascade_frontalcatface_extended.xml'
rec = RecognizeImg(path)
rec.GetCoordinates(fileName)
newPath = 'img\glasses.png'
newPhotoPath = 'img\cat_with_glasses.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg(winname)


path = 'img\cat_leo.jpg'
winname = 'cat_leo_glasses.jpg'
fileName = 'haarcascade_frontalcatface_extended.xml'
rec = RecognizeImg(path)
rec.GetCoordinates(fileName)
newPath = 'img\leo_glasses.png'
newPhotoPath = 'img\leo_the_cat.png'
rec.AddImage(newPath, newPhotoPath)
rec.ShowImg(winname)
