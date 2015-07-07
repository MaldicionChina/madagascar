sfmigsteep3 = rsf.doc.rsfprog('sfmigsteep3','system/seismic/Mmigsteep3.c','''3-D Kirchhoff time migration for antialiased steep dips. ''')
sfmigsteep3.par('hdr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmigsteep3.par('n2',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('d2',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('o2',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('n3',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('d3',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('o3',rsf.doc.rsfpar('float','','',''''''))
sfmigsteep3.par('n1',rsf.doc.rsfpar('int','','',''''''))
sfmigsteep3.par('vel',rsf.doc.rsfpar('float','','','''migration velocity '''))
sfmigsteep3.version('1.7')
sfmigsteep3.synopsis('''sfmigsteep3 < in.rsf hdr=head.rsf > mig.rsf n2= d2= o2= n3= d3= o3= n1= vel=''','''
Combine with sfmig3 antialias=flat for the complete response.
''')
rsf.doc.progs['sfmigsteep3']=sfmigsteep3

