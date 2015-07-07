[sfwcorr]
Cat:    RSF/user/gchliu
Desc:   Stack a dataset over the second dimensions by SNR weighted method
DocCmd: sfwcorr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   other rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  eps float  -  0 		stable parameter
Param:  w int  -  50 		size of window

