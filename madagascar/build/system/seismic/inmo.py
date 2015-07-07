sfinmo = rsf.doc.rsfprog('sfinmo','system/seismic/Minmo.c','''Inverse normal moveout. ''')
sfinmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfinmo.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfinmo.par('h0',rsf.doc.rsfpar('float','0.','','''reference offset '''))
sfinmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfinmo.version('1.7 Minmo.c 7107 2011-04-10 02:04:14Z ivlad')
sfinmo.synopsis('''sfinmo < cmp.rsf velocity=velocity.rsf > nmod.rsf offset=offset.rsf half=y slowness=n h0=0. eps=0.01''','''''')
rsf.doc.progs['sfinmo']=sfinmo

