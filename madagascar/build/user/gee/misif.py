sfmisif = rsf.doc.rsfprog('sfmisif','user/gee/Mmisif.c','''Find MISSing Input values and Filter in 1-D. ''')
sfmisif.par('filtout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfmisif.par('nmiss',rsf.doc.rsfpar('int','n1','','''number of iterations '''))
sfmisif.par('na',rsf.doc.rsfpar('int','3','','''filter size '''))
sfmisif.par('lag',rsf.doc.rsfpar('int','1','','''filter lag '''))
sfmisif.version('1.7 Mmisif.c 7107 2011-04-10 02:04:14Z ivlad')
sfmisif.synopsis('''sfmisif < in.rsf > out.rsf filtout=flt.rsf nmiss=n1 na=3 lag=1''','''''')
rsf.doc.progs['sfmisif']=sfmisif

