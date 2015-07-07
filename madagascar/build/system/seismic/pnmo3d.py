sfpnmo3d = rsf.doc.rsfprog('sfpnmo3d','system/seismic/Mpnmo3d.c','''Slope-based normal moveout for 3-D CMP geometry. ''')
sfpnmo3d.par('dipx',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo3d.par('dipy',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo3d.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo3d.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpnmo3d.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpnmo3d.par('extend',rsf.doc.rsfpar('int','8','','''trace extension '''))
sfpnmo3d.version('1.7')
sfpnmo3d.synopsis('''sfpnmo3d < cmp.rsf dipx=dipx.rsf dipy=dipy.rsf > nmod.rsf vel=vel.rsf half=y eps=0.01 extend=8''','''''')
rsf.doc.progs['sfpnmo3d']=sfpnmo3d

