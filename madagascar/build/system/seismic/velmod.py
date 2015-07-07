sfvelmod = rsf.doc.rsfprog('sfvelmod','system/seismic/Mvelmod.c','''Velocity transform.''')
sfvelmod.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfvelmod.par('extend',rsf.doc.rsfpar('int','4','','''trace extension '''))
sfvelmod.par('slowness',rsf.doc.rsfpar('bool','n','','''if y, use slowness instead of velocity '''))
sfvelmod.version('1.7')
sfvelmod.synopsis('''sfvelmod < scan.rsf > cmp.rsf half=y extend=4 slowness=n''','''
Inverse of sfvscan.
''')
rsf.doc.progs['sfvelmod']=sfvelmod

