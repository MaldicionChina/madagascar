sfdsreiko0 = rsf.doc.rsfprog('sfdsreiko0','user/llisiw/Mdsreiko0.c','''Double square-root eikonal solver (2D + explicit) ''')
sfdsreiko0.par('velocity',rsf.doc.rsfpar('bool','y','','''if y, the input is velocity; n, slowness squared '''))
sfdsreiko0.version('1.7')
sfdsreiko0.synopsis('''sfdsreiko0 < in.rsf > out.rsf velocity=y''','''''')
rsf.doc.progs['sfdsreiko0']=sfdsreiko0

