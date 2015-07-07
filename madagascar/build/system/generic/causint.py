sfcausint = rsf.doc.rsfprog('sfcausint','system/generic/Mcausint.c','''Causal integration on the first axis. ''')
sfcausint.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint integration '''))
sfcausint.version('1.7')
sfcausint.synopsis('''sfcausint < in.rsf > out.rsf adj=n''','''
December 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/370-Program-of-the-month-sfcausint.html
''')
rsf.doc.progs['sfcausint']=sfcausint

