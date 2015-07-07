sflorenz = rsf.doc.rsfprog('sflorenz','system/generic/Mlorenz.c','''Generate Lorenz attractor. ''')
sflorenz.par('niter',rsf.doc.rsfpar('int','1000','','''number of iterations '''))
sflorenz.par('n',rsf.doc.rsfpar('int','niter','','''set maximum '''))
sflorenz.par('rho',rsf.doc.rsfpar('double','28.00','','''Rayleigh number '''))
sflorenz.par('sigma',rsf.doc.rsfpar('double','10.00','','''Prandtl number '''))
sflorenz.par('beta',rsf.doc.rsfpar('double','8.00/3.00','','''Beta reference '''))
sflorenz.par('x0',rsf.doc.rsfpar('double','3.051522','','''intial x coordinate '''))
sflorenz.par('y0',rsf.doc.rsfpar('double','1.582542','','''intial y coordinate '''))
sflorenz.par('z0',rsf.doc.rsfpar('double','15.62388','','''intial z coordinate '''))
sflorenz.par('dt',rsf.doc.rsfpar('double','0.0001','','''time step '''))
sflorenz.version('1.7 Mlorenz.c 9567 2012-10-29 20:38:18Z sfomel')
sflorenz.synopsis('''sflorenz > out.rsf niter=1000 n=niter rho=28.00 sigma=10.00 beta=8.00/3.00 x0=3.051522 y0=1.582542 z0=15.62388 dt=0.0001''','''''')
rsf.doc.progs['sflorenz']=sflorenz

