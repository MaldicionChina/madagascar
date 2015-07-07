sfpow = rsf.doc.rsfprog('sfpow','system/generic/Mpow.c','''Apply power gain. ''')
sfpow.par('tpow',rsf.doc.rsfpar('float','0.','','''power on the first axis '''))
sfpow.par('pow#',rsf.doc.rsfpar('float','(0,0,...)','','''power on #-th axis '''))
sfpow.version('1.7')
sfpow.synopsis('''sfpow < in.rsf > out.rsf tpow=0. pow#=(0,0,...)''','''
March 2013 program of the month:
http://www.ahay.org/rsflog/index.php?/archives/327-Program-of-the-month-sfpow.html
''')
rsf.doc.progs['sfpow']=sfpow

