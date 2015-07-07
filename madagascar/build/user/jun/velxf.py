sfvelxf = rsf.doc.rsfprog('sfvelxf','user/jun/Mvelxf.f90','''Velocity transform for generating velocity spectra and its corresponding hyperbolic modeling''')
sfvelxf.par('adj',rsf.doc.rsfpar('','0','','''adj = 0  : from velocity-domain(t,s) to cmp-gather(t,x)'''))
sfvelxf.par('nx',rsf.doc.rsfpar('','ns','',''''''))
sfvelxf.par('dx',rsf.doc.rsfpar('','10.','',''''''))
sfvelxf.par('ox',rsf.doc.rsfpar('','0.','',''''''))
sfvelxf.par('ns',rsf.doc.rsfpar('','nx','',''''''))
sfvelxf.par('ds',rsf.doc.rsfpar('','0.001','',''''''))
sfvelxf.par('os',rsf.doc.rsfpar('','0.00000001','',''''''))
sfvelxf.version('1.7')
sfvelxf.synopsis('''sfvelxf < vtr.rsf < cmp.rsf adj=0 nx=ns dx=10. ox=0. ns=nx ds=0.001 os=0.00000001''','''''')
rsf.doc.progs['sfvelxf']=sfvelxf

