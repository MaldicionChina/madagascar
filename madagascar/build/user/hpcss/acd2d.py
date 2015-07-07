sfacd2d = rsf.doc.rsfprog('sfacd2d','user/hpcss/Macd2d.c','''time-domain acoustic FD modeling ''')
sfacd2d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfacd2d.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfacd2d.par('verb',rsf.doc.rsfpar('bool','n','','''setup I/O files '''))
sfacd2d.version('1.7')
sfacd2d.synopsis('''sfacd2d < Fw.rsf > Fo.rsf vel=Fv.rsf ref=Fr.rsf verb=n''','''''')
rsf.doc.progs['sfacd2d']=sfacd2d

