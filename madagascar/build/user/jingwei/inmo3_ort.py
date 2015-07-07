sfinmo3_ort = rsf.doc.rsfprog('sfinmo3_ort','user/jingwei/Minmo3_ort.c','''3-D Inverse normal moveout using orthogonal parametrization''')
sfinmo3_ort.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfinmo3_ort.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfinmo3_ort.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfinmo3_ort.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfinmo3_ort.version('1.7')
sfinmo3_ort.synopsis('''sfinmo3_ort < cmp.rsf > nmod.rsf velocity=vel.rsf half=y eps=0.01 extend=8''','''
velocity file contains slowness squared with n2=3 (Wavg,Wcos,Wsin)
''')
rsf.doc.progs['sfinmo3_ort']=sfinmo3_ort

