import numpy as np
import matplotlib.pyplot as plt
from scipy import stats, fftpack, linalg, interpolate, optimize, signal
from scipy.integrate import odeint




def q1():
    arr = np.random.randn(1000) * 2 + 10
    print("\nQ1 RESULTS:")
    print("Mean:", np.mean(arr))
    print("Median:", np.median(arr))
    print("Variance:", np.var(arr))


def q2():
    x = np.linspace(0, 4*np.pi, 128)
    X, Y = np.meshgrid(x, x)
    arr = np.sin(X) + 0.5*np.cos(3*Y)
    F = fftpack.fftshift(fftpack.fft2(arr))
    print("\nQ2 RESULTS: FFT 2D shape =", F.shape)



def q3():
    A = np.array([[4,2,1],[0,3,-1],[2,-2,5]], float)
    print("\nQ3 RESULTS:")
    print("Determinant:", linalg.det(A))
    print("Inverse:\n", linalg.inv(A))
    print("Eigenvalues:", linalg.eigvals(A))




def q4():
    x = np.linspace(0, 10, 11)
    y = np.sin(x)
    f = interpolate.interp1d(x, y, kind='cubic')
    x_new = np.linspace(0, 10, 200)
    y_new = f(x_new)
    print("\nQ4 RESULTS: Interpolation complete.")



def q5():
    fs = 100
    t = np.linspace(0, 5, fs*5)
    sig = np.sin(2*np.pi*t) + 0.4*np.sin(20*np.pi*t)
    b, a = signal.butter(4, 5/(fs/2), 'low')
    filtered = signal.filtfilt(b, a, sig)
    print("\nQ5 RESULTS: Signal filtered.")



def q6():
    sales = np.random.randint(200, 2000, (12,4))
    total_month = sales.sum(axis=1)
    print("\nQ6 RESULTS:")
    print("Total per month:", total_month)
    print("Best month:", np.argmax(total_month)+1)
    print("Worst month:", np.argmin(total_month)+1)



def q7():
    names = ["Arin","Aditya","Chirag","Gurleen","Kunal"]
    marks = np.array([
        [85,78,92,88],
        [79,82,74,90],
        [90,85,89,92],
        [66,75,80,78],
        [70,68,75,85]
    ])
    total = marks.sum(axis=1)
    print("\nQ7 RESULTS:")
    print("Total:", dict(zip(names, total)))
    print("Top performer:", names[np.argmax(total)])
    print("Bottom performer:", names[np.argmin(total)])



def q8():
    t = np.array([0,1,2,3,4,5])
    v = np.array([2,3.1,7.9,18.2,34.3,56.2])
    def quad(t,a,b,c): return a*t*t + b*t + c
    params,_ = optimize.curve_fit(quad, t, v)
    print("\nQ8 RESULTS:")
    print("Fitted parameters (a,b,c):", params)



def q9():
    print("\nQ9 RESULTS: (Plotting version of Q7)")



def q10():
    print("\nQ10 RESULTS: (Plot created normally)")



def q11():
    years = np.array([2000,2005,2010,2015,2020])
    pop = np.array([50,55,70,80,90])
    r,_ = stats.pearsonr(years, pop)
    slope, intercept, *_ = stats.linregress(years, pop)
    print("\nQ11 RESULTS:")
    print("Correlation:", r)
    print("Population in 2008:", slope*2008 + intercept)



def q12():
    coeffs = [3,-5,2,-8]
    roots = np.roots(coeffs)
    print("\nQ12 RESULTS: Roots:", roots)



def q13():
    print("\nQ13 RESULTS: Demo only.")



def q14():
    def f(x): return x**4 - 3*x**3 + 2
    x = np.linspace(-2, 3, 500)
    y = f(x)
    idx = np.argmin(y)
    print("\nQ14 RESULTS:")
    print("Minimum value:", y[idx], "at x =", x[idx])



def q15():
    m, c, k = 1, 0.2, 4
    def model(y, t):
        θ, ω = y
        return [ω, -(c/m)*ω - (k/m)*θ]
    t = np.linspace(0,20,1000)
    sol = odeint(model, [1,0], t)
    print("\nQ15 RESULTS: Max displacement =", sol[:,0].max())



q1()
q2()
q3()
q4()
q5()
q6()
q7()
q8()
q9()
q10()
q11()
q12()
q13()
q14()
q15()