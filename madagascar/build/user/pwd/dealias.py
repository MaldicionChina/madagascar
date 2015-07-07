sfdealias = rsf.doc.rsfprog('sfdealias','user/pwd/Mdealias.c','''3-D trace interpolation to a denser grid using PWD.''')
sfdealias.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdealias.par('both',rsf.doc.rsfpar('bool','n','','''if use left and right slopes '''))
sfdealias.par('eps',rsf.doc.rsfpar('float','0.01','','''regularization '''))
sfdealias.par('order',rsf.doc.rsfpar('int','1','','''accuracy order '''))
sfdealias.version('1.7 Mdealias2.c 1713 2006-03-03 08:21:29Z fomels')
sfdealias.synopsis('''sfdealias < in.rsf > out.rsf dip=dip.rsf both=n eps=0.01 order=1''','''
It may be necessary to bandpass the data before and after dealiasing 
to ensure that the temporal spectrum is banded. Rule of thumb: if 
max(jx,jy)=N, the temporal bandwidth should be 1/N of Nyquist.
''')
rsf.doc.progs['sfdealias']=sfdealias

