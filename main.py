from math import erf,exp,log
import random
# standard normal cumulative distribution function (CDF)
N = lambda x: .5 + erf(x/2** .5) /2 #normal
# model inputs: Spot price, Strike, Risk-free rate, Time to maturity, Volatility
S, K, r, T, s= 100, 100, .05, 1, .2 #inputs
v=s*T ** .5 # volatility scaled by square root of time
pv=K * exp(-r*T) # present value of the strike price PV(K)

# Black-Scholes terms
d1=(log(S/K) + (r+s*s/2)*T)/v

# European Call and Put option pricing formulas
C=S*N(d1) - pv *  N(d1-v) #call
P=pv* N(v-d1)-S*N(-d1) #put

# Output theoretical prices
print('call',round(C,4),'put',round(P,4))

# Verify Put-Call Parity: C - P should equal S - PV(K)
print('C-P',round(C-P,4)) #call minus put difference
print('S-PV(K)', round(S-pv,4)) #spot minus present value of strike
random.seed(32) #some end prices, fixed seed
for i in range(6): #payoffs at expiry
    ST=S*exp(random.gauss(0,v)) #end price
    c,p=max(ST-K,0), max(K-ST,0)
    print(f'{ST:.2f} {c:.2f} {p:.2f} {c-p:.2f}')