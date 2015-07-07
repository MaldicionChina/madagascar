sfcomp = rsf.doc.rsfprog('sfcomp','user/chen/Mcomp.c','''Compare 2 data set ''')
sfcomp.par('ref',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfcomp.par('mode',rsf.doc.rsfpar('int','0','','''compare method: 
	0 - normalized xcorrelation; 
	1 - mean square error '''))
sfcomp.version('1.7')
sfcomp.synopsis('''sfcomp < in.rsf > out.rsf ref=ref.rsf mode=0''','''''')
rsf.doc.progs['sfcomp']=sfcomp

