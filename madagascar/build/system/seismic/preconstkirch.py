sfpreconstkirch = rsf.doc.rsfprog('sfpreconstkirch','system/seismic/Mpreconstkirch.c','''Prestack Kirchhoff modeling/migration in constant velocity. ''')
sfpreconstkirch.par('inv',rsf.doc.rsfpar('bool','n','','''if y, modeling; if n, migration '''))
sfpreconstkirch.par('zero',rsf.doc.rsfpar('bool','n','','''if y, stack in migration '''))
sfpreconstkirch.par('aal',rsf.doc.rsfpar('bool','y','','''if y, apply antialiasing '''))
sfpreconstkirch.par('nh',rsf.doc.rsfpar('int','','','''number of offsets '''))
sfpreconstkirch.par('dh',rsf.doc.rsfpar('float','','','''offset sampling '''))
sfpreconstkirch.par('h0',rsf.doc.rsfpar('float','','','''offset origin '''))
sfpreconstkirch.par('vel',rsf.doc.rsfpar('float','','','''velocity '''))
sfpreconstkirch.version('1.7')
sfpreconstkirch.synopsis('''sfpreconstkirch < in.rsf > out.rsf inv=n zero=n aal=y nh= dh= h0= vel=''','''
Requires the input to be in (time,cmp x,cmp y,offset)
''')
rsf.doc.progs['sfpreconstkirch']=sfpreconstkirch

