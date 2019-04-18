def person(name,age,*number):
	s=0
	for n in number:
		s=s+n
	return s
t=(8,812,464,45)
print(cal(*t))