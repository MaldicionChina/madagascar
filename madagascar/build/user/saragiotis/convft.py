sfconvft = rsf.doc.rsfprog('sfconvft','user/saragiotis/Mconvft.c','''Trace-by-trace or data-by-trace convolution using Fourier transform. ''')
sfconvft.par('other',rsf.doc.rsfpar('file   ',desc='''auxiliary input file name'''))
sfconvft.par('axis',rsf.doc.rsfpar('int','1','','''across which axis to convolve.'''))
sfconvft.version('1.7')
sfconvft.synopsis('''sfconvft < in.rsf other=other.rsf > conv.rsf axis=1''','''''')
rsf.doc.progs['sfconvft']=sfconvft

