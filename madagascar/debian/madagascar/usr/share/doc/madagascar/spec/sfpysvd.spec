[sfpysvd]
Cat:    RSF/user/godwinj
Desc:   Perform SVD on a matrix using SCIPY
DocCmd: sfpysvd | cat
Port:   stdin  rsf r req 	RSF standard input (containing fin data)
Port:   stdout rsf w req 	RSF standard output (containing fout data)
Param:  left string  -   -  		File to store left singular vectors
Param:  right string  -   -  		File to store right singular vectors
Param:  vectors enum-bool  -  n 		Output singular vectors?

