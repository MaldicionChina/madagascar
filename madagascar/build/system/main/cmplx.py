sfcmplx = rsf.doc.rsfprog('sfcmplx','system/main/cmplx.c','''Create a complex dataset from its real and imaginary parts.''')
sfcmplx.weblink('http://ahay.org/wiki/Guide_to_madagascar_programs#sfcmplx')
sfcmplx.version('1.7')
sfcmplx.synopsis('''sfcmplx < real.rsf > cmplx.rsf real.rsf imag.rsf''','''There has to be only two input files specified and no additional parameters.
''')
rsf.doc.progs['sfcmplx']=sfcmplx

