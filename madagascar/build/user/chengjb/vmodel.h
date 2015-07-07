/* This file is automatically generated. DO NOT EDIT! */

#ifndef _vmodel_h
#define _vmodel_h


void vmodelboundary3d(float ***v, int nx, int ny, int nz, int nxpad, int nypad, int nzpad, int bd);
/*< filling padded boundaries of 3D model: nz, nx, ny are fastest, mid, and slowest dimension >*/


void vmodelboundary2d(float **v, int nx, int nz, int nxpad, int nzpad, int bd);
/*< filling padded boundaries of 2D model: nz is fastest dimension >*/

#endif
