sfthreshold = rsf.doc.rsfprog('sfthreshold','system/generic/Mthreshold.c','''Soft thresholding. ''')
sfthreshold.par('pclip',rsf.doc.rsfpar('float','','','''percentage to clip '''))
sfthreshold.version('1.7')
sfthreshold.synopsis('''sfthreshold < in.rsf > out.rsf pclip=''','''
November 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/409-Program-of-the-month-sfthreshold.html
''')
rsf.doc.progs['sfthreshold']=sfthreshold

