sfextract = rsf.doc.rsfprog('sfextract','system/generic/Mextract.c','''Forward interpolation in 2-D slices. ''')
sfextract.par('head',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfextract.par('xkey',rsf.doc.rsfpar('int','0','','''x key number '''))
sfextract.par('ykey',rsf.doc.rsfpar('int','1','','''y key number '''))
sfextract.par('interp',rsf.doc.rsfpar('int','2','[1,2]','''interpolation method, 1: nearest neighbor, 2: bi-linear '''))
sfextract.version('1.7 Mextract.c 7107 2011-04-10 02:04:14Z ivlad')
sfextract.synopsis('''sfextract < in.rsf > out.rsf head=head.rsf xkey=0 ykey=1 interp=2''','''''')
rsf.doc.progs['sfextract']=sfextract

