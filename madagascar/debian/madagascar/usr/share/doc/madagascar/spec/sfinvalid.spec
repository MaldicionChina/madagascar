[sfinvalid]
Cat:    RSF/user/ivlad
Desc:   Finds RSF files with missing or incomplete binaries or headers
DocCmd: sfinvalid | cat
Param:  chk4nan enum-bool  -  n 		Check for NaN values. Expensive!!
Param:  dir string  -   -  		Directory with files
LDesc:  (defaults to: .)
Param:  rec enum-bool  -  n 		Whether to go down recursively
Param:  verb enum-bool  -  n 		Display what is wrong with the dataset

