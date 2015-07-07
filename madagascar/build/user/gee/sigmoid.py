sfsigmoid = rsf.doc.rsfprog('sfsigmoid','user/gee/Msigmoid.c','''2-D synthetic model from J.F.Claerbout. ''')
sfsigmoid.par('n1',rsf.doc.rsfpar('int','400','','''vertical axis '''))
sfsigmoid.par('n2',rsf.doc.rsfpar('int','100','','''horizontal axis '''))
sfsigmoid.par('large',rsf.doc.rsfpar('int','5*n1','','''reflectivity series '''))
sfsigmoid.par('o1',rsf.doc.rsfpar('float','0.','',''''''))
sfsigmoid.par('o2',rsf.doc.rsfpar('float','0.','',''''''))
sfsigmoid.par('d1',rsf.doc.rsfpar('float','0.004','',''''''))
sfsigmoid.par('d2',rsf.doc.rsfpar('float','0.032','',''''''))
sfsigmoid.par('taper',rsf.doc.rsfpar('bool','y','','''if taper the edges '''))
sfsigmoid.version('1.7 Msigmoid.c 13370 2014-10-09 03:00:06Z sfomel')
sfsigmoid.synopsis('''sfsigmoid > mod.rsf n1=400 n2=100 large=5*n1 o1=0. o2=0. d1=0.004 d2=0.032 taper=y''','''
October 2014 program of the month:
http://ahay.org//rsflog/index.php?/archives/404-Program-of-the-month-sfsigmoid.html
''')
rsf.doc.progs['sfsigmoid']=sfsigmoid

