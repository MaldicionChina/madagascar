sfcconv = rsf.doc.rsfprog('sfcconv','user/gee/Mcconv.c','''1-D convolution with complex numbers. ''')
sfcconv.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcconv.par('single',rsf.doc.rsfpar('bool','y','','''single channel or multichannel '''))
sfcconv.par('lag',rsf.doc.rsfpar('int','1','','''lag for internal convolution '''))
sfcconv.version('1.7 Mconv.c 7107 2011-04-10 02:04:14Z ivlad')
sfcconv.synopsis('''sfcconv < in.rsf > out.rsf filt=filt.rsf single=y lag=1''','''''')
rsf.doc.progs['sfcconv']=sfcconv

