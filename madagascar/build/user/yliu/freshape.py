sffreshape = rsf.doc.rsfprog('sffreshape','user/yliu/Mfreshape.c','''Nonstationary spectral balancing in frequency domain. ''')
sffreshape.par('in2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('ma2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sffreshape.par('out2',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sffreshape.par('dim',rsf.doc.rsfpar('int','1','','''data dimensionality '''))
sffreshape.par('in2',rsf.doc.rsfpar('string ',desc='''optional second input file (auxiliary input file name)'''))
sffreshape.version('1.7 Mfreshape.c 7107 2011-04-10 02:04:14Z ivlad')
sffreshape.synopsis('''sffreshape < in.rsf in2=in2.rsf ma=ma.rsf ma2=ma2.rsf > out.rsf out2=out2.rsf dim=1''','''''')
rsf.doc.progs['sffreshape']=sffreshape

