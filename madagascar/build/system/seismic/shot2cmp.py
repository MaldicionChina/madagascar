sfshot2cmp = rsf.doc.rsfprog('sfshot2cmp','system/seismic/Mshot2cmp.c','''Convert shots to CMPs for regular 2-D geometry. ''')
sfshot2cmp.par('mask',rsf.doc.rsfpar('file   ',desc='''auxiliary output file name'''))
sfshot2cmp.par('positive',rsf.doc.rsfpar('bool','y','','''initial offset orientation '''))
sfshot2cmp.par('half',rsf.doc.rsfpar('bool','y','','''if y, the second axis is half-offset instead of full offset'''))
sfshot2cmp.par('mask',rsf.doc.rsfpar('string ',desc='''auxiliary output file name'''))
sfshot2cmp.version('1.7')
sfshot2cmp.synopsis('''sfshot2cmp < in.rsf > out.rsf mask=msk.rsf positive=y half=y''','''
The axes in the input are {time,offset,shot}
The axes in the output are {time,offset,midpoint}
''')
rsf.doc.progs['sfshot2cmp']=sfshot2cmp

