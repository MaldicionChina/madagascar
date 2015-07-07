sfnsmooth1 = rsf.doc.rsfprog('sfnsmooth1','user/fomels/Mnsmooth1.c','''1-D non-stationary smoothing. ''')
sfnsmooth1.par('rect',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnsmooth1.par('repeat',rsf.doc.rsfpar('int','1','','''repeat filtering several times '''))
sfnsmooth1.version('1.7 Msmooth.c 691 2004-07-04 19:28:08Z fomels')
sfnsmooth1.synopsis('''sfnsmooth1 < in.rsf > out.rsf rect=rect.rsf repeat=1''','''''')
rsf.doc.progs['sfnsmooth1']=sfnsmooth1

