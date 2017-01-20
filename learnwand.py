from wand.color import Color
from wand.image import Image
from wand.drawing import Drawing
from wand.font import Font
'''
with Color('blue') as bg:
	with Image(width=200, height = 200, background=bg) as img:
		img.save(filename = '200-100-blue.png')


with Image(filename='sf.jpeg') as img:
	print(img.width)
	print(img.height)
	img.resize(100, 56)
	img.save(filename = "sf_1.jpeg")


with Image(filename = 'sf.jpeg') as img:
	with img.clone() as flipped:
		flipped.flop()
		flipped.save(filename = 'sf-2.jpeg')

'''
#font = Font(path='./font/Americana Bold BT.ttf', size=64)
'''
with Drawing() as draw:
	with Image(filename='sf.jpeg') as img:
		with Color('light gray') as color:
			draw.fill_color = color
			draw.rectangle(left = 0, top =150, width = 300, height = 18)
		draw(img)
		img.save(filename = 'sf.jpeg')

with Drawing() as draw:	
	with Image(filename='sf.jpeg') as img:
		with Color('black') as color:
			draw.font = './font/Americana Bold BT.ttf' 
			draw.font_size = 40
			draw.text(10, 160, 'Hello World')
		draw(img)
		img.save(filename = 'sf.jpeg')
'''
from wand.font import Font 
font = Font(path='./font/Americana Bold BT.ttf', size=64)
with Image(width=300, height=150) as image:
	image.caption('wand', left=5, top=5, width=490, height=140, font=font)
	image.save(filename='caption-result.png')
'''
with Drawing() as draw:
	with Image(filename = './San_Francisco/sf1.jpg') as img:
		img.resize(500, 500)
		with Color('ivory') as color:
			draw.fill_color = color
			draw.rectangle(left = 0, top = 400, width = 500, height = 100)
		draw(img)
		img.save(filename = './San_Francisco/sf1.jpg')
'''