sfplanemis2 = rsf.doc.rsfprog('sfplanemis2','user/pwd/Mplanemis2.c','''Missing data interpolation in 2-D using plane-wave destruction. ''')
sfplanemis2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplanemis2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfplanemis2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfplanemis2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfplanemis2.par('nj1',rsf.doc.rsfpar('int','1','','''antialiasing for first dip '''))
sfplanemis2.par('nj2',rsf.doc.rsfpar('int','1','','''antialiasing for second dip '''))
sfplanemis2.par('prec',rsf.doc.rsfpar('bool','n','','''if y, apply preconditioning '''))
sfplanemis2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfplanemis2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfplanemis2.version('1.7')
sfplanemis2.synopsis('''sfplanemis2 < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf niter=100 order=1 nj1=1 nj2=1 prec=n verb=n''','''''')
rsf.doc.progs['sfplanemis2']=sfplanemis2

