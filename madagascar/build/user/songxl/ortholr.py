sfortholr = rsf.doc.rsfprog('sfortholr','user/songxl/Mortholr.cc','''Lowrank decomposition for 3-D orthorhombic wave propagation. ''')
sfortholr.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortholr.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortholr.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortholr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfortholr.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfortholr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfortholr.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfortholr.version('1.7')
sfortholr.synopsis('''sfortholr < velz.rsf fft=fft.rsf > middle.rsf left=left.rsf right=right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfortholr']=sfortholr

