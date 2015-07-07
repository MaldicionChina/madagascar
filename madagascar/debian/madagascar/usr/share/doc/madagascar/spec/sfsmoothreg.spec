[sfsmoothreg]
Cat:    RSF/user/fomels
Desc:   Smoothing in 1-D by simple regularization
DocCmd: sfsmoothreg | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing smooth data)
Param:  eps float  -  1. 		smoothness parameter 
Param:  repeat int  -  1 		repeat smoothing 

