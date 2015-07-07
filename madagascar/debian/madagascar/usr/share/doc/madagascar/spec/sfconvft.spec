[sfconvft]
Cat:    RSF/user/saragiotis
Desc:   Trace-by-trace or data-by-trace convolution using Fourier transform
DocCmd: sfconvft | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing conv data)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  axis int  -  1 		across which axis to convolve.

