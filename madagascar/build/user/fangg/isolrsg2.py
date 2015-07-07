sfisolrsg2 = rsf.doc.rsfprog('sfisolrsg2','user/fangg/Misolrsg2.cc','''Lowrank decomposition for 2-D isotropic wave propagation. ''')
sfisolrsg2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolrsg2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolrsg2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolrsg2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolrsg2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolrsg2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolrsg2.version('1.7')
sfisolrsg2.synopsis('''sfisolrsg2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolrsg2']=sfisolrsg2

