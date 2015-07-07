sfadiradon2 = rsf.doc.rsfprog('sfadiradon2','user/jingwei/Madiradon2.cc','''direct adjoint 2to2 hyper Radon transform (single integral, nearest point interpolation)''')
sfadiradon2.par('nt',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('nx',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('t0',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('dt',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('x0',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.par('dx',rsf.doc.rsfpar('','','',''''''))
sfadiradon2.version('1.7')
sfadiradon2.synopsis('''sfadiradon2 < input.rsf > output.rsf nt= nx= t0= dt= x0= dx=''','''''')
rsf.doc.progs['sfadiradon2']=sfadiradon2

