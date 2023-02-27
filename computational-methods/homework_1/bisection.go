package main

import (
	"fmt"
	"math"
)

func f(x float64) float64 {
	// Define your function f(x) here
	return math.Sin(x) + math.Pow(x, 3) - 9*x + 3
}

func bisectionMethod(a, b float64, eps float64) (float64, int) {
	// Initialize variables
	var fa, fb, fx float64
	var xm float64
	var m int = 0
	var flag bool = true

	// Calculate function values at a and b
	fa = f(a)
	fb = f(b)

	// Check if the function has opposite signs at a and b
	if fa*fb > 0 {
		fmt.Println("function has same sign at a and b")
		return 0, 0
	}

	// Implement bisection method
	for flag {
		xm = (a + b) / 2
		fx = f(xm)
		m++

		// Check if the root lies in the left half interval
		if fx*fa < 0 {
			b = xm
			fb = fx
		} else {
			a = xm
			fa = fx
		}

		// Check if interval has become too small
		if math.Abs(b-a) < eps {
			flag = false
		}
	}

	return xm, m
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
			// Apply bisection method to find root
			x, m := bisectionMethod(ai, bi, eps)

			// Output results
			fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
			fmt.Printf("Initial approximation: %.6f\n", (ai+bi)/2)
			fmt.Printf("Number of steps: %d\n", m)
			fmt.Printf("Approximate solution: %.10f\n", x)
			fmt.Printf("Length of last segment: %.10f\n", math.Abs(bi-ai))
			fmt.Printf("Residual: %.10f\n\n", math.Abs(f(x)))
		}
	}
}
