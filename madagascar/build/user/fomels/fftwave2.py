sffftwave2 = rsf.doc.rsfprog('sffftwave2','user/fomels/Mfftwave2.c','''Simple 2-D wave propagation ''')
sffftwave2.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffftwave2.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffftwave2.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sffftwave2.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sffftwave2.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sffftwave2.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sffftwave2.version('1.7')
sffftwave2.synopsis('''sffftwave2 < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf verb=n snap=0 cmplx=n pad1=1''','''''')
rsf.doc.progs['sffftwave2']=sffftwave2

