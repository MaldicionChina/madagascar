sfshapeagc = rsf.doc.rsfprog('sfshapeagc','user/fomels/Mshapeagc.c','''Automatic gain control by shaping regularization. ''')
sfshapeagc.par('gain',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshapeagc.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfshapeagc.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfshapeagc.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfshapeagc.par('rect#',rsf.doc.rsfpar('int','(125,1,1,...)','','''smoothing radius on #-th axis '''))
sfshapeagc.par('gain',rsf.doc.rsfpar('string ',desc='''output gain file (optional) (auxiliary output file name)'''))
sfshapeagc.version('1.7')
sfshapeagc.synopsis('''sfshapeagc < in.rsf > out.rsf gain=fgain.rsf niter=100 eps=0.0f verb=n rect#=(125,1,1,...)''','''''')
rsf.doc.progs['sfshapeagc']=sfshapeagc

