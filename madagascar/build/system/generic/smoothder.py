sfsmoothder = rsf.doc.rsfprog('sfsmoothder','system/generic/Msmoothder.c','''Smooth first derivative on the first axis.''')
sfsmoothder.par('eps',rsf.doc.rsfpar('float','0.2','','''smoothness parameter '''))
sfsmoothder.version('1.7')
sfsmoothder.synopsis('''sfsmoothder < in.rsf > der.rsf eps=0.2''','''
Applies D/(I + eps*D'D)
''')
rsf.doc.progs['sfsmoothder']=sfsmoothder

