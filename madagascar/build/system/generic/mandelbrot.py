sfmandelbrot = rsf.doc.rsfprog('sfmandelbrot','system/generic/Mmandelbrot.c','''Generate Mandelbrot set. ''')
sfmandelbrot.par('n1',rsf.doc.rsfpar('int','512','',''''''))
sfmandelbrot.par('n2',rsf.doc.rsfpar('int','512','','''dimensions '''))
sfmandelbrot.par('x0',rsf.doc.rsfpar('float','-2.','',''''''))
sfmandelbrot.par('y0',rsf.doc.rsfpar('float','-1.','','''set origin '''))
sfmandelbrot.par('xmax',rsf.doc.rsfpar('float','0.5','',''''''))
sfmandelbrot.par('ymax',rsf.doc.rsfpar('float','1.','','''set maximum '''))
sfmandelbrot.par('niter',rsf.doc.rsfpar('int','1000','','''number of iterations '''))
sfmandelbrot.par('dx',rsf.doc.rsfpar('float','(xmax-x0)/(n1-1)','',''''''))
sfmandelbrot.par('dy',rsf.doc.rsfpar('float','(ymax-y0)/(n2-1)','',''''''))
sfmandelbrot.version('1.7')
sfmandelbrot.synopsis('''sfmandelbrot > out.rsf n1=512 n2=512 x0=-2. y0=-1. xmax=0.5 ymax=1. niter=1000 dx=(xmax-x0)/(n1-1) dy=(ymax-y0)/(n2-1)''','''''')
rsf.doc.progs['sfmandelbrot']=sfmandelbrot

