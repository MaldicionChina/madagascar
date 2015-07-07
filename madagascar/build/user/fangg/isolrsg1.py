sfisolrsg1 = rsf.doc.rsfprog('sfisolrsg1','user/fangg/Misolrsg1.cc','''Lowrank decomposition for 1-D isotropic wave propagation. ''')
sfisolrsg1.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolrsg1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolrsg1.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolrsg1.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolrsg1.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolrsg1.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolrsg1.version('1.7')
sfisolrsg1.synopsis('''sfisolrsg1 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolrsg1']=sfisolrsg1

