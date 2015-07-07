sfpmig = rsf.doc.rsfprog('sfpmig','system/seismic/Mpmig.c','''Slope-based prestack time migration. ''')
sfpmig.par('xdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig.par('hdip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpmig.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpmig.par('mzo',rsf.doc.rsfpar('bool','n','','''do migration to zero offset '''))
sfpmig.par('eps',rsf.doc.rsfpar('float','1.0','','''stretch regularization '''))
sfpmig.version('1.7')
sfpmig.synopsis('''sfpmig < cmp.rsf xdip=xdip.rsf hdip=hdip.rsf > mig.rsf half=y mzo=n eps=1.0''','''''')
rsf.doc.progs['sfpmig']=sfpmig

