f=open('tiger.jpg','rb') # Read binary (rb) for images

f1=open('Mypic.jpg','wb')

for i in f:
    f1.write(i)