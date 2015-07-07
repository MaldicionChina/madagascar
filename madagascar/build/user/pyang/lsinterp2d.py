sflsinterp2d = rsf.doc.rsfprog('sflsinterp2d','user/pyang/Mlsinterp2d.c','''Least-squares interpolation for 2D validition''')
sflsinterp2d.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsinterp2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsinterp2d.par('niter',rsf.doc.rsfpar('int','100','','''inner iterations '''))
sflsinterp2d.par('nouter',rsf.doc.rsfpar('int','5','','''outer iterations '''))
sflsinterp2d.par('eps',rsf.doc.rsfpar('float','1.e-2','','''regularization parameter '''))
sflsinterp2d.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sflsinterp2d.version('1.7')
sflsinterp2d.synopsis('''sflsinterp2d < Fin.rsf mask=Fmask.rsf > Fout.rsf verb=n niter=100 nouter=5 eps=1.e-2''','''''')
rsf.doc.progs['sflsinterp2d']=sflsinterp2d

