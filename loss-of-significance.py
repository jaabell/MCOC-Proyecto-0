import scipy as sp
import matplotlib.pylab as plt
import sys

#Sum that minimizes truncation error at expense of more memory usage
def smart_sum(a,dtype=0):
	if dtype==0:
		dtype=a.dtype
	a = a.reshape((-1))
	N = a.size
	iter = 0
	while N > 1:
		iter += 1
		a0 = 0.
		if N % 2 == 1:
			a0 = a[0]
			a = a[1:]
			N = N-1
		tmp = a[0:(N/2)] 
		tmp += a[(N/2):]
		if a0 > 0:
			tmp += a0
		a = tmp
		N = a.size
	return a[0]

#Mean using smart_sum
def smart_mean(a):
	N = a.size
	return smart_sum(a) / N

#Target value
exact_mean = 0.55

#Try these array lengths
N_power_values = [15, 16, 17, 18, 19, 20, 21, 22]

#Initialize arrays to store results... all as float64
M = len(N_power_values)
mean_1 = sp.zeros(M, dtype=sp.float64)
mean_2 = sp.zeros(M, dtype=sp.float64)
mean_3 = sp.zeros(M, dtype=sp.float64)
mean_4 = sp.zeros(M, dtype=sp.float64)
mean_5 = sp.zeros(M, dtype=sp.float64)
error_1 = sp.zeros(M, dtype=sp.float64)
error_2 = sp.zeros(M, dtype=sp.float64)
error_3 = sp.zeros(M, dtype=sp.float64)
error_4 = sp.zeros(M, dtype=sp.float64)
error_5 = sp.zeros(M, dtype=sp.float64)

#For all array sizes, compute means with different methods....
for i, exp in enumerate(N_power_values):

	N = 2**exp

	#Init arrays
	a32 = sp.zeros((2,N), dtype=sp.float32)
	a64 = sp.zeros((2,N), dtype=sp.float64)
	a32[0,:] = 1.0
	a32[1,:] = 0.1
	a64[0,:] = 1.0
	a64[1,:] = 0.1

	#Compute means with different methods and data types
	mean_1[i] = sp.mean(a32)
	mean_2[i] = sp.mean(a64)
	mean_3[i] = sp.mean(a32, dtype=sp.float64)
	mean_4[i] = smart_mean(a32)
	mean_5[i] = smart_mean(a64)

	#Compute relative errors
	error_1[i] = abs(mean_1[i] - exact_mean)/ exact_mean 
	error_2[i] = abs(mean_2[i] - exact_mean)/ exact_mean 
	error_3[i] = abs(mean_3[i] - exact_mean)/ exact_mean 
	error_4[i] = abs(mean_4[i] - exact_mean)/ exact_mean 
	error_5[i] = abs(mean_5[i] - exact_mean)/ exact_mean 

	#Print to std-output some stuff
	print "N = {}".format(N)
	print "  mean_1 = {0:14.12f}   (error_1 = {1:14.12f}%)".format(mean_1[i], error_1[i]*100)
	print "  mean_2 = {0:14.12f}   (error_2 = {1:14.12f}%)".format(mean_2[i], error_2[i]*100)
	print "  mean_3 = {0:14.12f}   (error_3 = {1:14.12f}%)".format(mean_3[i], error_3[i]*100)
	print "  mean_4 = {0:14.12f}   (error_4 = {1:14.12f}%)".format(mean_4[i], error_4[i]*100)
	print "  mean_5 = {0:14.12f}   (error_5 = {1:14.12f}%)".format(mean_5[i], error_5[i]*100)


#Plot relative errors
plt.figure(1)

plt.semilogy(N_power_values, error_1, label="a.dtype=float32 y $\mu$=sp.mean(a)")
plt.semilogy(N_power_values, error_2, label="a.dtype=float64 y $\mu$=sp.mean(a)")
plt.semilogy(N_power_values, error_3, label="a.dtype=float32 y $\mu$=sp.mean(a,dtype=sp.float64)")
plt.semilogy(N_power_values, error_4, label="a.dtype=float32 y $\mu$=smart_mean(a)")
plt.semilogy(N_power_values, error_5, label="a.dtype=float64 y $\mu$=smart_mean(a)")

plt.xlabel("$N$, donde a.size=$2^N$")
plt.ylabel("Error relativo")

plt.grid(True)

#Set the legend to be outside the ax
ax = plt.gca()
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width, 0.81*box.height])
ax.legend(loc='lower left', bbox_to_anchor=(0, 1.00))

plt.savefig("loss-of-significance.png")

plt.show()