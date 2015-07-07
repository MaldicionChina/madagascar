sfhalfint = rsf.doc.rsfprog('sfhalfint','system/seismic/Mhalfint.c','''Half-order integration or differentiation. ''')
sfhalfint.par('adj',rsf.doc.rsfpar('bool','n','','''If y, apply adjoint '''))
sfhalfint.par('inv',rsf.doc.rsfpar('bool','n','','''If y, do differentiation instead of integration '''))
sfhalfint.par('rho',rsf.doc.rsfpar('float','1.-1./n1','','''Leaky integration constant '''))
sfhalfint.version('1.7')
sfhalfint.synopsis('''sfhalfint < in.rsf > out.rsf adj=n inv=n rho=1.-1./n1''','''
December 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/317-Program-of-the-month-sfhalfint.html
''')
rsf.doc.progs['sfhalfint']=sfhalfint

