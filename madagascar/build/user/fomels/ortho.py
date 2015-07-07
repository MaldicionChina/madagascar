sfortho = rsf.doc.rsfprog('sfortho','user/fomels/Mortho.c','''Orthogonolize signal and noise. ''')
sfortho.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortho.par('sig2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortho.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfortho.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfortho.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfortho.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfortho.version('1.7')
sfortho.synopsis('''sfortho < fnoi.rsf sig=fsig.rsf > fnoi2.rsf sig2=fsig2.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfortho']=sfortho

