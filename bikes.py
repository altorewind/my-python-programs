bikes=['ac','bc','cc','dc']

print(bikes)
print(bikes[-2].title())

eb=['axsax','gsrg','feqnyth','yadvje']
print(eb)
eb[1]='d321ewf'
print(eb)
eb.append('sosger')
print(eb)
eb.insert(0,'fdolo')
print(eb)
del eb[2]
print(eb)
ed=eb.pop(3)
print(eb)
print(ed)
eb.remove('axsax')
print(eb)
#eb.sort()
#print(eb)
print('sorted:',sorted(eb))
print('reversedsort:',sorted(eb,reverse=True))
eb.reverse()
print("len=",len(eb))
for i in eb:
	print(i)
