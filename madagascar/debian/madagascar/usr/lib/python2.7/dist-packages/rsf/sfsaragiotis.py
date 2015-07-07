import rsf.doc

sfconvft = rsf.doc.rsfprog('sfconvft','user/saragiotis/Mconvft.c','''Trace-by-trace or data-by-trace convolution using Fourier transform. ''')
sfconvft.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvft.par('axis',rsf.doc.rsfpar('int','1','','''across which axis to convolve.'''))
sfconvft.version('1.7')
sfconvft.synopsis('''sfconvft < in.rsf other=other.rsf > conv.rsf axis=1''','''''')
rsf.doc.progs['sfconvft']=sfconvft

sfstackn = rsf.doc.rsfprog('sfstackn','user/saragiotis/Mstackn.c','''Stack prespecified values. ''')
sfstackn.par('min',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstackn.par('max',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfstackn.par('mean',rsf.doc.rsfpar('bool','y','','''if n, sum; if y, average '''))
sfstackn.par('thres',rsf.doc.rsfpar('float','0.','','''threshold (percentage of maxabs) '''))
sfstackn.par('min',rsf.doc.rsfpar('string ',desc='''file determining from which value to stack (auxiliary input file name)'''))
sfstackn.par('max',rsf.doc.rsfpar('string ',desc='''file determining up to which value to stack (auxiliary input file name)'''))
sfstackn.version('1.7')
sfstackn.synopsis('''sfstackn < in.rsf > out.rsf min=minin.rsf max=maxin.rsf mean=y thres=0.''','''''')
rsf.doc.progs['sfstackn']=sfstackn

sfzerocross = rsf.doc.rsfprog('sfzerocross','user/saragiotis/Mzerocross.c','''Zero crossings. ''')
sfzerocross.par('levels',rsf.doc.rsfpar('int','3','','''levels of quantization [2,3,5].
      levels=2	1: zero crossing or zero; 0: otherwise
      levels=3	1: positive to negative zc; -1 negative to positive zc; 0: otherwise
      levels=5	+/-2: positive/negative values; +/-1: as in levels=3; 0: zero. 
    '''))
sfzerocross.version('1.7')
sfzerocross.synopsis('''sfzerocross < in.rsf > out.rsf levels=3''','''''')
rsf.doc.progs['sfzerocross']=sfzerocross

