sfslice = rsf.doc.rsfprog('sfslice','system/generic/Mslice.c','''Extract a slice using picked surface (usually from a stack or a semblance).''')
sfslice.par('pick',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfslice.version('1.7')
sfslice.synopsis('''sfslice < in.rsf pick=pick.rsf > out.rsf''','''
See also: sfpick.
''')
rsf.doc.progs['sfslice']=sfslice

