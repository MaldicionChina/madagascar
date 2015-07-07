/* This file is automatically generated. DO NOT EDIT! */

#ifndef _ml_traveltime_vconstant_h
#define _ml_traveltime_vconstant_h


#include "general_traveltime.h"


double T0_k(twod y_k,twod y_k1);
/*<Traveltime>*/


double T0_k_k(twod y_k, twod y_k1);
/*<Derivative of T with respect to x_k>*/


double T0_k_k1(twod y_k, twod y_k1);
/*<Derivative of T with respect to x_k1>*/


double T0_k_k_k(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k>*/


double T0_k_k1_k1(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k1>*/


double T0_k_k_k1(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k and x_k1>*/


double T0_k_zk(twod y_k, twod y_k1);
/*<Derivative of T with respect to z_k>*/


double T0_k_zk1(twod y_k, twod y_k1);
/*<Derivative of T with respect to z_k1>*/


double T0_k_zk_zk(twod y_k, twod y_k1);
/*<Second Derivative of T with respect to z_k>*/


double T0_k_zk1_zk1(twod y_k, twod y_k1);
/*<Second Derivative of T with respect to z_k1>*/


double T0_k_zk_zk1(twod y_k, twod y_k1);
/*<Second Derivative of T with respect to z_k and z_k1>*/


double T0_k_k_zk(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k and z_k>*/


double T0_k_k1_zk1(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k1 and z_k1>*/


double T0_k_k_zk1(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k and z_k1>*/


double T0_k_k1_zk(twod y_k, twod y_k1);
/*<Second derivative of T with respect to x_k1 and z_k>*/

#endif
