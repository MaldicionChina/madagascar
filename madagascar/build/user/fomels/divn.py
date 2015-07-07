sfdivn = rsf.doc.rsfprog('sfdivn','user/fomels/Mdivn.c','''Smooth division. ''')
sfdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfdivn.par('eps',rsf.doc.rsfpar('float','0.0f','','''regularization '''))
sfdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfdivn.version('1.7')
sfdivn.synopsis('''sfdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y eps=0.0f rect#=(1,1,...)''','''''')
rsf.doc.progs['sfdivn']=sfdivn

