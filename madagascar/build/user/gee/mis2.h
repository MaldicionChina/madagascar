/* This file is automatically generated. DO NOT EDIT! */

#ifndef _mis2_h
#define _mis2_h


void mis2(int niter         /* number of iterations */, 
	  int nx            /* model size */, 
	  float *xx         /* model */, 
	  sf_filter aa      /* helix filter */, 
	  const bool *known /* mask for known data */,
	  float eps         /* regularization parameter */,
	  bool doprec       /* to apply preconditioning */);
/*< interpolate >*/

#endif
