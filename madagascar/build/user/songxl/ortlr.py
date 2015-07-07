sfortlr = rsf.doc.rsfprog('sfortlr','user/songxl/Mortlr.cc','''Lowrank decomposition for 3-D orthorhombic wave propagation. ''')
sfortlr.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortlr.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortlr.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortlr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfortlr.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfortlr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfortlr.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfortlr.version('1.7')
sfortlr.synopsis('''sfortlr < velz.rsf fft=fft.rsf > middle.rsf left=left.rsf right=right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfortlr']=sfortlr

