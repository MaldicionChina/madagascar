sffkoclet = rsf.doc.rsfprog('sffkoclet','user/yliu/Mfkoclet.c','''1-D seislet transform using omega-wavenumber offset continuation ''')
sffkoclet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sffkoclet.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sffkoclet.par('dwt',rsf.doc.rsfpar('bool','n','','''if y, do wavelet transform '''))
sffkoclet.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity flag '''))
sffkoclet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sffkoclet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is biorthogonal  '''))
sffkoclet.version('1.7 Mfkoclet.c 9673 2012-12-13 04:51:41Z yang_liu')
sffkoclet.synopsis('''sffkoclet < in.rsf > out.rsf inv=n adj=n dwt=n verb=y eps=0.01 type=''','''Forward transform (adj=n inv=y/n) m=T[d]
Inverse transform (adj=y inv=y)   d=T^(-1)[d]
Adjoint transform (adj=y inv=n)   d=T'[d]
''')
rsf.doc.progs['sffkoclet']=sffkoclet

