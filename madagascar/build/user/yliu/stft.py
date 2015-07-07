sfstft = rsf.doc.rsfprog('sfstft','user/yliu/Mstft.c','''Short-time Fourier transform (STFT). ''')
sfstft.par('inv',rsf.doc.rsfpar('bool','n','','''if y, perform inverse transform '''))
sfstft.par('sym',rsf.doc.rsfpar('bool','n','','''if y, apply symmetric scaling to make the FFT operator Hermitian '''))
sfstft.par('opt',rsf.doc.rsfpar('bool','y','','''if y, determine optimal size for efficiency '''))
sfstft.par('ntw',rsf.doc.rsfpar('int','7','','''time-window length '''))
sfstft.version('1.7 Mstft.c 7202 2011-05-03 02:13:48Z yang_liu')
sfstft.synopsis('''sfstft < in.rsf > out.rsf inv=n sym=n opt=y ntw=7''','''''')
rsf.doc.progs['sfstft']=sfstft

