sfinmo3 = rsf.doc.rsfprog('sfinmo3','system/seismic/Minmo3.c','''3-D Inverse normal moveout.''')
sfinmo3.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfinmo3.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3.version('1.7')
sfinmo3.synopsis('''sfinmo3 < cmp.rsf > nmod.rsf velocity=vel.rsf half=y eps=0.01 extend=8''','''
velocity file contains slowness squared with n2=3 (wx,wy,wxy)
''')
rsf.doc.progs['sfinmo3']=sfinmo3

