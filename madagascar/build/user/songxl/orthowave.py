sforthowave = rsf.doc.rsfprog('sforthowave','user/songxl/Morthowave.c','''Simple 3-D wave propagation ''')
sforthowave.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sforthowave.par('snaps',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sforthowave.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sforthowave.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sforthowave.par('mid',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sforthowave.par('verb',rsf.doc.rsfpar('bool','y','','''verbosity '''))
sforthowave.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sforthowave.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sforthowave.par('snap',rsf.doc.rsfpar('int','0','','''interval for snapshots '''))
sforthowave.version('1.7')
sforthowave.synopsis('''sforthowave < Fw.rsf > Fo.rsf ref=Fr.rsf snaps=snaps.rsf left=left.rsf right=right.rsf mid=mid.rsf verb=y cmplx=n pad1=1 snap=0''','''''')
rsf.doc.progs['sforthowave']=sforthowave

