[sfthr]
Cat:    RSF/user/slim
Desc:   Threshold float/complex inputs given a constant/varying threshold level
DocCmd: sfthr | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  fthr string  -   -  		varying threshold level (positive number) (auxiliary input file name)
Param:  mode string  -   -  		'soft', 'hard', 'nng' (default: soft)
Param:  thr float  -   -  		threshold level (positive number) 

