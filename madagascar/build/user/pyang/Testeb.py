sfTesteb = rsf.doc.rsfprog('sfTesteb','user/pyang/MTesteb.c','''Demo for effective boundary saving in regular grid''')
sfTesteb.par('back',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfTesteb.par('nb',rsf.doc.rsfpar('int','20','','''thickness of sponge ABC '''))
sfTesteb.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfTesteb.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval '''))
sfTesteb.par('fm',rsf.doc.rsfpar('float','20.0','','''dominant freq of Ricker wavelet '''))
sfTesteb.par('ft',rsf.doc.rsfpar('int','0','','''first recorded time '''))
sfTesteb.par('jt',rsf.doc.rsfpar('int','1','','''time interval '''))
sfTesteb.par('ns',rsf.doc.rsfpar('int','1','','''number of shots '''))
sfTesteb.par('ng',rsf.doc.rsfpar('int','nx','','''number of receivers '''))
sfTesteb.version('1.7')
sfTesteb.synopsis('''sfTesteb < Fv.rsf > Fw1.rsf back=Fw2.rsf nb=20 nt= dt= fm=20.0 ft=0 jt=1 ns=1 ng=nx''','''The sponge absorbing boundary condition is applied for simplicity!
2N-order FD: effective boundary needs N points on each side!
Note: In this demo, 2N=4 (N=2). 
 ''')
rsf.doc.progs['sfTesteb']=sfTesteb

