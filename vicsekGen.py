from PIL import Image, ImageDraw

width = 1920
height = 1920
colWht = (255,255,255)
colBlk = (0,0,0)

img = Image.new('RGB',(width,height), colWht)
drw = ImageDraw.Draw(img)

#init points
cntr = [int(width/2), int(height/2)]
size = 100

#Inital single box
drw.polygon([(cntr[0] -size,cntr[1] -size), (cntr[0] -size,cntr[1] +size),(cntr[0] +size,cntr[1] +size), (cntr[0] +size,cntr[1] -size)], fill=colBlk)
#img.show()
box = (cntr[0] -size,cntr[1] -size,cntr[0] +size,cntr[1] +size)

def drawCross(box,step,cropImg):

    for i in range(0,step):
        img.show()
        tempImg = img.crop(box)

        tempImg.show()

        img.paste(tempImg, (box[0] - 2*size, box[1]))
        img.paste(tempImg, (box[0], box[1]- 2*size))
        img.paste(tempImg, (box[0] + 2*size, box[1]))
        img.paste(tempImg, (box[0], box[1] + 2*size))


        box = [box[0]-img.width, box[1]-img.height, box[0]+img.width, box[1]+img.height]



drawCross(box,2,img)

img.show()