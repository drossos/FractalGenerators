from PIL import Image, ImageDraw

width = 1920
height = 1920
colWht = (255,255,255)
colBlk = (0,0,0)

img = Image.new('RGB',(width,height), colWht)
drw = ImageDraw.Draw(img)

size = 250
#init points
cntr = [width/2, height/2]
divideFactor = 2
#drw.polygon([(cntr -size,cntr -size), (cntr -size,cntr +size),(cntr +size,cntr +size), (cntr +size,cntr -size)], fill=colBlk)

#Takes in 3 points each with (x,y) components and colour
#Is called resursively
def drawSqr(cntr,size,step):
    drw.polygon([(cntr[0] -size,cntr[1] -size), (cntr[0] -size,cntr[1] +size),(cntr[0] +size,cntr[1] +size), (cntr[0] +size,cntr[1] -size)], fill=colBlk)

    step -= 1
    #TODO FIX THIS ONLY WORKS FOR ORDER 1
    if (step >= 0):
        drawSqr([cntr[0]/2 - size/divideFactor, cntr[1]], size/divideFactor, step)
        drawSqr([cntr[0]/2 - size/divideFactor, cntr[1] - cntr[1]/2 - size/divideFactor], size/divideFactor, step)
        drawSqr([cntr[0]/2 - size/divideFactor, cntr[1] + cntr[1]/2 + size/divideFactor], size/divideFactor, step)

        drawSqr([cntr[0] + cntr[0]/2 + size/divideFactor, cntr[1]], size/divideFactor, step)
        drawSqr([cntr[0] + cntr[0]/2 + size/divideFactor, cntr[1] - cntr[1]/2 - size/divideFactor], size/divideFactor, step)
        drawSqr([cntr[0] + cntr[0]/2 + size/divideFactor, cntr[1] + cntr[1]/2 + size/divideFactor], size/divideFactor, step)

        drawSqr([cntr[0], cntr[1] + cntr[1]/2 + size/divideFactor], size/divideFactor, step)
        drawSqr([cntr[0], cntr[1] - cntr[1]/2 - size/divideFactor], size/divideFactor, step)

    else:
        return 0


#degree of the fractal
step = 2
drawSqr(cntr, size, step)

#shows the image in new window
#can also enable so image saves in directory 
img.show()