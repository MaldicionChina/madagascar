sfsimilarity = rsf.doc.rsfprog('sfsimilarity','user/fomels/Msimilarity.c','''Local similarity measure between two datasets. ''')
sfsimilarity.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsimilarity.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfsimilarity.par('niter',rsf.doc.rsfpar('int','20','','''maximum number of iterations '''))
sfsimilarity.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfsimilarity.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfsimilarity.version('1.7')
sfsimilarity.synopsis('''sfsimilarity < in.rsf > out.rsf other=other.rsf verb=y niter=20 eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfsimilarity']=sfsimilarity

