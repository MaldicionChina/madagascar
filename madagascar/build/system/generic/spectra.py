sfspectra = rsf.doc.rsfprog('sfspectra','system/generic/Mspectra.c','''Frequency spectra. ''')
sfspectra.par('all',rsf.doc.rsfpar('bool','n','','''if y, compute average spectrum for all traces '''))
sfspectra.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfspectra.version('1.7')
sfspectra.synopsis('''sfspectra < in.rsf > out.rsf all=n opt=y''','''
March 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/285-Program-of-the-month-sfspectra.html
''')
rsf.doc.progs['sfspectra']=sfspectra

