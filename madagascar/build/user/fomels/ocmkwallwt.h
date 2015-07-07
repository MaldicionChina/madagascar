/* This file is automatically generated. DO NOT EDIT! */

#ifndef _ocmkwallwt_h
#define _ocmkwallwt_h


#include <stdio.h>


#include <rsf.h>


void ocmkwallwt(bool inv      /* if compute 1/weight */, 
		int dim       /* number of dimensions */, 
		int* npatch   /* number of patches [dim] */, 
		int* nwall    /* data size [dim] */, 
		int* nwind    /* patch size [dim] */, 
		float* windwt /* window weighting */, 
		FILE* wallwt  /* out-of-core wall weighting */);
/*< make wall weight >*/

#endif
