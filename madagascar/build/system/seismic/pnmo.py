sfpnmo = rsf.doc.rsfprog('sfpnmo','system/seismic/Mpnmo.c','''Slope-based normal moveout. ''')
sfpnmo.par('dip',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('vel',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo.par('offset',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('crv',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfpnmo.par('eta',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfpnmo.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset '''))
sfpnmo.par('eps',rsf.doc.rsfpar('float','0.01','','''stretch regularization '''))
sfpnmo.par('offset',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmo.par('crv',rsf.doc.rsfpar('string ',desc='''auxiliary input file name'''))
sfpnmo.version('1.7 Mpnmo.c 4796 2009-09-29 19:39:07Z ivlad')
sfpnmo.synopsis('''sfpnmo < cmp.rsf dip=dip.rsf > nmod.rsf vel=vel.rsf offset=offset.rsf crv=crv.rsf eta=eta.rsf half=y eps=0.01''','''''')
rsf.doc.progs['sfpnmo']=sfpnmo

