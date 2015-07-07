sforp = rsf.doc.rsfprog('sforp','user/songxl/Morp.c','''2-D 10th-order Finite-difference dispersion''')
sforp.par('vx',rsf.doc.rsfpar('float','2.1','',''''''))
sforp.par('vy',rsf.doc.rsfpar('float','2.05','',''''''))
sforp.par('vz',rsf.doc.rsfpar('float','2.0','',''''''))
sforp.par('e1',rsf.doc.rsfpar('float','0.3','',''''''))
sforp.par('e2',rsf.doc.rsfpar('float','0.1','',''''''))
sforp.par('e3',rsf.doc.rsfpar('float','1.0','',''''''))
sforp.par('phi',rsf.doc.rsfpar('float','45.0','',''''''))
sforp.version('1.7')
sforp.synopsis('''sforp > out.rsf < vel.rsf vx=2.1 vy=2.05 vz=2.0 e1=0.3 e2=0.1 e3=1.0 phi=45.0''','''''')
rsf.doc.progs['sforp']=sforp

