sfmap2coh = rsf.doc.rsfprog('sfmap2coh','system/seismic/Mmap2coh.c','''From parameter's attribute map (veltran) to coherency-like plots. ''')
sfmap2coh.par('map',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfmap2coh.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfmap2coh.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfmap2coh.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfmap2coh.par('min2',rsf.doc.rsfpar('float','o2','','''min2 '''))
sfmap2coh.par('max2',rsf.doc.rsfpar('float','o2+d2*(n2-1)','','''max2 '''))
sfmap2coh.par('nw',rsf.doc.rsfpar('int','4','','''interpolator size (2,3,4,6,8) '''))
sfmap2coh.par('map',rsf.doc.rsfpar('string ',desc='''parameters map (auxiliary input file name)'''))
sfmap2coh.version('1.7')
sfmap2coh.synopsis('''sfmap2coh < cmp.rsf map=map.rsf > coh.rsf nv= v0= dv= min2=o2 max2=o2+d2*(n2-1) nw=4''','''   (eventually masked) ''')
rsf.doc.progs['sfmap2coh']=sfmap2coh

