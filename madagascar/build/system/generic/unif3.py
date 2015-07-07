sfunif3 = rsf.doc.rsfprog('sfunif3','system/generic/Munif3.c','''Generate 3-D layered velocity model from specified interfaces. ''')
sfunif3.par('x0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('y0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('z0',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('v00',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdx',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdy',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('dvdz',rsf.doc.rsfpar('floats','','',''' [ninf]'''))
sfunif3.par('n1',rsf.doc.rsfpar('int','','','''Number of samples on the depth axis '''))
sfunif3.par('d1',rsf.doc.rsfpar('float','','','''Sampling of the depth axis '''))
sfunif3.par('o1',rsf.doc.rsfpar('float','0.','','''Origin of the depth axis '''))
sfunif3.par('layers',rsf.doc.rsfpar('string ',desc='''file with layer properties '''))
sfunif3.version('1.7 Munif3.c 4796 2009-09-29 19:39:07Z ivlad')
sfunif3.synopsis('''sfunif3 < surface.rsf > model.rsf x0= y0= z0= v00= dvdx= dvdy= dvdz= n1= d1= o1=0. layers=''','''
Unless layers= is specified, velocity is a linear function of position inside
each layer.

Inspired by SU's unif2.
''')
rsf.doc.progs['sfunif3']=sfunif3

