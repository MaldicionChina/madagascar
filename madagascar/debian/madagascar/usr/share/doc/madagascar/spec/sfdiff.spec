[sfdiff]
Cat:    RSF/user/chenyk
Desc:   Compare the difference of two rsf data sets with the same size
DocCmd: sfdiff | cat
Port:   stdin  rsf r req 	RSF standard input (containing inp1 data)
Port:   stdout rsf w req 	RSF standard output (containing dif data)
Port:   match rsf r  -  		auxiliary input file name (containing unspecified data)

