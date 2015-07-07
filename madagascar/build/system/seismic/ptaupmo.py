sfptaupmo = rsf.doc.rsfprog('sfptaupmo','system/seismic/Mptaupmo.c','''Slope-based tau-p moveout. ''')
sfptaupmo.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo.par('dipt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmo.par('vel2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfptaupmo.par('v0',rsf.doc.rsfpar('float','0.','','''initial velocity '''))
sfptaupmo.par('type',rsf.doc.rsfpar('string ',desc='''transform type '''))
sfptaupmo.version('1.7')
sfptaupmo.synopsis('''sfptaupmo < inp.rsf dip=dip.rsf dipt=dipt.rsf > nmod.rsf vel2=vel2.rsf eps=0.01 v0=0. type=''','''''')
rsf.doc.progs['sfptaupmo']=sfptaupmo

