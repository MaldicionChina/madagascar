sfisolr3 = rsf.doc.rsfprog('sfisolr3','user/fomels/Misolr3.cc','''Lowrank decomposition for 3-D isotropic wave propagation. ''')
sfisolr3.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfisolr3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfisolr3.par('seed',rsf.doc.rsfpar('','time(NULL','',''''''))
sfisolr3.par('eps',rsf.doc.rsfpar('','1.e-4','','''tolerance'''))
sfisolr3.par('npk',rsf.doc.rsfpar('','20','','''maximum rank'''))
sfisolr3.par('dt',rsf.doc.rsfpar('','','','''time step'''))
sfisolr3.version('1.7')
sfisolr3.synopsis('''sfisolr3 < vel.rsf fft=fft.rsf left=left.rsf > right.rsf seed=time(NULL eps=1.e-4 npk=20 dt=''','''''')
rsf.doc.progs['sfisolr3']=sfisolr3

