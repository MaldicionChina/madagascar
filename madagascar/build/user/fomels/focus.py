sffocus = rsf.doc.rsfprog('sffocus','user/fomels/Mfocus.c','''Focusing indicator. ''')
sffocus.par('dim',rsf.doc.rsfpar('int','','','''dimensionality '''))
sffocus.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sffocus.par('verb',rsf.doc.rsfpar('bool','y','',''''''))
sffocus.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sffocus.version('1.7')
sffocus.synopsis('''sffocus < in.rsf > out.rsf dim= niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sffocus']=sffocus

