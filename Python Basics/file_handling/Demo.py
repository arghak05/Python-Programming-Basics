f=open('MyData.txt','r')

print(f.readline(),end='') # Reads 1 line
print(f.readline(),end='')
print(f.read()) # Reads whole file

f1=open('abc.txt','w')
f1.write('Something')
f1.write('People')
f1.write('Laptop')

f2=open('abc.txt','a')
f2.write('Mobile')

