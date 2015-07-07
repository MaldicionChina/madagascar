sfhelicon = rsf.doc.rsfprog('sfhelicon','user/gee/Mhelicon.c','''Multidimensional convolution and deconvolution by helix transform. ''')
sfhelicon.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfhelicon.par('n',rsf.doc.rsfpar('ints','','',''' [dim]'''))
sfhelicon.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint operation '''))
sfhelicon.par('div',rsf.doc.rsfpar('bool','n','','''if y, do inverse operation (deconvolution) '''))
sfhelicon.par('lag',rsf.doc.rsfpar('string','','','''file with filter lags '''))
sfhelicon.par('lag',rsf.doc.rsfpar('string ',desc='''file with filter lags'''))
sfhelicon.version('1.7 Mhelicon.c 12632 2014-05-13 23:21:50Z sfomel')
sfhelicon.synopsis('''sfhelicon < in.rsf filt=filt.rsf > out.rsf n= adj=n div=n lag=''','''
May 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/387-Program-of-the-math-sfhelicon.html
''')
rsf.doc.progs['sfhelicon']=sfhelicon

