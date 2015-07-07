/* This file is automatically generated. DO NOT EDIT! */

#ifndef _t2diter_h
#define _t2diter_h


void t2d_init(int dim  /* model dimension */,
	      int *n   /* model size */,
	      float *d /* model sampling */,
	      int n_t0, float d_t0, float o_t0,
	      int n_x0, float d_x0, float o_x0);
/*< initialize >*/


void t2d_caustic(float* x0   /* x0 */,
		 int* f0     /* f0 (modified in place) */, 
		 int* n, float* d /* model */,
		 float thres /* thresholding */);
/*< caustic region (2D) >*/


void t2d_set(float* t0 /* t0 */,
	     float* x0 /* x0 */,
	     int* f0   /* f0 */,
	     float* v0   /* slowness squared */, 
	     float* vd0  /* Dix velocity */,
	     float* vdt0 /* Dix derivative in t0 */, 
	     float* vdx0 /* Dix derivative in x0 */,
	     int* m0   /* mask */,
	     float* p0 /* preconditioner */);
/*< set operator >*/


void t2d_close(void);
/*< free >*/


void t2d_cost(float* cost);
/*< evaluate cost >*/


void t2d_dt(const float* ds /* perturbation */,
	    float* dt       /* linear prediction of dt */);
/*< linear predict dt >*/


void t2d_dx(const float* dt /* dt */,
	    float* dx       /* linear prediction of dx */);
/*< linear predict dx >*/


void t2d_prec(bool adj, bool add, int nd, int nr, float *d, float *r);
/*< preconditioner >*/


void t2d_oper(bool adj, bool add, int nx, int nr, float *x, float *r);
/*< linear operator >*/

#endif
