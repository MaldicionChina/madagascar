sfortllr = rsf.doc.rsfprog('sfortllr','user/songxl/Mortllr.cc','''Lowrank decomposition for 3-D orthorhombic wave propagation with linearization. ''')
sfortllr.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfortllr.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortllr.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfortllr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfortllr.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfortllr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfortllr.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfortllr.version('1.7')
sfortllr.synopsis('''sfortllr < velz.rsf fft=fft.rsf > middle.rsf left=left.rsf right=right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfortllr']=sfortllr

