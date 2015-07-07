sftimefreq = rsf.doc.rsfprog('sftimefreq','user/fomels/Mtimefreq.c','''Time-frequency analysis using local attributes. ''')
sftimefreq.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sftimefreq.par('nw',rsf.doc.rsfpar('int','','','''number of frequencies '''))
sftimefreq.par('dw',rsf.doc.rsfpar('float','','','''f	requency step '''))
sftimefreq.par('w0',rsf.doc.rsfpar('float','0.','','''first frequency '''))
sftimefreq.par('rect',rsf.doc.rsfpar('int','10','','''smoothing radius '''))
sftimefreq.par('niter',rsf.doc.rsfpar('int','100','','''number of inversion iterations '''))
sftimefreq.par('phase',rsf.doc.rsfpar('bool','n','','''output phase instead of amplitude '''))
sftimefreq.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sftimefreq.version('1.7')
sftimefreq.synopsis('''sftimefreq < time.rsf > timefreq.rsf mask=mask.rsf nw= dw= w0=0. rect=10 niter=100 phase=n''','''''')
rsf.doc.progs['sftimefreq']=sftimefreq

