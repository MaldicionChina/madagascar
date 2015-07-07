[sfsnrstack]
Cat:    RSF/user/gchliu
Desc:   Stack a dataset over the second dimensions by SNR weighted method
DocCmd: sfsnrstack | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  ee float  -  1.0 		
Param:  esp float  -  1.0 		
Param:  sft float  -  1 		weight shift
Param:  w int  -  50 		sliding window size

