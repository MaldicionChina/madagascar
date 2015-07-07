[sfdsreiko]
Cat:    RSF/user/llisiw
Desc:   Double square-root eikonal solver (2D)
DocCmd: sfdsreiko | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (no hint on content)
Param:  alpha string  -   -  		auxiliary output file name
Param:  causal enum-bool  -  y 		if y, neglect non-causal branches of DSR 
Param:  flag string  -   -  		auxiliary output file name
Param:  mask string  -   -  		auxiliary input file name
Param:  nloop int  -  10 		number of bisection root-search 
Param:  thres float  -  5.e-5 		threshold (percentage) 
Param:  tol float  -  1.e-3 		tolerance for bisection root-search 
Param:  velocity enum-bool  -  y 		if y, the input is velocity; n, slowness squared 

