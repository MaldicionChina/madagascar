sfrotate = rsf.doc.rsfprog('sfrotate','system/main/rotate.c','''Rotate a portion of one or more axes in the data hypercube. ''')
sfrotate.par('verb',rsf.doc.rsfpar('bool','n','','''Verbosity flag '''))
sfrotate.par('memsize',rsf.doc.rsfpar('int','sf_memsize()','','''Max amount of RAM (in Mb) to be used '''))
sfrotate.par('rot#',rsf.doc.rsfpar('int','(0,0,...)','','''length of #-th axis that is moved to the end '''))
sfrotate.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfrotate')
sfrotate.version('1.7 rotate.c 1729 2006-03-12 10:00:32Z fomels')
sfrotate.synopsis('''sfrotate < in.rsf > out.rsf verb=n memsize=sf_memsize() rot#=(0,0,...)''','''''')
rsf.doc.progs['sfrotate']=sfrotate

