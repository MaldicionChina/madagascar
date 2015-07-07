[sfcshifts2]
Cat:    RSF/user/gchliu
Desc:   Generate shifts for 2-D regularized autoregression in complex domain. From (x,y,f) to (x,y,s,f)
DocCmd: sfcshifts2 | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing shifts data)
Param:  ns1 int  -   -  		number of shifts in first dim 
Param:  ns2 int  -   -  		number of shifts in second dim 

