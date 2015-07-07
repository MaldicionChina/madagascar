sfunif2 = rsf.doc.rsfprog('sfunif2','system/generic/Munif2.c','''Generate 2-D layered velocity model from specified interfaces. ''')
sfunif2.par('x0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('z0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('v00',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('dvdx',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('dvdz',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif2.par('n1',rsf.doc.rsfpar('int','','','''Number of samples on the depth axis '''))
sfunif2.par('d1',rsf.doc.rsfpar('float','','','''Sampling of the depth axis '''))
sfunif2.par('o1',rsf.doc.rsfpar('float','0.','','''Origin of the depth axis '''))
sfunif2.par('label1',rsf.doc.rsfpar('string ',desc='''depth axis label '''))
sfunif2.par('unit1',rsf.doc.rsfpar('string ',desc=''''''))
sfunif2.version('1.7')
sfunif2.synopsis('''sfunif2 < surface.rsf > model.rsf x0= z0= v00= dvdx= dvdz= n1= d1= o1=0. label1= unit1=''','''
In each layer, velocity is a linear function of position.

Inspired by SU's unif2.

October 2013 program of the month:
http://ahay.org/rsflog/index.php?/archives/359-Program-of-the-month-sfunif2.html
''')
rsf.doc.progs['sfunif2']=sfunif2

