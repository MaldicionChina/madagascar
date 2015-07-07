sflow = rsf.doc.rsfprog('sflow','user/chenyk/Mlow.c','''Calculating local (signal-and-noise) orthogonalization weight (LOW)  ''')
sflow.par('sig',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflow.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sflow.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sflow.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sflow.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sflow.version('1.7')
sflow.synopsis('''sflow < fnoi.rsf sig=fsig.rsf > flow.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sflow']=sflow

