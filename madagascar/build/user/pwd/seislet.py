sfseislet = rsf.doc.rsfprog('sfseislet','user/pwd/Mseislet.c','''Seislet transform ''')
sfseislet.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfseislet.par('inv',rsf.doc.rsfpar('bool','n','','''if y, do inverse transform '''))
sfseislet.par('adj',rsf.doc.rsfpar('bool','n','','''if y, do adjoint transform '''))
sfseislet.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfseislet.par('unit',rsf.doc.rsfpar('bool','n','','''if y, use unitary scaling '''))
sfseislet.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfseislet.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfseislet.par('type',rsf.doc.rsfpar('string ',desc='''[haar,linear,biorthogonal] wavelet type, the default is linear  '''))
sfseislet.version('1.7')
sfseislet.synopsis('''sfseislet < in.rsf > out.rsf dip=dip.rsf inv=n adj=n eps=0.01 unit=n order=1 verb=n type=''','''''')
rsf.doc.progs['sfseislet']=sfseislet

