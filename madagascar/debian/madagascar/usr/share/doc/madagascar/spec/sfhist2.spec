[sfhist2]
Cat:    RSF/user/ivlad
Desc:   Compute a 2-D histogram of integer- or float-valued input data
DocCmd: sfhist2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Port:   inp2 rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  d1 float  -   -  		histogram sampling for dimension 1 
Param:  d2 float  -   -  		histogram sampling for dimension 2 
Param:  n1 int  -   -  		number of histogram samples in dimension 1 
Param:  n2 int  -   -  		number of histogram samples in dimension 2 
Param:  o1 float  -   -  		histogram origin for dimension 1 
Param:  o2 float  -   -  		histogram origin for dimension 2 

