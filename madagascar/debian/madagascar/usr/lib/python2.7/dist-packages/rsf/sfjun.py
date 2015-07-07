import rsf.doc

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

sfvelinvww = rsf.doc.rsfprog('sfvelinvww','user/jun/Mvelinvww.f90','''Inverse velocity spectrum with interpolation by modeling from inversion result''')
sfvelinvww.par('velout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfvelinvww.par('ns',rsf.doc.rsfpar('','nh','',''''''))
sfvelinvww.par('ds',rsf.doc.rsfpar('','0.001','',''''''))
sfvelinvww.par('os',rsf.doc.rsfpar('','0.00000001','',''''''))
sfvelinvww.par('huber',rsf.doc.rsfpar('','0','',''''''))
sfvelinvww.par('irls',rsf.doc.rsfpar('','0','',''''''))
sfvelinvww.par('nstep',rsf.doc.rsfpar('','1','',''''''))
sfvelinvww.par('niter',rsf.doc.rsfpar('','20','',''''''))
sfvelinvww.par('rwt',rsf.doc.rsfpar('','0.','',''''''))
sfvelinvww.par('mwt',rsf.doc.rsfpar('','0.','',''''''))
sfvelinvww.par('srate',rsf.doc.rsfpar('','0.01','',''''''))
sfvelinvww.par('epw',rsf.doc.rsfpar('','0.01','',''''''))
sfvelinvww.par('savevel',rsf.doc.rsfpar('','0','',''''''))
sfvelinvww.version('1.7')
sfvelinvww.synopsis('''sfvelinvww < infile.rsf > outfile.rsf velout=vtr.rsf ns=nh ds=0.001 os=0.00000001 huber=0 irls=0 nstep=1 niter=20 rwt=0. mwt=0. srate=0.01 epw=0.01 savevel=0''','''''')
rsf.doc.progs['sfvelinvww']=sfvelinvww

