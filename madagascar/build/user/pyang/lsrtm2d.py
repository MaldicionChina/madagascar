sflsrtm2d = rsf.doc.rsfprog('sflsrtm2d','user/pyang/Mlsrtm2d.c','''2-D zero-offset least-squares reverse time migration (LSRTM)''')
sflsrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflsrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sflsrtm2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sflsrtm2d.par('niter',rsf.doc.rsfpar('int','10','','''totol number of least-squares iteration'''))
sflsrtm2d.par('tol',rsf.doc.rsfpar('float','1.e-12','','''tolerance of inversion '''))
sflsrtm2d.version('1.7')
sflsrtm2d.synopsis('''sflsrtm2d < data.rsf > imag.rsf vel=modl.rsf n0=0 verb=n niter=10 tol=1.e-12''','''''')
rsf.doc.progs['sflsrtm2d']=sflsrtm2d

