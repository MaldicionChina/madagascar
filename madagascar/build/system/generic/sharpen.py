sfsharpen = rsf.doc.rsfprog('sfsharpen','system/generic/Msharpen.c','''Sharpening operator ''')
sfsharpen.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsharpen.par('perc',rsf.doc.rsfpar('float','50.0','','''percentage for sharpening '''))
sfsharpen.par('other',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsharpen.par('other',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsharpen.version('1.7')
sfsharpen.synopsis('''sfsharpen < in.rsf > out.rsf other=other.rsf perc=50.0''','''''')
rsf.doc.progs['sfsharpen']=sfsharpen

