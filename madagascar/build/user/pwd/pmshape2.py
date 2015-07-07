sfpmshape2 = rsf.doc.rsfprog('sfpmshape2','user/pwd/Mpmshape2.c','''Missing data interpolation in 2-D using plane-wave destruction and shaping regularization. ''')
sfpmshape2.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmshape2.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmshape2.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfpmshape2.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfpmshape2.par('rect1',rsf.doc.rsfpar('int','3','',''''''))
sfpmshape2.par('rect2',rsf.doc.rsfpar('int','3','','''smoothing radius '''))
sfpmshape2.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpmshape2.version('1.7')
sfpmshape2.synopsis('''sfpmshape2 < in.rsf > out.rsf dip=dip.rsf mask=mask.rsf niter=100 order=1 rect1=3 rect2=3''','''''')
rsf.doc.progs['sfpmshape2']=sfpmshape2

