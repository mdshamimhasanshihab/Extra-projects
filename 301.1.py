import cmath as cm

B=int(input('Basic Size:'))
x=int(input(f'Enter the limit no-1 for D:'))
y=int(input(f'Enter the limit no-2 for D:'))

D=cm.sqrt(x*y)
print(f"\nThe value of D is-{D}\n" )
i=((D**(1/3))*0.45+0.001*D)*0.001
print(f'\nStandard tolerance Unit={i}\n')
it1=int(input('\nEnter it number for hole:'))
it2=int(input('\nEnter it number for Shaft:'))


print(f'\ntolerance grade for hole: {it1*i}\n')
print(f'\ntolerance grade for shaft: {it2*i}\n')

dev=input('\nEnter deviation letter for shaft:')
if (dev=='a'):
    if (D<=120):
        de=-(265+1.3*D)
    else:
        de=-3.5*D
elif (dev=='b'):
    if (D<=160):
        de=-(140+0.85*D)
    else:
        de=-1.8*D
elif (dev=='c'):
    if (D<=40):
        de=-52*(D**0.2)
    else:
        de=-(95+0.8*D)
elif (dev=='d'):
    de=-(16*(D**0.44))
elif (dev=='e'):
    de=-(11*(D**0.41))
elif (dev=='f'):
    de=-5.5*(D**0.34)
elif (dev=='g'):
    de=-2.5*(D**0.34)
elif (dev=='h'):
    de=0
else:
    print('value out of reach')

dee=de*0.001
print(f"Deviation for Shaft-{dee}")

print(f'\nMinimum clearance = {-dee}')
print(f'\nMaximum clearance = {-dee+it1*i+it2*i}')
print('__________________________________________\n')
print("\n For hole____")
print('Hole limits are---')
print(f'LLH={B}')
print(f'HLH={B+it1*i}')
print(f'Hole tolerance={it1*i}')
print('__________________________________________\n')
print(f"Deviation for Shaft-{dee}")
print("\n For Shaft____")
print(f'HLS={B+dee}')
print(f'HLS={B+dee-it2*i}')
print(f'Shaft tolerance={it2*i}')
print('__________________________________________\n')
print(f'Gauge tolerance for hole={it1*i*0.1}')
print(f'wear allowance for hole={it1*i*0.01}')
print('__________________________________________\n')
print(f'Gauge tolerance for Shaft={it2*i*0.1}')
print(f'wear allowance for Shaft={it2*i*0.01}')

print("\n\nFor Hole:")
print('__________________________________________\n')

print('Design of Go Gauge:\n')
print(f'Low limit={B+it1*i*0.01}')
print(f'High limit={B+it1*i*0.01+it1*i*0.1}')

print('__________________________________________\n')
print('Design of Not Go Gauge:\n')
print(f'Low limit={B+it1*i}')
print(f'High limit={B+it1*i+it1*i*0.1}')

print("\n\nFor Shaft:")
print('__________________________________________\n')

print('Design of Go Gauge:\n')
print(f'High limit={B+dee-it2*i*0.01}')
print(f'Low limit={B+dee-it2*i*0.01-it2*i*0.1}')

print('__________________________________________\n')
print('Design of Not Go Gauge:\n')
print(f'High limit={B+dee-it2*i}')
print(f'High limit={B+dee-it2*i-it2*i*0.1}')
