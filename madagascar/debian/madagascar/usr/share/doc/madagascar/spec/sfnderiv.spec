[sfnderiv]
Cat:    RSF/user/ediazp
Desc:   
DocCmd: sfnderiv | cat
Port:   stdin  rsf r req 	RSF standard input (containing Fin data)
Port:   stdout rsf w req 	RSF standard output (containing Fout data)
Param:  axis int  -  1 		apply differentiator along axis, default is fast axis
Param:  length int  -  5 		filter length, the lengthier the accurate, but also gets costlier
Param:  order int  -  1 		order of the derivative, default first derivative
Param:  scale enum-bool  -  y 		scales by 1/d^order

