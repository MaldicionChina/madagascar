sfprekirch = rsf.doc.rsfprog('sfprekirch','user/chenyk/Mprekirch.c','''2-D Prestack Kirchhoff time migration with antialiasing. ''')
sfprekirch.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfprekirch.par('nz',rsf.doc.rsfpar('int','nt','',''''''))
sfprekirch.par('dz',rsf.doc.rsfpar('float','dt','',''''''))
sfprekirch.par('z0',rsf.doc.rsfpar('float','t0','',''''''))
sfprekirch.par('antialias',rsf.doc.rsfpar('float','1.0','','''antialiasing '''))
sfprekirch.version('1.7')
sfprekirch.synopsis('''sfprekirch < inp.rsf vel=vel.rsf > mig.rsf nz=nt dz=dt z0=t0 antialias=1.0''','''The axes in the input are {time,midpoint,offset}
The axes in the output are {time,midpoint}
''')
rsf.doc.progs['sfprekirch']=sfprekirch

