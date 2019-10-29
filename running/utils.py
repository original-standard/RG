
from running.main import *
from scipy import optimize
from math import exp
from math import log
from math import sqrt



matching_factor = {"SSMOMG" : lambda x : 1 + x * 1.978852189 + x * x * (55.03243483 - 3. * 6.161687618 
                + 1.978852189 * 1.978852189), 
                "SSMOM" : lambda x : (1. + 0.6455188560 * x + (22.60768757 - 4.013549470 * 3. - 0.6455188560    
                  * 0.6455188560) * x * x ),
                "TSMOMG" : lambda x : (1 + 1.11816038 * x - x * x * (8.607630493 - 1.955130440 * 3.)),
                "TSMOM" : lambda x : (1. -0.21517295 * x - x * x * (43.38395007 - 4.10327859 * 3.))}


BILINEAR = {"tensor" : tensor(3), "scalar" : scalar(3)}


ALPHA_S = 0.2904 / (3.14 * 4.) # ALPHA_S

SCALE = 2 # at 2GeV


def int(a,param):
 return (param.Cm1() / a + param.C0() * log(a) + param.C1() * a + param.C2() * a * a)
def solv(a,param):
 alpha = param[1]
 mu_1 = param[2]
 mu_2 = param[3]
 res = (int(a,param[0]) - int(alpha,param[0]) + 2 * log((mu_1 / mu_2)))
 return res * res

def matching(mu,match):
 p = (tensor(3),ALPHA_S,SCALE,mu)
 sol = optimize.fmin(solv,ALPHA_S,disp=False,args=(p,),xtol=10e-12)
 return matching_factor[match](sol[0])

def flow(mu,bi):
 c = BILINEAR[bi]
 p = (c,ALPHA_S,2.0,mu)                   
 sol = optimize.fmin(solv,ALPHA_S,disp=False,args=(p,),xtol=10e-12)
 ln = c.C0_2() * (log((ALPHA_S)) -log(sol[0]))
 ln = ln + c.C1_2() * ((ALPHA_S) - sol[0])
 ln = ln + c.C2_2() * ((ALPHA_S) * (ALPHA_S) - sol[0] * sol[0])
 return exp(ln) 
