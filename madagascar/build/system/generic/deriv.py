sfderiv = rsf.doc.rsfprog('sfderiv','system/generic/Mderiv.c','''First derivative with a maximally linear FIR differentiator. ''')
sfderiv.par('order',rsf.doc.rsfpar('int','6','','''filter order '''))
sfderiv.par('scale',rsf.doc.rsfpar('bool','n','','''if scale by 1/dx '''))
sfderiv.version('1.7')
sfderiv.synopsis('''sfderiv < in.rsf > out.rsf order=6 scale=n''','''
May 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/290-Program-of-the-month-sfderiv.html
''')
rsf.doc.progs['sfderiv']=sfderiv

