sfisolr2 = rsf.doc.rsfprog('sfisolr2','user/fomels/Misolr2.cc','''Lowrank decomposition for 2-D isotropic wave propagation. ''')
sfisolr2.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr2.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr2.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr2.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr2.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr2.version('1.7')
sfisolr2.synopsis('''sfisolr2 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr2']=sfisolr2

