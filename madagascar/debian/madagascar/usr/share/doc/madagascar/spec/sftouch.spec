[sftouch]
Cat:    RSF/user/ivlad
Desc:   Applies the Unix command touch to binaries of RSF datasets in a directory
DocCmd: sftouch | cat
Param:  chk4nan enum-bool  -  n 		Check for NaN values. Expensive!!
Param:  dir string  -   -  		Directory with files
LDesc:  (defaults to: .)
Param:  rec enum-bool  -  n 		Whether to go down recursively
Param:  verb enum-bool  -  n 		Display what is wrong with the dataset

