sfsegyheader = rsf.doc.rsfprog('sfsegyheader','system/seismic/Msegyheader.c','''Make a trace header file for segywrite.''')
sfsegyheader.par('tfile',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfsegyheader.par('n1',rsf.doc.rsfpar('int','','','''number of samples in a trace '''))
sfsegyheader.par('d1',rsf.doc.rsfpar('float','','','''trace sampling '''))
sfsegyheader.par('o1',rsf.doc.rsfpar('float','0','','''trace origin '''))
sfsegyheader.par('tfile',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfsegyheader.version('1.7')
sfsegyheader.synopsis('''sfsegyheader < in.rsf > out.rsf tfile=tfile.rsf n1= d1= o1=0''','''
   Use the output for tfile= argument in segywrite.
''')
rsf.doc.progs['sfsegyheader']=sfsegyheader

