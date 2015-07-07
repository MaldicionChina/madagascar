sfpwsmooth = rsf.doc.rsfprog('sfpwsmooth','user/pwd/Mpwsmooth.c','''2-D structure-enhancing filtering. ''')
sfpwsmooth.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwsmooth.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpwsmooth.par('ns',rsf.doc.rsfpar('int','0','','''smoothing radius '''))
sfpwsmooth.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfpwsmooth.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwsmooth.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwsmooth.version('1.7')
sfpwsmooth.synopsis('''sfpwsmooth < in.rsf dip=dip.rsf > out.rsf verb=n ns=0 adj=n eps=0.01 order=1''','''''')
rsf.doc.progs['sfpwsmooth']=sfpwsmooth

