import requests
import hashlib

#Non-hash password
url="https://api.pwnedpasswords.com/range/"+"password123"
res=requests.get(url)
print(res)
#If the output is Response 400 it is BAD

#Hash password
url="https://api.pwnedpasswords.com/range/"+"CBFDAC6008F9CAB4083784CBD1874F76618D2A97"
res=requests.get(url)
print(res)

#Password Checker module


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res=requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code},ch')
    return res

def get_password_leaks_count(hashes,hash_to_check):
	hashes = (line.split(":") for line in hashes.text.splitlines())
	for h,count in hashes:
		if h==hash_to_check:
			return count
	return 0
	

def pwned_api_check(password): #Hashed password
    sha1password=hashlib.sha1(password.encode("utf-8").hexdigest().upper())
    first5_char,tail=sha1password[:5],sha1password[5:]
    response=request_api_data(first5_char)
    return get_password_leaks_count(response,tail)

def main(args):
	for password in args:
		count=pwned_api_check(password)
	if count:
		print(f'{password} was found {count} times')
	else:
		print(f'{password} was NOT found, so you are fine')
	return "done!"

main("123")
request_api_data("123")
pwned_api_check("123")






# #You will not be able to run this file here and will need to copy it onto your computer and run it on your machine. 
# #You will also need to make sure you have installed the requests module from PyPi (pip install)
# import requests
# import hashlib
# import sys

# def request_api_data(query_char):
#   url = 'https://api.pwnedpasswords.com/range/' + query_char
#   res = requests.get(url)
#   if res.status_code != 200:
#     raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
#   return res

# def get_password_leaks_count(hashes, hash_to_check):
#   hashes = (line.split(':') for line in hashes.text.splitlines())
#   for h, count in hashes:
#     if h == hash_to_check:
#       return count
#   return 0

# def pwned_api_check(password):
#   sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
#   first5_char, tail = sha1password[:5], sha1password[5:]
#   response = request_api_data(first5_char)
#   return get_password_leaks_count(response, tail)

# def main(args):
#   for password in args:
#     count = pwned_api_check(password)
#     if count:
#       print(f'{password} was found {count} times... you should probably change your password!')
#     else:
#       print(f'{password} was NOT found. Carry on!')
#   return 'done!'

# if __name__ == '__main__':
#   sys.exit(main(sys.argv[1:]))