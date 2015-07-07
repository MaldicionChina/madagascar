sffincon = rsf.doc.rsfprog('sffincon','system/seismic/Mfincon.c','''Offset continuation by finite differences ''')
sffincon.par('nh',rsf.doc.rsfpar('int','','','''Number of steps in offset '''))
sffincon.par('dh',rsf.doc.rsfpar('float','','','''Offset step size '''))
sffincon.par('h0',rsf.doc.rsfpar('float','','','''Initial offset '''))
sffincon.par('all',rsf.doc.rsfpar('bool','n','','''if y, output all offsets '''))
sffincon.version('1.7')
sffincon.synopsis('''sffincon < input.rsf > output.rsf nh= dh= h0= all=n''','''''')
rsf.doc.progs['sffincon']=sffincon

