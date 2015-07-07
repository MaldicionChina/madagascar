sfptaupmoVTI = rsf.doc.rsfprog('sfptaupmoVTI','system/seismic/MptaupmoVTI.c','''Slope-based tau-p moveout in VTI. ''')
sfptaupmoVTI.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmoVTI.par('ddip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfptaupmoVTI.par('tau0',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmoVTI.par('cos2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfptaupmoVTI.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfptaupmoVTI.par('dip',rsf.doc.rsfpar('string ',desc='''slope field (auxiliary input file name)'''))
sfptaupmoVTI.par('ddip',rsf.doc.rsfpar('string ',desc='''curvature field (auxiliary input file name)'''))
sfptaupmoVTI.par('tau0',rsf.doc.rsfpar('string ',desc='''tau0(tau,p) (auxiliary output file name)'''))
sfptaupmoVTI.version('1.7')
sfptaupmoVTI.synopsis('''sfptaupmoVTI < inp.rsf dip=dip.rsf ddip=ddip.rsf > nmod.rsf tau0=tau0.rsf cos2=cos2.rsf eps=0.01''','''''')
rsf.doc.progs['sfptaupmoVTI']=sfptaupmoVTI

