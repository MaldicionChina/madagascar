sfpostfilter2 = rsf.doc.rsfprog('sfpostfilter2','system/generic/Mpostfilter2.c','''Convert B-spline coefficients to data in 2-D. ''')
sfpostfilter2.par('nw',rsf.doc.rsfpar('int','','','''filter size '''))
sfpostfilter2.par('vert',rsf.doc.rsfpar('bool','y','','''include filter on the first axis '''))
sfpostfilter2.par('horz',rsf.doc.rsfpar('bool','y','','''include filter on the second axis '''))
sfpostfilter2.version('1.7')
sfpostfilter2.synopsis('''sfpostfilter2 < in.rsf > out.rsf nw= vert=y horz=y''','''''')
rsf.doc.progs['sfpostfilter2']=sfpostfilter2

