l, u, p, d = 0, 0, 0, 0
s = "R@m@_f0rtu9e$"
if (len(s) >= 8):
	for i in s:

		# counting lowercase alphabets 
		if (i.islower()):
			l+=1		

		# counting uppercase alphabets
		if (i.isupper()):
			u+=1		

		# counting digits
		if (i.isdigit()):
			d+=1		

		# counting the mentioned special characters
		if(i=='@'or i=='$' or i=='_'):
			p+=1		
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
	print("Valid Password")
else:
	print("Invalid Password")




password="a"
length=len(password)
l=any(i.islower() for i in password)
u=any(i.isupper() for i in password)
d=any(i.isdigit() for i in password)
miss=3-(l+d+u)
if length<=6:
    print(max(miss,6-length))
elif length<=20:
    print(miss)
else:
    e=length-20
    print(e+max(miss,0))










