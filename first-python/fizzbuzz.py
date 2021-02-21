opt=''
for i in range(1,100):
    if i%3==0 :
      opt += 'fizz'
    if i%5==0 :
        opt += 'buzz'
    if i%3!=0 and i%5!=0:
        opt += str(i)
    opt += '\n'
print(opt)
