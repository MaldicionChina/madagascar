sfboxsmooth = rsf.doc.rsfprog('sfboxsmooth','system/generic/Mboxsmooth.c','''Multi-dimensional smoothing with boxes. ''')
sfboxsmooth.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfboxsmooth.par('rect#',rsf.doc.rsfpar('int','(1,1,...)','','''smoothing radius on #-th axis '''))
sfboxsmooth.version('1.7')
sfboxsmooth.synopsis('''sfboxsmooth < in.rsf > out.rsf repeat=1 rect#=(1,1,...)''','''''')
rsf.doc.progs['sfboxsmooth']=sfboxsmooth

