sfmax1 = rsf.doc.rsfprog('sfmax1','system/generic/Mmax1.c','''Picking local maxima on the first axis. ''')
sfmax1.par('min',rsf.doc.rsfpar('float','o1','','''minimum value of time '''))
sfmax1.par('max',rsf.doc.rsfpar('float','o1+(n1-1)*d1','','''maximum value of time '''))
sfmax1.par('np',rsf.doc.rsfpar('int','n1','','''maximum number of picks '''))
sfmax1.par('sorted',rsf.doc.rsfpar('bool','y','','''if y, sort by amplitude '''))
sfmax1.version('1.7')
sfmax1.synopsis('''sfmax1 < in.rsf > out.rsf min=o1 max=o1+(n1-1)*d1 np=n1 sorted=y''','''
Outputs complex numbers (time,amplitude) 

September 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/403-Program-of-the-month-sfmax1.html
''')
rsf.doc.progs['sfmax1']=sfmax1

