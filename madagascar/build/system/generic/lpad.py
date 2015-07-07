sflpad = rsf.doc.rsfprog('sflpad','system/generic/Mlpad.c','''Pad and interleave traces.''')
sflpad.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sflpad.par('jump',rsf.doc.rsfpar('int','2','','''aliasing '''))
sflpad.version('1.7')
sflpad.synopsis('''sflpad < in.rsf > out.rsf mask=mask.rsf jump=2''','''
Each initial trace is followed by "jump" zero traces, the same for planes.

March 2014 program of the month:
http://ahay.org/rsflog/index.php?/archives/377-Program-of-the-math-sflpad.html
''')
rsf.doc.progs['sflpad']=sflpad

