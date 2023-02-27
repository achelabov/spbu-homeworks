package main

import (
	"fmt"
	"math"
)

func f(x float64) float64 {
	// Define your function f(x) here
	return math.Sin(x) + math.Pow(x, 3) - 9*x + 3
}

func secantMethod(x0 float64, x1 float64, eps float64) (float64, int) {
	// Initialize variables
	var fx0, fx1, x float64 = x0, x1, x1
	var m int = 0

	// Implement the Secant Method
	for {
		fx0 = f(x0)
		fx1 = f(x1)

		// Check if the method failed
		if fx1-fx0 == 0 {
			fmt.Println("Error: Division by zero")
			return 0, 0
		}

		// Compute new approximation using the Secant Method
		x = x1 - fx1*(x1-x0)/(fx1-fx0)
		m++

		// Check if root is found
		if math.Abs(x-x1) < eps {
			return x, m
		}

		// Check if maximum number of iterations is reached
		if m >= 100 {
			fmt.Println("Error: Maximum number of iterations reached")
			return 0, 0
		}

		// Update x0 and x1
		x0 = x1
		x1 = x
	}

	return x, m
}

func main() {
	// Prompt user for interval endpoints, number of steps, and epsilon precision
	var a, b float64
	var N int
	var eps float64
	fmt.Println("Enter interval endpoints [a,b]:")
	fmt.Print("a = ")
	fmt.Scan(&a)
	fmt.Print("b = ")
	fmt.Scan(&b)
	fmt.Print("Enter number of steps (N): ")
	fmt.Scan(&N)
	fmt.Print("Enter epsilon precision: ")
	fmt.Scan(&eps)

	// Compute step size h
	var h float64 = (b - a) / float64(N)

	// Iterate over all subintervals
	for i := 0; i < N; i++ {
		// Define subinterval
		var ai float64 = a + float64(i)*h
		var bi float64 = ai + h

		// Check if the function has opposite signs at a and b
		if f(ai)*f(bi) < 0 {
			// Apply the Secant Method to find root
			x0 := ai
			x1 := bi
			x, m := secantMethod(x0, x1, eps)

			// Output results
			fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
			fmt.Printf("Initial approximation: %.6f and %.6f\n", x0, x1)
			fmt.Printf("Number of steps: %d\n", m)
			fmt.Printf("Approximate solution: %.10f\n", x)
			fmt.Printf("Residual: %.10f\n\n", math.Abs(f(x)))
		}
	}
}
