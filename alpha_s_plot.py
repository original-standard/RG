
import running
from scipy import optimize
from math import pi

N = 3 # N of light quarks
START = 1 # GeV
END = 3 # GeV
NUM = 100

for i in range(NUM):
    mu = START + (END - START) / NUM * i
    p = (running.tensor(N),running.ALPHA_S,running.SCALE,mu)
    sol = optimize.fmin(running.solv,running.ALPHA_S,disp=False,args=(p,),xtol=10e-12)
    print(mu,sol[0] * 4. * pi)
