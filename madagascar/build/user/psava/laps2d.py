sflaps2d = rsf.doc.rsfprog('sflaps2d','user/psava/Mlaps2d.c','''OpenMP lagged-products in the time-domain ''')
sflaps2d.par('ur',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflaps2d.par('cc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sflaps2d.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sflaps2d.par('buf',rsf.doc.rsfpar('bool','n','',''''''))
sflaps2d.par('nhz',rsf.doc.rsfpar('int','0','','''number of lags on the z axis '''))
sflaps2d.par('nhx',rsf.doc.rsfpar('int','0','','''number of lags on the x axis '''))
sflaps2d.par('nht',rsf.doc.rsfpar('int','0','','''number of lags on the t axis '''))
sflaps2d.version('1.7')
sflaps2d.synopsis('''sflaps2d < Fs.rsf ur=Fr.rsf cc=Fc.rsf > Fi.rsf verb=n buf=n nhz=0 nhx=0 nht=0''','''''')
rsf.doc.progs['sflaps2d']=sflaps2d

