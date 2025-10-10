import numpy as np
import matplotlib.pyplot as plt

def check_collinearity(A, B, C, tol=1e-9):
    
    
    mat = np.array([
        [A[0], A[1], 1],
        [B[0], B[1], 1],
        [C[0], C[1], 1]
    ])
    
    
    det = np.linalg.det(mat)
    
  
    return abs(det) <= tol

if __name__ == "__main__":

    A = np.array([1,5])
    B = np.array([2,3])
    C = np.array([-2,-11])

    is_collinear = check_collinearity(A, B, C)
    print("Collinear" if is_collinear else "Not collinear")

    plt.figure(figsize=(8, 8))
    
    
    plt.plot(A[0], A[1], 'ro', markersize=8, label='Point A')
    plt.plot(B[0], B[1], 'go', markersize=8, label='Point B')
    plt.plot(C[0], C[1], 'bo', markersize=8, label='Point C')


    plt.text(A[0] + 0.2, A[1], f"A{tuple(A)}", fontsize=12)
    plt.text(B[0] + 0.2, B[1], f"B{tuple(B)}", fontsize=12)
    plt.text(C[0] + 0.2, C[1], f"C{tuple(C)}", fontsize=12)
    
   
    if is_collinear:
      
        if abs(A[0] - C[0]) < 1e-9:
         
            plt.axvline(x=A[0], color='k', linestyle='--', label='Collinear Line')
        else:

            all_x = np.array([A[0], B[0], C[0]])
            x_line = np.linspace(all_x.min() - 1, all_x.max() + 1, 100)
            
            slope = (C[1] - A[1]) / (C[0] - A[0])

            y_line = A[1] + slope * (x_line - A[0])
            
            plt.plot(x_line, y_line, 'k--', label='Collinear Line')


    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Collinearity Check of Three Points')
    plt.legend()
    plt.grid(True)
    plt.gca().set_aspect('equal', adjustable='box') # Ensure x and y axes have equal scales
    plt.show()