sfsimidenoise1 = rsf.doc.rsfprog('sfsimidenoise1','user/chenyk/Msimidenoise1.c','''Random noise attenuation using local similarity (different weighting approach) ''')
sfsimidenoise1.par('similarity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimidenoise1.par('s1',rsf.doc.rsfpar('float','','','''thresholding level 1 '''))
sfsimidenoise1.par('s2',rsf.doc.rsfpar('float','','','''thresholding level 2 '''))
sfsimidenoise1.version('1.7')
sfsimidenoise1.synopsis('''sfsimidenoise1 < in.rsf > out.rsf similarity=simi.rsf s1= s2=''','''The weighting function is defined as
W(s) = 1				if s>s2
	 = (s-s1)/(s2-s1)	if s1<=s<=s2
	 = 0				if s<s1
''')
rsf.doc.progs['sfsimidenoise1']=sfsimidenoise1

