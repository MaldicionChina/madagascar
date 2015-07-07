sfpwdsmooth2 = rsf.doc.rsfprog('sfpwdsmooth2','user/pwd/Mpwdsmooth2.c','''2-D smoothing by triangle plane-wave construction shaping. ''')
sfpwdsmooth2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpwdsmooth2.par('rect1',rsf.doc.rsfpar('int','3','',''''''))
sfpwdsmooth2.par('rect2',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfpwdsmooth2.par('adj',rsf.doc.rsfpar('bool','n','','''adjoint flag '''))
sfpwdsmooth2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfpwdsmooth2.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfpwdsmooth2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpwdsmooth2.version('1.7')
sfpwdsmooth2.synopsis('''sfpwdsmooth2 < in.rsf dip=dip.rsf > out.rsf rect1=3 rect2=3 adj=n verb=n eps=0.01 order=1''','''''')
rsf.doc.progs['sfpwdsmooth2']=sfpwdsmooth2

