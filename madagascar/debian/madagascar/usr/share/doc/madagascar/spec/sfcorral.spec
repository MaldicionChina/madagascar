[sfcorral]
Cat:    RSF/user/rickettj
Desc:   Cross-correlate every trace with every other in frequency domain
DocCmd: sfcorral | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp data)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  nlags int  -  100 		number of lags 

