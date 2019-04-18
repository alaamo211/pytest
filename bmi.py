# -*- coding: utf-8 -*-

height = int(input('你的身高(米)：'))/100
weight = int(input('你的体重(公斤)：'))

bmi = weight/(height*height)
if bmi<18.5:
	print('过轻',bmi)
elif bmi>18.5 and bmi<=25:
	print('正常',bmi)
elif bmi>25 and bmi<=28:
	print('过重',bmi)
elif bmi>28 and bmi<=32:
	print('肥胖',bmi)
elif bmi>32:
	print('严重肥胖',bmi)	