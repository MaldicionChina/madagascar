sffftwave3 = rsf.doc.rsfprog('sffftwave3','user/fomels/Mfftwave3.c','''Simple 3-D wave propagation ''')
sffftwave3.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave3.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave3.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sffftwave3.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave3.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave3.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave3.version('1.7')
sffftwave3.synopsis('''sffftwave3 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=y cmplx=n pad1=1 snap=0''','''''')
rsf.doc.progs['sffftwave3']=sffftwave3

