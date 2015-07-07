sfrtm2d = rsf.doc.rsfprog('sfrtm2d','user/pyang/Mrtm2d.c','''2-D zero-offset reverse-time migration''')
sfrtm2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrtm2d.par('adj',rsf.doc.rsfpar('bool','n','','''if y, migration; else, modeling '''))
sfrtm2d.par('n0',rsf.doc.rsfpar('int','0','','''shot depth in the grid '''))
sfrtm2d.par('nt',rsf.doc.rsfpar('int','','','''number of time steps '''))
sfrtm2d.par('dt',rsf.doc.rsfpar('float','','','''time sampling interval: dt '''))
sfrtm2d.version('1.7')
sfrtm2d.synopsis('''sfrtm2d vel=modl.rsf < data.rsf > imag.rsf adj=n n0=0 nt= dt=''',''' ''')
rsf.doc.progs['sfrtm2d']=sfrtm2d

