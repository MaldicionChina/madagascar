sfconv = rsf.doc.rsfprog('sfconv','user/gee/Mconv.c','''1-D convolution. ''')
sfconv.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconv.par('trans',rsf.doc.rsfpar('bool','n','','''if y, transient convolution; if n, internal '''))
sfconv.par('each',rsf.doc.rsfpar('bool','n','','''if y, new filter for each trace '''))
sfconv.par('lag',rsf.doc.rsfpar('int','1','','''lag for internal convolution '''))
sfconv.version('1.7 Mconv.c 7107 2011-04-10 02:04:14Z ivlad')
sfconv.synopsis('''sfconv < in.rsf > out.rsf filt=filt.rsf trans=n each=n lag=1''','''''')
rsf.doc.progs['sfconv']=sfconv

