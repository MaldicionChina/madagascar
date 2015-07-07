sfsglr1 = rsf.doc.rsfprog('sfsglr1','user/fangg/Msglr1.c','''1-D lowrank wave propagation on staggered grid''')
sfsglr1.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('den',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('rec',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsglr1.par('left',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('right',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('fft',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('ic',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('presrc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('velsrc',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('preinit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('velinit',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsglr1.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity '''))
sfsglr1.par('srcmms',rsf.doc.rsfpar('bool','n','','''use MMS source '''))
sfsglr1.par('slx',rsf.doc.rsfpar('float','','','''source location in x '''))
sfsglr1.par('srcdecay',rsf.doc.rsfpar('bool','y','','''source decay'''))
sfsglr1.par('srcrange',rsf.doc.rsfpar('int','10','','''source decay range'''))
sfsglr1.par('srctrunc',rsf.doc.rsfpar('float','100','','''trunc source after srctrunc time (s)'''))
sfsglr1.par('cmplx',rsf.doc.rsfpar('bool','n','','''use complex FFT '''))
sfsglr1.par('pad1',rsf.doc.rsfpar('int','1','','''padding factor on the first axis '''))
sfsglr1.par('inject',rsf.doc.rsfpar('bool','y','','''=y inject source; =n initial condition'''))
sfsglr1.par('gdep',rsf.doc.rsfpar('float','0.0','','''depth of geophone (meter)'''))
sfsglr1.version('1.7')
sfsglr1.synopsis('''sfsglr1 vel=Fvel.rsf den=Fden.rsf < Fsrc.rsf > Fo.rsf rec=Frec.rsf left=left.rsf right=right.rsf fft=Ffft.rsf ic=Fic.rsf presrc=Fpsrc.rsf velsrc=Fvsrc.rsf preinit=Fpint.rsf velinit=Fvint.rsf verb=n srcmms=n slx= srcdecay=y srcrange=10 srctrunc=100 cmplx=n pad1=1 inject=y gdep=0.0''','''''')
rsf.doc.progs['sfsglr1']=sfsglr1

