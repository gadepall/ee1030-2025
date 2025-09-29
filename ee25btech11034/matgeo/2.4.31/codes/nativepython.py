import numpy as np
import matplotlib.pyplot as plt
def create_geometry_graph():
    """
    Creates and displays a graph of points A, P, Q, the line segment PQ,
    the line from A to the midpoint of PQ, and the perpendicular bisector of PQ.
    """
    A = np.array([2, 7])
    P = np.array([6, 5])
    Q = np.array([0, -4])
    # Calculate the midpoint M of the line segment PQ
    M = (P + Q) / 2

    
    # Create a figure and an axes object for plotting
    fig, ax = plt.subplots(figsize=(9, 9))

    
    # Use scatter to plot individual points. zorder=5 ensures they are drawn on top of lines.
    ax.scatter(A[0], A[1], color='red', s=100, label=f'Point A {A}', zorder=5)
    ax.scatter(P[0], P[1], color='blue', s=100, label=f'Point P {P}', zorder=5)
    ax.scatter(Q[0], Q[1], color='green', s=100, label=f'Point Q {Q}', zorder=5)
    ax.scatter(M[0], M[1], color='purple', s=100, label=f'Midpoint M {M}', zorder=5)

    
    # Plot the line segment connecting P and Q
    ax.plot([P[0], Q[0]], [P[1], Q[1]], 'k-', lw=2, label='Line Segment PQ')

    # Plot the line segment connecting A and the midpoint M
    ax.plot([A[0], M[0]], [A[1], M[1]], 'r--', lw=2, label='Line Segment AM')

    
    # This shows the actual line A would need to be on.
    # The perpendicular bisector passes through M and is perpendicular to PQ.

    # Calculate the slope of PQ
    # Add a check for vertical/horizontal lines to avoid division by zero
    if not np.isclose(P[0], Q[0]):  # If the line PQ is not vertical
        slope_pq = (P[1] - Q[1]) / (P[0] - Q[0])
        if not np.isclose(slope_pq, 0): # If the line is not horizontal
            # The slope of the perpendicular bisector is the negative reciprocal
            slope_perp = -1 / slope_pq

            # Get the current plot limits to draw the line across the whole graph
            x_vals = np.array(ax.get_xlim())
            # Use the point-slope form: y - y1 = m(x - x1) -> y = m(x - x1) + y1
            y_vals = slope_perp * (x_vals - M[0]) + M[1]
            ax.plot(x_vals, y_vals, color='orange', linestyle='-.', lw=2, label='Perpendicular Bisector')
        else: # The line PQ is horizontal
            ax.axvline(x=M[0], color='orange', linestyle='-.', lw=2, label='Perpendicular Bisector')
    else: # The line PQ is vertical
        ax.axhline(y=M[1], color='orange', linestyle='-.', lw=2, label='Perpendicular Bisector')


    # --- 7. Finalize and Show Plot ---
    # Add titles, labels, and a grid for better readability
    ax.set_title('Geometric Visualization of Points A, P, and Q', fontsize=16)
    ax.set_xlabel('X-axis', fontsize=12)
    ax.set_ylabel('Y-axis', fontsize=12)
    ax.axhline(0, color='grey', lw=0.5)
    ax.axvline(0, color='grey', lw=0.5)
    ax.grid(True, linestyle='--', alpha=0.7)
    
    # Set the aspect ratio to 'equal' to ensure perpendicular lines look correct
    ax.set_aspect('equal', adjustable='box')
    
    # Add a legend to identify all the plotted elements
    ax.legend(fontsize=10)
    
    # Display the plot
    plt.show()
def check_perpendicular_bisector(A, P, Q):
    """
    Checks if point A lies on the perpendicular bisector of the line segment PQ.
    """
    midpoint_M = (P + Q) / 2
    vector_MA = A - midpoint_M
    vector_QP = P - Q
    dot_product = (vector_MA.T @ vector_QP).item()
    
    if np.isclose(dot_product, 0):
        print("Point A lies on the perpendicular bisector of PQ.")
    else:
        print(f" Point A does NOT lie on the perpendicular bisector of PQ (the dot product is not 0).")

# Define points as column vectors
A = np.array([[2, 7]]).reshape(-1,1)
P = np.array([[6,5]]).reshape(-1,1)
Q = np.array([[0, -4]]).reshape(-1,1)

check_perpendicular_bisector(A, P, Q)

create_geometry_graph()
