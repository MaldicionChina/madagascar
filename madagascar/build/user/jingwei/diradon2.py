sfdiradon2 = rsf.doc.rsfprog('sfdiradon2','user/jingwei/Mdiradon2.cc','''direct 2to2 hyper Radon transform (single integral, nearest point interpolation)''')
sfdiradon2.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon2.version('1.7')
sfdiradon2.synopsis('''sfdiradon2 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiradon2']=sfdiradon2

