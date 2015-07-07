sfhistogram = rsf.doc.rsfprog('sfhistogram','system/generic/Mhistogram.c','''Compute a histogram of integer- or float-valued input data.''')
sfhistogram.par('n1',rsf.doc.rsfpar('int','','','''number of histogram samples '''))
sfhistogram.par('o1',rsf.doc.rsfpar('float','','','''histogram origin '''))
sfhistogram.par('d1',rsf.doc.rsfpar('float','','','''histogram sampling '''))
sfhistogram.version('1.7')
sfhistogram.synopsis('''sfhistogram < in.rsf > out.rsf n1= o1= d1=''','''
The output grid is not centered on the bins; it marks their "left edge".
I.e., the first sample holds the number of values between o1 and o1+d1. 

February 2015 program of the month:
http://ahay.org/rsflog/index.php?/archives/427-Program-of-the-month-sfhistogram.html
''')
rsf.doc.progs['sfhistogram']=sfhistogram

