import rsf.doc

sfinmo3_ort = rsf.doc.rsfprog('sfinmo3_ort','user/jingwei/Minmo3_ort.c','''3-D Inverse normal moveout using orthogonal parametrization''')
sfinmo3_ort.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3_ort.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfinmo3_ort.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3_ort.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3_ort.version('1.7')
sfinmo3_ort.synopsis('''sfinmo3_ort < cmp.rsf > nmod.rsf velocity=vel.rsf half=y eps=0.01 extend=8''','''
velocity file contains slowness squared with n2=3 (Wavg,Wcos,Wsin)
''')
rsf.doc.progs['sfinmo3_ort']=sfinmo3_ort

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

sfradon34 = rsf.doc.rsfprog('sfradon34','user/jingwei/Mradon34.cc','''azimuthally anisotropic 3to4 Radon transform (using 3to3 butterfly)''')
sfradon34.par('ntau',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('np',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('nq',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('ns',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('tau0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dtau',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('p0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dp',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('q0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('dq',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('s0',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('ds',rsf.doc.rsfpar('','','',''''''))
sfradon34.par('N',rsf.doc.rsfpar('','','','''number of partitions'''))
sfradon34.version('1.7')
sfradon34.synopsis('''sfradon34 < input.rsf > output.rsf ntau= np= nq= ns= tau0= dtau= p0= dp= q0= dq= s0= ds= N=''','''''')
rsf.doc.progs['sfradon34']=sfradon34

sfsum = rsf.doc.rsfprog('sfsum','user/jingwei/Msum.cc','''adjoint test ''')
sfsum.par('input2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input3',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.par('input4',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsum.version('1.7')
sfsum.synopsis('''sfsum < input1.rsf input2=input2.rsf input3=input3.rsf input4=input4.rsf > output.rsf''','''''')
rsf.doc.progs['sfsum']=sfsum

