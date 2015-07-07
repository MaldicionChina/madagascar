sfcpef1 = rsf.doc.rsfprog('sfcpef1','user/gee/Mcpef1.c','''Estimate complex PEF on the first axis. ''')
sfcpef1.par('nf',rsf.doc.rsfpar('int','','','''filter length '''))
sfcpef1.par('niter',rsf.doc.rsfpar('int','2*nf','','''number of iterations '''))
sfcpef1.version('1.7')
sfcpef1.synopsis('''sfcpef1 < in.rsf > out.rsf nf= niter=2*nf''','''''')
rsf.doc.progs['sfcpef1']=sfcpef1

