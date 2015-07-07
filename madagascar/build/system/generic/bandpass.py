sfbandpass = rsf.doc.rsfprog('sfbandpass','system/generic/Mbandpass.c','''Bandpass filtering. ''')
sfbandpass.par('flo',rsf.doc.rsfpar('float','','','''Low frequency in band, default is 0 '''))
sfbandpass.par('fhi',rsf.doc.rsfpar('float','','','''High frequency in band, default is Nyquist '''))
sfbandpass.par('phase',rsf.doc.rsfpar('bool','n','','''y: minimum phase, n: zero phase '''))
sfbandpass.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfbandpass.par('nplo',rsf.doc.rsfpar('int','6','','''number of poles for low cutoff '''))
sfbandpass.par('nphi',rsf.doc.rsfpar('int','6','','''number of poles for high cutoff '''))
sfbandpass.version('1.7')
sfbandpass.synopsis('''sfbandpass < in.rsf > out.rsf flo= fhi= phase=n verb=n nplo=6 nphi=6''','''
November 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/313-Program-of-the-month-sfbandpass.html
''')
rsf.doc.progs['sfbandpass']=sfbandpass

