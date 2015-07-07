sfwei = rsf.doc.rsfprog('sfwei','user/psava/Mwei.c','''3-D modeling/migration with extended SSF ''')
sfwei.par('slo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwei.par('dat',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwei.par('coo',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfwei.par('cip',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfwei.par('verb',rsf.doc.rsfpar('bool','n','','''verbosity flag '''))
sfwei.par('causal',rsf.doc.rsfpar('bool','n','','''causality '''))
sfwei.par('causal',rsf.doc.rsfpar('bool','n','','''causality '''))
sfwei.par('irun',rsf.doc.rsfpar('string ',desc=''''''))
sfwei.version('1.7')
sfwei.synopsis('''sfwei slo=Fslo.rsf < Fsou.rsf dat=Frec.rsf > Fcic.rsf coo=Fcoo.rsf cip=Feic.rsf > Fwfl.rsf verb=n causal=n causal=n irun=''','''''')
rsf.doc.progs['sfwei']=sfwei

