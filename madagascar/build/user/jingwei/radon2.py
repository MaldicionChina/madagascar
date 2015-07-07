sfradon2 = rsf.doc.rsfprog('sfradon2','user/jingwei/Mradon2.cc','''2to2 Radon transform (using 2to2 butterfly)''')
sfradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon2.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon2.version('1.7')
sfradon2.synopsis('''sfradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp= N=''','''''')
rsf.doc.progs['sfradon2']=sfradon2

