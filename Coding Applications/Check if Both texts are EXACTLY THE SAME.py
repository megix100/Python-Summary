import re
print("\nCheck if both TEXTS are the EXACTLY THE SAME")
patt=re.compile("Hello, Mr Ciro could you please pass the salt?")
d=patt.fullmatch("Hello, Mr Ciro could you please pass the salt!")
#EVEN A SMALL DIFFERENCE - EXCLAMATION / INTERROGATION SIGNS WILL GET CAUGHT - And the RETURN IS NONE
print(d)
pat=re.compile("Hello, Mr Ciro could you please pass the salt")
e=pat.fullmatch("Hello, Mr Ciro could you please pass the salt")
#if it is equal then it is True
print(e)