sfaliasp = rsf.doc.rsfprog('sfaliasp','system/generic/Maliasp.c','''Aliasing test. ''')
sfaliasp.par('n1',rsf.doc.rsfpar('int','600','',''''''))
sfaliasp.par('n2',rsf.doc.rsfpar('int','24','','''dimensions '''))
sfaliasp.par('cycles',rsf.doc.rsfpar('float','10.','','''wave frequency '''))
sfaliasp.par('ix0',rsf.doc.rsfpar('int','0','','''central trace '''))
sfaliasp.par('slow',rsf.doc.rsfpar('float','0.1','','''slowness '''))
sfaliasp.version('1.7')
sfaliasp.synopsis('''sfaliasp > out.rsf n1=600 n2=24 cycles=10. ix0=0 slow=0.1''','''''')
rsf.doc.progs['sfaliasp']=sfaliasp

