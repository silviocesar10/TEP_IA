import scipy.optimize

# Objective Function: 150x_1 + 130x_2 
# Constraint 1: 3x_1 + 2x_2 <= 40 
# Constraint 2: -x_1 <= -5

result = scipy.optimize.linprog( 
    [-150, -130],  # Cost function: 150x_1 + 130x_2 
    A_ub=[[3, 2], [-1, 0]],  # Coefficients for inequalities 
    b_ub=[40, -5],  # Constraints for inequalities: 40 and -5 
) 
 
if result.success: 
    print(f"X1: {round(result.x[0], 2)} hours") 
    print(f"X2: {round(result.x[1], 2)} hours") 
else: 
    print("No solution")
 