import matplotlib.pyplot as plt
import numpy as np

def plot_matrix(matrix, title="Matrix Plot", figsize=(10, 8), fontsize=10):
    """
    Plot a matrix using imshow with mesh, cell values, and color coding for pos/neg values.
    
    Parameters:
    -----------
    matrix : array-like
        2D matrix to plot
    title : str, optional
        Title for the plot (default: "Matrix Plot")
    figsize : tuple, optional
        Figure size (width, height) (default: (10, 8))
    fontsize : int, optional
        Font size for cell values (default: 10)
    
    Returns:
    --------
    fig, ax : matplotlib figure and axis objects
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create the imshow plot
    im = ax.imshow(matrix, cmap='RdBu_r', aspect='equal')
    
    # Add colorbar
    cbar = plt.colorbar(im, ax=ax)
    cbar.set_label('Value', rotation=270, labelpad=20)
    
    # Add mesh/grid
    ax.set_xticks(np.arange(-0.5, matrix.shape[1], 1), minor=True)
    ax.set_yticks(np.arange(-0.5, matrix.shape[0], 1), minor=True)
    ax.grid(which="minor", color="black", linestyle='-', linewidth=0.5)
    
    # Add cell values
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix[i, j]
            # Use white text for dark backgrounds, black for light backgrounds
            text_color = 'white' if abs(value) > np.max(np.abs(matrix)) * 0.5 else 'black'
            ax.text(j, i, f'{value:.2f}', ha="center", va="center", 
                   color=text_color, fontsize=fontsize)
    
    # Set labels and title
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Column Index')
    ax.set_ylabel('Row Index')
    
    # Remove minor tick labels
    ax.tick_params(which="minor", size=0)
    
    plt.tight_layout()
    return fig, ax