sfreg2tri = rsf.doc.rsfprog('sfreg2tri','system/generic/Mreg2tri.c','''Decimate a regular grid to triplets for triangulation. ''')
sfreg2tri.par('edgeout',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfreg2tri.par('nt',rsf.doc.rsfpar('int','','','''number of triplets '''))
sfreg2tri.par('zero',rsf.doc.rsfpar('float','0.','','''level surface '''))
sfreg2tri.par('edgeout',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfreg2tri.version('1.7')
sfreg2tri.synopsis('''sfreg2tri < in.rsf > out.rsf edgeout=edge.rsf nt= zero=0.''','''''')
rsf.doc.progs['sfreg2tri']=sfreg2tri

