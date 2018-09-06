import requests
import os
import random
import string
import json

url = 'http://craigslist.pottsfam.com/index872dijasydu2iuad27aysdu2yytaus6d2ajsdhasdasd2.php'

##### INIT SECTION #####
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
#creates char set 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
random.seed = (os.urandom(1024))



def loadArray():
	domains = json.loads(open('domains.json').read())
	lnames = json.loads(open('lnames.json').read())
	female = json.loads(open('female-fname.json').read())
	male = json.loads(open('male-fname.json').read())
	return(domains, lnames, female, male)

def getName():
	personType = random.choice(['male','female'])
	email_format = random.choice([1, 2, 3])
	lname = random.choice(lnames)
	if personType is 'male':
		fname = random.choice(male)
	else:
		fname = random.choice(female)
	if email_format is 1:
		print(fname + "." + lname + "@" + random.choice(domains))
	elif email_format is 2:
		print(fname + "_" + lname + "@" + random.choice(domains))
	else:
		print(fname[0] + lname + "@" + random.choice(domains))


def post(count):
	for name in names:
		name_extra = ''.join(random.choice(string.digits))

		username = name.lower() + name_extra + '@yahoo.com'
		password = ''.join(random.choice(chars) for i in range(8))

		requests.post(url, allow_redirects=False, data={
			'auid2yjauysd2uasdasdasd': username,
			'kjauysd6sAJSDhyui2yasd': password
		})


if __name__ == "__main__": # execute only if run as a script
	domains, lnames, female, male = loadArray()
	print 'sending username %s and password %s' % (username, password)
