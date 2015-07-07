[sfbooklist]
Cat:    RSF/user/jennings
Desc:   List properties of Madagascar example book directories
DocCmd: sfbooklist | cat
Param:  command string  -   -  		command to execute in each directory, default = none
Param:  levels int  -  3 		directory search depth
Param:  list string  -   -  		how much to list [all,filter,none], default = all
Param:  local enum-bool  -  n 		fetch-local-data filter
Param:  nofetch enum-bool  -  y 		fetch-no-data filter
Param:  private enum-bool  -  n 		fetch-private-data filter
Param:  public enum-bool  -  n 		fetch-public-data filter
Param:  rsfproj string  -   -  		rsfproj filter [yes,no,both], default = yes
Param:  size int  -  1024**2 		max data size filter (MB)
Param:  skipfile string  -   -  		file with list of directories to skip
Param:  timer string  -   -  		output execution time [log,file,none], default = none
Param:  uses string  -   -  		uses filter, default = any

