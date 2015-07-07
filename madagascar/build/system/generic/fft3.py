sffft3 = rsf.doc.rsfprog('sffft3','system/generic/Mfft3.c','''FFT transform on extra axis.''')
sffft3.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sffft3.par('sym',rsf.doc.rsfpar('bool','n','','''if y, apply symmetric scaling to make the FFT operator Hermitian '''))
sffft3.par('sign',rsf.doc.rsfpar('int','inv? 1: 0','','''transform sign (0 or 1) '''))
sffft3.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sffft3.par('axis',rsf.doc.rsfpar('int','2','','''Axis to transform '''))
sffft3.par('pad',rsf.doc.rsfpar('int','2','','''padding factor '''))
sffft3.version('1.7')
sffft3.synopsis('''sffft3 < in.rsf > out.rsf inv=n sym=n sign=inv? 1: 0 opt=y axis=2 pad=2''','''
Input and output are complex data. The input is padded by factor pad.

July 2012 program of the month:
http://ahay.org/rsflog/index.php?/archives/298-Program-of-the-month-sffft3.html
''')
rsf.doc.progs['sffft3']=sffft3

