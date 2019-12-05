print('akskj')
print('First line\nsecond line')
print('C:\slow\software\game')
print("""
 i love you
        miss you brother
 """)
print('py' 'thon')

world='python'
print(world)

print(world[0:len(world)-2])
print(world[0:2])
x = world[0:3]+'py'
print(x)
a='akash'
b='hotash'
print('{0}    {1}'.format(a,b))

x,y=1,10
while(x<y):
    if x%2 ==0:
        print(x,end=',')
    x = x+1
y=0
if y==0:
    print('y is equal to {0}'.format(y))
elif y>0:
    print('y is greater than {0}'.format(y))
else:
    print('y is less than {0}'.format(y))

print(list(range(10)))

for i in range(10):
    print(i)
def myFunction(n):
    print("aksh",10,20)

myFunction(10)