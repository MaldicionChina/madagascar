sfrweab = rsf.doc.rsfprog('sfrweab','system/seismic/Mrweab.c','''Riemannian Wavefield Extrapolation: a,b coefficients ''')
sfrweab.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrweab.par('abr',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfrweab.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrweab.par('naref',rsf.doc.rsfpar('int','1','',''''''))
sfrweab.par('nbref',rsf.doc.rsfpar('int','1','',''''''))
sfrweab.par('peps',rsf.doc.rsfpar('float','0.01','',''''''))
sfrweab.version('1.7')
sfrweab.synopsis('''sfrweab < Fi.rsf slo=Fs.rsf > Fo.rsf abr=Fr.rsf verb=n naref=1 nbref=1 peps=0.01''','''''')
rsf.doc.progs['sfrweab']=sfrweab

