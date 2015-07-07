sfshapefill = rsf.doc.rsfprog('sfshapefill','user/fomels/Mshapefill.c','''Missing data interpolation in 2-D by Laplacian regularization. ''')
sfshapefill.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfshapefill.par('niter',rsf.doc.rsfpar('int','200','','''number of iterations '''))
sfshapefill.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfshapefill.par('dim',rsf.doc.rsfpar('int','dim','','''dimensionality '''))
sfshapefill.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfshapefill.par('mask',rsf.doc.rsfpar('string ',desc='''optional mask file with zeroes for missing data locations (auxiliary input file name)'''))
sfshapefill.version('1.7')
sfshapefill.synopsis('''sfshapefill < in.rsf > out.rsf mask=mask.rsf niter=200 verb=n dim=dim rect#=(1,1,...)''','''''')
rsf.doc.progs['sfshapefill']=sfshapefill

