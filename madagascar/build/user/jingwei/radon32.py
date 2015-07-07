sfradon32 = rsf.doc.rsfprog('sfradon32','user/jingwei/Mradon32.cc','''azimuthally isotropic 3to2 Radon transform (using 2to2 butterfly)''')
sfradon32.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon32.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon32.version('1.7')
sfradon32.synopsis('''sfradon32 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp= N=''','''''')
rsf.doc.progs['sfradon32']=sfradon32

