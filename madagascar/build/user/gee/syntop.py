sfsyntop = rsf.doc.rsfprog('sfsyntop','user/gee/Msyntop.c','''Make synthetic topography map. ''')
sfsyntop.par('mod',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsyntop.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfsyntop.par('n1',rsf.doc.rsfpar('int','100','',''''''))
sfsyntop.par('n2',rsf.doc.rsfpar('int','100','','''data dimensions '''))
sfsyntop.version('1.7')
sfsyntop.synopsis('''sfsyntop mod=mod.rsf > syn.rsf mask=mask.rsf n1=100 n2=100''','''''')
rsf.doc.progs['sfsyntop']=sfsyntop

