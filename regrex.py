import re
massage = "abhijitborate20@gmail.com"
ansregerx=re.compile(r'[\wa-zA-Z]\w[0-9]@[\w.\w]')
print(ansregerx.findall(massage))


#massage = "hey  i want Email address"


# compiler