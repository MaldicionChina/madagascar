sfpefdeburst = rsf.doc.rsfprog('sfpefdeburst','user/gee/Mpefdeburst.c','''Burst noise removal using PEF. ''')
sfpefdeburst.par('na',rsf.doc.rsfpar('int','3','','''PEF length '''))
sfpefdeburst.par('niter',rsf.doc.rsfpar('int','10','','''number of iterations '''))
sfpefdeburst.version('1.7')
sfpefdeburst.synopsis('''sfpefdeburst < in.rsf > out.rsf na=3 niter=10''','''''')
rsf.doc.progs['sfpefdeburst']=sfpefdeburst

