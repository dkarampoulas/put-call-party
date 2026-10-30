# Black-Scholes & Put-Call Parity Simulation

Python implementation of the Black-Scholes-Merton option pricing model, Put-Call Parity verification, and terminal option payoff simulation using Geometric Brownian Motion.

## Features
**Prices European Options:** Calculates the theoretical value of Call and Put options based on stock price, strike, volatility, and time.
2. **Checks Put-Call Parity:** Confirms that $C - P$ matches $S - PV(K)$ so there's no arbitrage lurking around.
3. **Simulates Payoffs:** Runs a few randomized terminal stock prices (using Geometric Brownian Motion) to see how the options would actually pay out at expiration.

## Requirements
- Python 3.x (Standard libraries: `math`, `random`)

## Usage
```bash
python main.py


EXAMPLE OUTPUT
call 10.4506 put 5.5735
C-P 4.8771
S-PV(K) 4.8771
113.04 13.04 0.00 13.04
106.70 6.70 0.00 6.70
86.88 0.00 13.12 -13.12
150.03 50.03 0.00 50.03
72.68 0.00 27.32 -27.32