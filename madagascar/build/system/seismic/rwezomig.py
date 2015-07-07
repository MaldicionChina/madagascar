sfrwezomig = rsf.doc.rsfprog('sfrwezomig','system/seismic/Mrwezomig.c','''Riemannian Wavefield Extrapolation: zero-offset modeling/migration ''')
sfrwezomig.par('abm',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwezomig.par('abr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfrwezomig.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfrwezomig.par('method',rsf.doc.rsfpar('int','0','','''extrapolation method '''))
sfrwezomig.par('adj',rsf.doc.rsfpar('bool','n','','''y=modeling; n=migration '''))
sfrwezomig.par('nw',rsf.doc.rsfpar('int','','',''''''))
sfrwezomig.par('dw',rsf.doc.rsfpar('float','','',''''''))
sfrwezomig.par('ow',rsf.doc.rsfpar('float','0.','',''''''))
sfrwezomig.version('1.7')
sfrwezomig.synopsis('''sfrwezomig abm=Fm.rsf abr=Fr.rsf < Fi.rsf > Fd.rsf verb=n method=0 adj=n nw= dw= ow=0.''','''''')
rsf.doc.progs['sfrwezomig']=sfrwezomig

