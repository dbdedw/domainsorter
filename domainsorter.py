import os.path, os
checks = 0
usernames = []
passwords = []

if not os.path.exists("./input.txt"):
    f= open("input.txt","w+")
if not os.path.exists("results"):
    os.makedirs("results")
if not os.path.exists("results/sorter"):
    os.makedirs("results/sorter")

checkname = input ("what do you want the name of this check to be?\n")
domainname = input ("what domain do you want to extract?\n")
os.makedirs('results/sorter/{}'.format(checkname))
with open("input.txt", "r+", encoding='utf-8') as s:
    sx = s.readlines()
    for x in sx:
      username = x.split(":")[0].replace('\n', '')
      password = x.split(":")[1].replace('\n', '')
      usernames.append(username)
      passwords.append(password)
      if checks <len(usernames):
        while checks <len(usernames):
          if username.__contains__(domainname):
            open('results/sorter/{}/{}.txt'.format(checkname, domainname),'a+').write("{}{}\n".format(username, password))
            checks+=1
          else:
            open('results/sorter/{}/no{}.txt'.format(checkname, domainname),'a+').write("{}{}\n".format(username, password))
            checks+=1