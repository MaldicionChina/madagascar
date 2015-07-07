sfsplit = rsf.doc.rsfprog('sfsplit','user/ivlad/Msplit.py','''Splits file into slices along the last dimension''')
sfsplit.par('verb',rsf.doc.rsfpar('bool','n','',''''''))
sfsplit.par('inp',rsf.doc.rsfpar('string','','','''ifile.rsf'''))
sfsplit.par('outdir',rsf.doc.rsfpar('string','(out_basenm+ivlad.ext','',''''''))
sfsplit.par('nthick',rsf.doc.rsfpar('int','1','','''slice thickness'''))
sfsplit.version('1.7')
sfsplit.synopsis('''sfsplit verb=n inp= outdir=(out_basenm+ivlad.ext nthick=1''','''Usage:

sfsplit inp=file.rsf outdir=[file_split.rsf] nthick=[1]

Parameter nthick gives the maximum thickness of a slice. The last slice may
be thinner.''')
rsf.doc.progs['sfsplit']=sfsplit

