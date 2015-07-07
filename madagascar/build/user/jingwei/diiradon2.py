sfdiiradon2 = rsf.doc.rsfprog('sfdiiradon2','user/jingwei/Mdiiradon2.cc','''direct 2to2 hyper Radon transform (double integral, exact)''')
sfdiiradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiiradon2.version('1.7')
sfdiiradon2.synopsis('''sfdiiradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiiradon2']=sfdiiradon2

