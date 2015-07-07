[sfwarpadd]
Cat:    RSF/user/fomels
Desc:   Add a perturbation to the warping function
DocCmd: sfwarpadd | cat
Port:   stdin  rsf r req 	RSF standard input (no hint on content)
Port:   stdout rsf w req 	RSF standard output (containing sum data)
Port:   add rsf r  -  		auxiliary input file name (containing unspecified data)
Param:  accuracy int  -   -  		Interpolation accuracy order 
Param:  m1 int  -   -  		Trace pading 
LDesc:  (defaults to: n1*2)

