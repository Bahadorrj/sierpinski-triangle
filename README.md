# Sierpinski Triangle Generator

A Python implementation of the Sierpinski Triangle fractal using the Chaos Game method with animated visualization.

## Description

This project generates the Sierpinski Triangle fractal using the Chaos Game algorithm. The program creates an animated visualization where points are plotted progressively to reveal the fractal pattern. The Sierpinski Triangle is a famous fractal that demonstrates self-similarity and infinite complexity.

## How It Works

The Chaos Game algorithm works as follows:

1. **Initial Setup**: Start with three vertices of an equilateral triangle
2. **Random Starting Point**: Choose a random point inside the triangle
3. **Iterative Process**: For each iteration:
   - Randomly select one of the three vertices
   - Move halfway between the current point and the selected vertex
   - Plot the new point
4. **Result**: After many iterations, the Sierpinski Triangle pattern emerges

## Features

- **Animated Visualization**: Watch the fractal form point by point
- **Customizable Parameters**: Adjust side length, number of points, and animation speed
- **Mathematical Accuracy**: Uses proper barycentric coordinates for point generation
- **Real-time Display**: Matplotlib animation shows the fractal building in real-time

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install numpy matplotlib
```

## Usage

Run the program:

```bash
python triangle.py
```

The program will:

1. Display an equilateral triangle outline
2. Start plotting points from a random starting position
3. Animate the formation of the Sierpinski Triangle pattern
4. Continue until all 100,000 points are plotted

## Configuration

You can modify these parameters in `triangle.py`:

- `side_length = 100`: Length of the triangle's sides
- `N = 100000`: Number of points to generate
- `interval = 0.005`: Animation interval in milliseconds

## Mathematical Details

The program uses barycentric coordinates to generate random points within the triangle:

```python
def random_point_in_triangle(vertices):
    u, v = np.random.rand(2)
    if u + v > 1:
        u, v = 1 - u, 1 - v
    return (1 - u - v) * vertices[0] + u * vertices[1] + v * vertices[2]
```

This ensures uniform distribution of starting points within the triangle.

## Output

The program displays a matplotlib window showing:

- The outline of the equilateral triangle
- Points being plotted progressively in real-time
- The final Sierpinski Triangle fractal pattern

## Educational Value

This project demonstrates:

- Fractal geometry and self-similarity
- The Chaos Game algorithm
- Random number generation in geometric contexts
- Computer graphics and animation
- Mathematical visualization

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this project.
