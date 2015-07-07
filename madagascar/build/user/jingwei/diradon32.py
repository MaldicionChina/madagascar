sfdiradon32 = rsf.doc.rsfprog('sfdiradon32','user/jingwei/Mdiradon32.cc','''direct azimuthally isotropic 3to2 hyper Radon transform''')
sfdiradon32.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('np',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('p0',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.par('dp',rsf.doc.rsfpar('','','',''''''))
sfdiradon32.version('1.7')
sfdiradon32.synopsis('''sfdiradon32 < input.rsf > output.rsf ntau= np= tau0= dtau= p0= dp=''','''''')
rsf.doc.progs['sfdiradon32']=sfdiradon32

