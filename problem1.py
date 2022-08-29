# MAE 598 - Design Optimization HW1 Problem 1
# Benjamin Webb
# 8/27/2022

import scipy.optimize as sp
import numpy as np


def Fx(x):
	# Function to minimize in problem 1
	# x is a 5 element array
	F = (x[0] - x[1]) ** 2 + (x[1] + x[2] - 2) ** 2 + (x[3] - 1) ** 2 + (x[4] - 1) ** 2

	return F


# Main program for problem 1
if __name__ == '__main__':
	# HW1 Problem 1

	# Define Constraints
	# Bound constraints
	bound_constraints = sp.Bounds([-10.0, -10.0, -10.0, -10.0, -10.0], [10.0, 10.0, 10.0, 10.0, 10.0])

	# Linear constraints
	A = np.array([[1.0, 3.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 1.0, -2.0], [0.0, 1.0, 0.0, 0.0, -1.0]])
	lb = np.array([0.0, 0.0, 0.0])
	ub = np.array([0.0, 0.0, 0.0])
	linear_constraints = sp.LinearConstraint(A, lb, ub)

	# Define initial guess
	x0 = np.array([0.0, 0.0, 0.0, 0.0, 0.0])

	# Solve minimization problem
	min_sol = sp.minimize(Fx, x0, method='trust-constr', bounds=bound_constraints, constraints=linear_constraints, options={'verbose': 1})

	print('x1 = ' + str(min_sol.x[0]))
	print('x2 = ' + str(min_sol.x[1]))
	print('x3 = ' + str(min_sol.x[2]))
	print('x4 = ' + str(min_sol.x[3]))
	print('x5 = ' + str(min_sol.x[4]))
