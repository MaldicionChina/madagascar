sfdecon = rsf.doc.rsfprog('sfdecon','user/gee/Mdecon.c','''Deconvolution (N-dimensional).''')
sfdecon.par('filt',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfdecon.par('predictive',rsf.doc.rsfpar('bool','n','','''if y, do predictive deconvolution '''))
sfdecon.par('rect1',rsf.doc.rsfpar('int','0','','''smoothing in the first axis '''))
sfdecon.par('lag',rsf.doc.rsfpar('string ',desc=''''''))
sfdecon.version('1.7 Mdecon.c 6681 2010-10-09 15:27:28Z sfomel')
sfdecon.synopsis('''sfdecon < in.rsf > out.rsf filt=filt.rsf predictive=n rect1=0 lag=''','''
Uses the helix and patching technology.
''')
rsf.doc.progs['sfdecon']=sfdecon

