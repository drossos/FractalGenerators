from PIL import Image, ImageDraw

width = 1920
height = 1920
colWht = (255,255,255)
colBlk = (0,0,0)

img = Image.new('RGB',(width,height), colWht)
drw = ImageDraw.Draw(img)
distFactor = 4
size = 100
#init points
cntr = [width/2, height/2]
divideFactor = 1
#drw.polygon([(cntr -size,cntr -size), (cntr -size,cntr +size),(cntr +size,cntr +size), (cntr +size,cntr -size)], fill=colBlk)

#Takes in 3 points each with (x,y) components and colour
#Is called resursively
def drawSqr(cntr,size,step,divideFactor):
    drw.polygon([(cntr[0] -size,cntr[1] -size), (cntr[0] -size,cntr[1] +size),(cntr[0] +size,cntr[1] +size), (cntr[0] +size,cntr[1] -size)], fill=colBlk)

    step -= 1


    if (step >= 0):
        divideFactor += 1
        drawSqr([(cntr[0] - distFactor*size), cntr[1]], size/divideFactor, step, divideFactor)
        drawSqr([(cntr[0] - distFactor*size), (cntr[1] - distFactor*size)], size/divideFactor, step, divideFactor)
        drawSqr([(cntr[0] - distFactor*size), (cntr[1] + distFactor* size)], size/divideFactor, step, divideFactor)

        drawSqr([(cntr[0] + distFactor * size), cntr[1]], size / divideFactor, step, divideFactor)
        drawSqr([(cntr[0] + distFactor * size), (cntr[1] - distFactor * size)], size / divideFactor, step, divideFactor)
        drawSqr([(cntr[0] + distFactor * size), (cntr[1] + distFactor * size)], size / divideFactor, step, divideFactor)

        drawSqr([cntr[0], (cntr[1] - distFactor* size) ], size/divideFactor, step, divideFactor)
        drawSqr([cntr[0], (cntr[1] + distFactor*size) ], size/divideFactor, step, divideFactor)

    else:
        return 0


#degree of the fractal
step = 5
drawSqr(cntr, size, step, divideFactor)

#shows the image in new window
#can also enable so image saves in directory 
img.show()