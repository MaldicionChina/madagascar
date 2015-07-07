sfitaupmo = rsf.doc.rsfprog('sfitaupmo','system/seismic/Mitaupmo.c','''Inverse normal moveout in tau-p domain. ''')
sfitaupmo.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfitaupmo.par('interval',rsf.doc.rsfpar('bool','y','','''use interval velocity '''))
sfitaupmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfitaupmo.par('eta',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfitaupmo.version('1.7')
sfitaupmo.synopsis('''sfitaupmo < cmp.rsf velocity=velocity.rsf > nmod.rsf eta=eta.rsf interval=y eps=0.01''','''''')
rsf.doc.progs['sfitaupmo']=sfitaupmo

