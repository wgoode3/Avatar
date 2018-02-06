from PIL import Image
from random import randrange

def genAvatar(filename):
	color = (randrange(256), randrange(256), randrange(256))
	rand_img = [[randrange(0,2) for _ in xrange(5)] for _ in xrange(3)]
	rand_img.append(rand_img[1])
	rand_img.append(rand_img[0])
	im = Image.new('RGB', (5,5), color='white')

	for i in xrange(5):
		for j in xrange(5):
			if rand_img[i][j] == 1:
				im.putpixel((i,j), color)

	im = im.resize((200,200))
	im.save(filename + ".png")
	im.show()

genAvatar("test")