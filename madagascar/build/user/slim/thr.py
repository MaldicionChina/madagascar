sfthr = rsf.doc.rsfprog('sfthr','user/slim/Mthr.c','''Threshold float/complex inputs given a constant/varying threshold level.''')
sfthr.par('fthr',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfthr.par('thr',rsf.doc.rsfpar('float','','','''threshold level (positive number) '''))
sfthr.par('fthr',rsf.doc.rsfpar('string ',desc='''varying threshold level (positive number) (auxiliary input file name)'''))
sfthr.par('mode',rsf.doc.rsfpar('string ',desc=''''soft', 'hard', 'nng' (default: soft)'''))
sfthr.version('1.7')
sfthr.synopsis('''sfthr < in.rsf > out.rsf fthr=fthr.rsf thr= mode=''','''
Methods available:
- soft
- hard
- non-negative Garrote (nng)

Written by: Gilles Hennenfent & Colin Russell, UBC
Created: February 2006
''')
rsf.doc.progs['sfthr']=sfthr

