sfdeblur = rsf.doc.rsfprog('sfdeblur','user/fomels/Mdeblur.c','''Non-stationary debluring by inversion ''')
sfdeblur.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdeblur.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdeblur.par('nliter',rsf.doc.rsfpar('int','1','','''number of nonlinear iterations '''))
sfdeblur.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfdeblur.par('eps',rsf.doc.rsfpar('float','0.','','''regularization parameter '''))
sfdeblur.version('1.7')
sfdeblur.synopsis('''sfdeblur < in.rsf > out.rsf rect=rect.rsf niter=100 nliter=1 verb=n eps=0.''','''''')
rsf.doc.progs['sfdeblur']=sfdeblur

