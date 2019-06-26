from PIL import Image
def main():
	try:
		#Relative path
		#Image of right hand
		img = Image.open("images/hh1.png") 
		width, height = img.size
		area = (0,220,int(width),int(height/1.16))
		area1 = (0,240,int(width),int(height/1.65))
		area2 = (0,280,int(width),int(height/1.55))
		area3 = (int(width/2),280,int(width),int(height/1.3))
		# img_original = img
		img_default = img.crop(area)
		img1 = img.crop(area1)
		img2 = img.crop(area2)
		img3 = img.crop(area3)
		# Saved in the same relative location
		img_default.save("images/palm.png")
		img1.save("images/heartLine.png")	# Heart line - heart_parameter
		img2.save("images/headLine.png")	# Head line---head_parameter
		img3.save("images/lifeLine.png") # life line---age_parameter
		# Heart Line - shows a person's attitude to love and quality of love.
		# Head Line - reveals a person's wisdom, belief, attitude, thinking ability, strain capacity, creative ability as well as abilities of memory, self-control and more. 
		# LIfe line - age & mainly reflects a person's physical vitality and life energy
	except IOError:
		pass
if __name__ == "__main__":
	main()