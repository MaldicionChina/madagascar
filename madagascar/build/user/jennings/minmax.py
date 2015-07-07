sfminmax = rsf.doc.rsfprog('sfminmax','user/jennings/Mminmax.c','''Element by element minimum or maximum of two RSF files.''')
sfminmax.par('file1',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfminmax.par('file2',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfminmax.par('file1',rsf.doc.rsfpar('string ',desc='''RSF filename required, data type must be float (auxiliary input file name)'''))
sfminmax.par('file2',rsf.doc.rsfpar('string ',desc='''RSF filename required, data type must be float (auxiliary input file name)'''))
sfminmax.par('mode',rsf.doc.rsfpar('string ',desc=''''min' (default) or 'max' '''))
sfminmax.version('1.7 Mminmax.c 4796 2009-09-29 19:39:07Z ivlad')
sfminmax.synopsis('''sfminmax file1=file1.rsf file2=file2.rsf > out.rsf mode=''','''
file1 and file2 must have the same number of elements.

See also: sflistminmax, sfstack.
''')
rsf.doc.progs['sfminmax']=sfminmax

