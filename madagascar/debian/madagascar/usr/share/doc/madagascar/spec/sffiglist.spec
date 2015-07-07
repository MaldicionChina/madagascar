[sffiglist]
Cat:    RSF/user/jennings
Desc:   Compare Vplot files in Fig and Lock directories
DocCmd: sffiglist | cat
Param:  copy enum-bool  -  n 		copy different figs from figdir to lockdir?
Param:  figdir string  -   -  		fig directory, default = ./Fig
Param:  list string  -   -  		how much to list [none,diff,miss,all], default = all
Param:  lockdir string  -   -  		lock directory, default = lock counterpart of figdir
Param:  rsftest enum-bool  -  n 		write .rsftest file?
Param:  show string  -   -  		how much to show [none,diff,miss,all], default = none

