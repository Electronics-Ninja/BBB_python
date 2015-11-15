import time, Image, ImageDraw, collections, psutil
from Adafruit_LED_Backpack import Matrix8x8

display = Matrix8x8.Matrix8x8(address=0x73, busnum=1)
display.begin()
display.clear()
display.write_display()
history = collections.deque([0]*8)

try:
	while True:
		load = psutil.cpu_percent(interval=2)
		height = load/100*8
		height = int(height + 0.5)
		if (height > 8): height = 8
		history.append(height)
		history.popleft()
		image = Image.new('1', (8,8))
		draw = ImageDraw.Draw(image)
		if height == 0:
			display.set_pixel(0,0,1)
			display.write_display()
		for i in range(8):
			height = history[i]
			if (height > 0):
				draw.line((i,7,i,8-height), fill=255)
		display.set_image(image)
		display.write_display()
except KeyboardInterrupt:
	pass
