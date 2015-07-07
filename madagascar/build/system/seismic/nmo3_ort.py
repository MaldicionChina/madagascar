sfnmo3_ort = rsf.doc.rsfprog('sfnmo3_ort','system/seismic/Mnmo3_ort.c','''3-D Normal moveout using orthogonal parametrization''')
sfnmo3_ort.par('velocity',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3_ort.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfnmo3_ort.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second and third axes are half-offset instead of full offset '''))
sfnmo3_ort.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfnmo3_ort.par('mute',rsf.doc.rsfpar('int','12','','''mute zone '''))
sfnmo3_ort.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfnmo3_ort.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfnmo3_ort.version('1.7')
sfnmo3_ort.synopsis('''sfnmo3_ort < cmp.rsf > nmod.rsf velocity=vel.rsf offset=offset.rsf half=y eps=0.01 mute=12 extend=8''','''
input data has gathers along *4th* axis; 
velocity file contains slowness squared with n2=3 (Wavg,Wcos,Wsin);
offset file contains x,y offset pairs for input data
''')
rsf.doc.progs['sfnmo3_ort']=sfnmo3_ort

