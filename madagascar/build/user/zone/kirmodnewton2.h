/* This file is automatically generated. DO NOT EDIT! */

#ifndef _kirmodnewton2_h
#define _kirmodnewton2_h


#include "kirmod2.h"
#include "kirmodnewton.h"


typedef struct Velocity2 {
	float *v, *gx, *gz, *xref, *zref, *thick, *sumthick, **aniso;
} velocity2;


void kirmodnewton_init(float **temp_rr /* Reflectors data of dimension N2xN1 */,
					   float **temp_rd /* Dip data*/,
					   int *updown /* Direction of the ray */,
					   float r01 /* Origin of reflectors */,
					   float dr1 /* Increment between elements in reflectors */,
					   int N1 /* Number of elements in each reflector */,
					   int n /* Number of reflections */,
					   int order /* Order of eno interpolation */,
					   int N2 /* Number of reflectors including surface*/,
					   int vstatus1 /* Type of model (vconstant(0) or vgradient(1) or VTI(2))*/,
					   float *xref_inp /* x-coordinate reference points */,
					   float *zref_inp /* z-coorditnate reference points */,
					   float *v_inp /* Velocities at reference points */,
					   float *gx_inp /* x-gradient at the reference points */,
					   float *gz_inp /* z-gradeint at the reference points */,
					   float **aniso_input /* anisotropy parameters*/);
/*<Initialize reflectors for kirmodnewton>*/


surface kirmodnewton2_init(int ns,  float s0,  float ds  /* source/midpoint axis */,
					 int nh,  float h0,  float dh  /* offset axis */,
					 int nx1, float x01, float dx1 /* reflector axis */,
					 int nc1                       /* number of reflectors */,
                     bool cmp                      /* if CMP instead of shot gather */,
                     bool absoff                   /* use absolute offset */);
/*< Initialize surface locations same as in kirmod2 >*/


void kirmodnewton2_table(surface y /* Surface structure*/,
				   bool debug /* Debug Newton */,
				   bool fwdxini /* Use the result of the previous iteration for the next one*/,
				   int niter /* Number of iteration for Newton */,
				   double tolerance /* Tolerance level for Newton */);
/*<Compute traveltime map>*/


ktable kirmodnewton2_map(surface y, int is, int ih, int ix, int ic);
/*< Extract from traveltime/amplitude map >*/

#endif
