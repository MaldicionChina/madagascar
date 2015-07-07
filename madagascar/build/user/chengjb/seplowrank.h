/* This file is automatically generated. DO NOT EDIT! */

#ifndef _seplowrank_h
#define _seplowrank_h


/*****************************************************************************************/
void seplowrank2d(float *ldata,float *rdata,float *fmid, float *x, int *ijkx, int *ijkz,
                int nx,int nz,int m,int n,int m2,int n2, int iflag);
/*< seplowrank2d: separating wave-modes based on low-rank decomposition >*/


/*****************************************************************************************/
void sep(float *w, float *x, int *ijkx, int *ijkz, int nx,int nz,int m,int n, int iflag);
/*< sep: separating wave-modes by filtering in wavenumber domain >*/


void  reconstruct(float **w, float *ldata, float *fmid, float *rdata, int m, int n, int m2, int n2);
/*< re-construct matrix using the lowrank decomposed matrixs >*/


void  reconstruct1(float *w, float *ldata, float *fmid, float *rdata, int m, int n, int m2, int n2, int im);
/*< re-construct matrix using the lowrank decomposed matrixs >*/


/*****************************************************************************************/
void seplowrank3d(float *ldata,float *rdata,float *fmid, float *p, int *ijkx, int *ijky, int *ijkz,
                      int nx, int ny, int nz, int m, int n, int m2, int n2, int iflag);
/*< seplowrank3d: wave-mode separation based on low-rank decomposition >*/

#endif
