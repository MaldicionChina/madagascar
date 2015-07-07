sfblend = rsf.doc.rsfprog('sfblend','user/chenyk/Mblend.c','''Seismic blending operator.''')
sfblend.par('verbose',rsf.doc.rsfpar('int','1','','''0 terse, 1 informative, 2 chatty, 3 debug '''))
sfblend.par('shot_time_in',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.par('shot_time_out',rsf.doc.rsfpar('string ',desc=''''''))
sfblend.version('1.7')
sfblend.synopsis('''sfblend < in.rsf > out.rsf verbose=1 shot_time_in= shot_time_out=''',''' Custom program to blend the seismic data.
''')
rsf.doc.progs['sfblend']=sfblend

