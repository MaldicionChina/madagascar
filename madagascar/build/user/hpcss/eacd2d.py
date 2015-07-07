sfeacd2d = rsf.doc.rsfprog('sfeacd2d','user/hpcss/Meacd2d.c','''Extended time-domain acoustic FD modeling ''')
sfeacd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeacd2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfeacd2d.par('verb',rsf.doc.rsfpar('bool','n','','''setup I/O files '''))
sfeacd2d.version('1.7')
sfeacd2d.synopsis('''sfeacd2d < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=n''','''''')
rsf.doc.progs['sfeacd2d']=sfeacd2d

