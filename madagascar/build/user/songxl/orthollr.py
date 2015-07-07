sforthollr = rsf.doc.rsfprog('sforthollr','user/songxl/Morthollr.cc','''Lowrank decomposition for 3-D orthorhombic wave propagation with linearization. ''')
sforthollr.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sforthollr.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sforthollr.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sforthollr.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sforthollr.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sforthollr.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sforthollr.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sforthollr.version('1.7')
sforthollr.synopsis('''sforthollr < velz.rsf fft=fft.rsf > middle.rsf left=left.rsf right=right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sforthollr']=sforthollr

