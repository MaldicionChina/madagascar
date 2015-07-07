/* This file is automatically generated. DO NOT EDIT! */

#ifndef _fwportpseudop_h
#define _fwportpseudop_h


void fwportpseudop1(float dt2,float*** p1,float*** p2,float*** p3,float*** q1,float*** q2,float*** q3,
		    float*** r1,float*** r2,float*** r3,
		    float* coeff_2dx,float* coeff_2dy,float* coeff_2dz,float* coeff_1dx,float* coeff_1dy,float* coeff_1dz,
		    float*** vp0,float ***vs0,float*** epsi_1,float*** del_1, float ***gama_1,float*** epsi_2,float*** del_2,
		    float ***gama_2,float ***del_3, float ***alpha, float ***the, float ***phi,
		    int nx, int ny, int nz, int nxpad, int nypad, int nzpad, float dx, float dy, float dz);
/*< fwportpseudop1: forward-propagating in ORT media with pseudo-pure P-wave equation>*/


void fwportpseudop(float dt2,float*** p1,float*** p2,float*** p3,float*** q1,float*** q2,float*** q3,
                   float*** r1,float*** r2,float*** r3,
                   float* coeff_2dx,float* coeff_2dy,float* coeff_2dz,float* coeff_1dx,float* coeff_1dy,float* coeff_1dz,
                   float*** vp0,float ***vs0,float*** epsi_1,float*** del_1, float ***gama_1,float*** epsi_2,float*** del_2,
                   float ***gama_2,float ***del_3, float ***alpha, float ***the, float ***phi,
                   int nx, int ny, int nz, int nxpad, int nypad, int nzpad, float dx, float dy, float dz);
/*< fwportpseudop: forward-propagating in ORT media with pseudo-pure P-wave equation>*/


/******************************for the hti media****************************/
void fwportpseudophomo(float dt,float***p1,float***p2,float***p3, 
		       float***q1,float***q2,float***q3, 
		       float***r1,float***r2,float***r3, 
		       float*coeff_2dx,float*coeff_2dy,float*coeff_2dz,float*coeff_1dx,float*coeff_1dy,float*coeff_1dz,
		       float vp0, float vs0,float epsi1,float del1, float gama1,float epsi2,float del2, 
		       float gama2,float del3, int nx, int ny, int nz, float dx, float dy, float dz);
/*< fwportpseudophomo: forward-propagating in ORT media with pseudo-pure P-wave equation>*/

#endif
