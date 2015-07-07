sfpveltran = rsf.doc.rsfprog('sfpveltran','system/seismic/Mpveltran.c','''Slope-based velocity transform. ''')
sfpveltran.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpveltran.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpveltran.par('nv',rsf.doc.rsfpar('int','','','''number of velocities '''))
sfpveltran.par('v0',rsf.doc.rsfpar('float','','','''velocity origin '''))
sfpveltran.par('dv',rsf.doc.rsfpar('float','','','''velocity sampling '''))
sfpveltran.par('interval',rsf.doc.rsfpar('bool','n','','''if y, compute interval velocity '''))
sfpveltran.par('eps',rsf.doc.rsfpar('float','0.1','','''stretch regularization '''))
sfpveltran.version('1.7')
sfpveltran.synopsis('''sfpveltran < cmp.rsf dip=dip.rsf > vel.rsf dipt=dipt.rsf half=y nv= v0= dv= interval=n eps=0.1''','''''')
rsf.doc.progs['sfpveltran']=sfpveltran

