There are 3 algorithms each of which I have recently programmed at home for practice and understanding purposes. 

-The first algorithm is gradient descent. The code does linear regression using gradient descent.
-Gradient descent uses derivatives to find maxima. 
Adding the derivative(slope) to the position until the derivative reaches zero or becomes negative.

-The second algorithm is Perlin noise. The code uses perlin noise to generate a 3d noise map, where a 2d slice is rendered to produce something like
artificial weather patterns.
-Perlin noise uses an n-dimensional unit cube with pseudo random gradients each seeded by vertices of the n-cube. 
A dot product is done from the sample location inside the cube and the random gradients and then interpolation is done
Get how much each edge should affect the result.
-Basically it works by sampling an infinite pesudo-random fractal.

-The third algorithm is simplex noise. Which optimizes a system of linear equations. The does an example of this.
-It works by using a tableau and pivot variables, which work by moving monotonically towards an optimum.