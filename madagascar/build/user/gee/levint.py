sflevint = rsf.doc.rsfprog('sflevint','user/gee/Mlevint.c','''Leveler inverse interpolation in 1-D. ''')
sflevint.par('nx',rsf.doc.rsfpar('int','','','''number of bins '''))
sflevint.par('x0',rsf.doc.rsfpar('float','','','''grid origin '''))
sflevint.par('dx',rsf.doc.rsfpar('float','','','''grid sampling '''))
sflevint.par('niter',rsf.doc.rsfpar('int','1+m1*3/2','',''''''))
sflevint.par('eps',rsf.doc.rsfpar('float','0.2','','''regularization parameter '''))
sflevint.par('na',rsf.doc.rsfpar('int','3','',''''''))
sflevint.par('head',rsf.doc.rsfpar('string ',desc=''''''))
sflevint.version('1.7 Mlevint.c 7107 2011-04-10 02:04:14Z ivlad')
sflevint.synopsis('''sflevint < in.rsf > out.rsf nx= x0= dx= niter=1+m1*3/2 eps=0.2 na=3 head=''','''''')
rsf.doc.progs['sflevint']=sflevint

