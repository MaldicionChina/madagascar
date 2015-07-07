sfburstnoise = rsf.doc.rsfprog('sfburstnoise','user/gee/Mburstnoise.c','''Synthetics with bursts of noise. ''')
sfburstnoise.par('sigma',rsf.doc.rsfpar('float','1.','','''noise magnitude '''))
sfburstnoise.par('thresh',rsf.doc.rsfpar('float','0.93','','''noise threshold '''))
sfburstnoise.par('thresh2',rsf.doc.rsfpar('float','0.4','','''noise threshold '''))
sfburstnoise.version('1.7 Mburstnoise.c 4796 2009-09-29 19:39:07Z ivlad')
sfburstnoise.synopsis('''sfburstnoise < in.rsf > out.rsf sigma=1. thresh=0.93 thresh2=0.4''','''''')
rsf.doc.progs['sfburstnoise']=sfburstnoise

