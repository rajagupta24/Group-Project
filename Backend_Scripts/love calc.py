import random
print("\nEnter your name:")
n1=input()
print("\nEnter your partners name:")
n2=input()
name=n1+n2
new_name=name.lower()
t=new_name.count('t')
r=new_name.count('r')
u=new_name.count('u')
e=new_name.count('e')
tens=(t+r+u+e)*1.7
l=new_name.count('l')
o=new_name.count('o')
v=new_name.count('v')
e=new_name.count('e')
ones=(l+o+v+e)*2
percentage=(tens*10)+(ones)
if percentage>100:
    percentage=100-random.randint(2,9)
if(percentage <10 or percentage>90  ):
    print(f"your love score is {percentage}%, you go together like coke and mentos")
else:
    print(f"your love score is {percentage}%")
