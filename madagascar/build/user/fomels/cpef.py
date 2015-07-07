sfcpef = rsf.doc.rsfprog('sfcpef','user/fomels/Mcpef.c','''1-D prediction-error filter estimation from complex data ''')
sfcpef.par('single',rsf.doc.rsfpar('bool','y','','''single channel or multichannel '''))
sfcpef.par('nf',rsf.doc.rsfpar('int','','','''filter length '''))
sfcpef.version('1.7')
sfcpef.synopsis('''sfcpef < in.rsf > out.rsf single=y nf=''','''''')
rsf.doc.progs['sfcpef']=sfcpef

