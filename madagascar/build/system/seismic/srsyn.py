sfsrsyn = rsf.doc.rsfprog('sfsrsyn','system/seismic/Msrsyn.c','''Synthesize shot/receiver wavefields for 3-D SR migration ''')
sfsrsyn.par('wav',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsrsyn.par('swf',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsrsyn.par('nx',rsf.doc.rsfpar('int','','','''x samples '''))
sfsrsyn.par('dx',rsf.doc.rsfpar('float','','','''x sampling '''))
sfsrsyn.par('ox',rsf.doc.rsfpar('float','','','''x origin '''))
sfsrsyn.par('ny',rsf.doc.rsfpar('int','1','','''y samples '''))
sfsrsyn.par('dy',rsf.doc.rsfpar('float','1','','''y sampling '''))
sfsrsyn.par('oy',rsf.doc.rsfpar('float','0','','''y origin '''))
sfsrsyn.version('1.7')
sfsrsyn.synopsis('''sfsrsyn < Fr.rsf wav=Fs.rsf swf=Fsw.rsf > Frw.rsf nx= dx= ox= ny=1 dy=1 oy=0''','''''')
rsf.doc.progs['sfsrsyn']=sfsrsyn

