[sfstft]
Cat:    RSF/user/yliu
Desc:   Short-time Fourier transform (STFT)
DocCmd: sfstft | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  inv enum-bool  -  n 		if y, perform inverse transform 
Param:  ntw int  -  7 		time-window length 
Param:  opt enum-bool  -  y 		if y, determine optimal size for efficiency 
Param:  sym enum-bool  -  n 		if y, apply symmetric scaling to make the FFT operator Hermitian 

