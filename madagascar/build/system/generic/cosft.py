sfcosft = rsf.doc.rsfprog('sfcosft','system/generic/Mcosft.c','''Multi-dimensional cosine transform.''')
sfcosft.par('sign#',rsf.doc.rsfpar('int','0','','''transform along #-th dimension 
	  [+1 forward or -1 backward] '''))
sfcosft.version('1.7')
sfcosft.synopsis('''sfcosft < in.rsf > out.rsf sign#=0''','''
The input and output are real and have the same dimensions. 
Pad the data if you need to suppress wrap-around effects.
''')
rsf.doc.progs['sfcosft']=sfcosft

