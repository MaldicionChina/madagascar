sfcdivn = rsf.doc.rsfprog('sfcdivn','user/fomels/Mcdivn.c','''Smooth division for complex data. ''')
sfcdivn.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcdivn.par('niter',rsf.doc.rsfpar('int','100','','''number of iterations '''))
sfcdivn.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sfcdivn.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfcdivn.version('1.7')
sfcdivn.synopsis('''sfcdivn < fnum.rsf den=fden.rsf > frat.rsf niter=100 verb=y rect#=(1,1,...)''','''''')
rsf.doc.progs['sfcdivn']=sfcdivn

