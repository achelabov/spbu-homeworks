package main

import (
	"fmt"
	"math"
)

func f(x float64) float64 {
	// Define your function f(x) here
	return math.Sin(x) + math.Pow(x, 3) - 9*x + 3
}

func df(x float64) float64 {
	// Define the derivative of f(x) here
	return math.Cos(x) + 3*math.Pow(x, 2) - 9
}

func modifiedNewtonMethod(x0 float64, eps float64) (float64, int) {
	// Initialize variables
	var fx0, x float64 = f(x0), x0
	var m int = 0

	// Implement the Modified Newton's Method
	for {
		// Check if the derivative is zero
		if df(x) == 0 {
			fmt.Println("Error: Division by zero")
			return 0, 0
		}

		// Compute new approximation using the Modified Newton's Method
		x = x - fx0/df(x)
		m++

		// Check if root is found
		if math.Abs(x-x0) < eps {
			return x, m
		}

		// Check if maximum number of iterations is reached
		if m >= 100 {
			fmt.Println("Error: Maximum number of iterations reached")
			return 0, 0
		}

		// Update x0 and fx0
		x0 = x
		fx0 = f(x0)
	}

	return x, m
}

func newtonMethod(x0 float64, eps float64) (float64, int) {
	// Initialize variables
	var fx, dfx float64
	var x float64 = x0
	var m int = 0
	var flag bool = true

	// Implement Newton's method
	for flag {
		fx = f(x)
		dfx = df(x)
		x = x - fx/dfx
		m++

		// Check if root is found
		if math.Abs(fx) < eps {
			return x, m
		}

		// Check if the method failed
		if dfx == 0 {
			fmt.Println("Error: Derivative is zero")
			return 0, 0
		}

		// Check if maximum number of iterations is reached
		if m >= 100 {
			fmt.Println("Error: Maximum number of iterations reached")
			return 0, 0
		}
	}

	return x, m
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

func bisectionMethod(a, b float64, eps float64) (float64, int) {
	// Initialize variables
	var fa, fb, fx float64
	var xm, dfx, dfa float64
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
		dfx = math.Abs(fx)
		dfa = math.Abs(fa)
		m++

		// Check if root is found
		if dfx < eps && dfa < eps {
			return xm, m
		}

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
			func() {
				// Apply bisection method to find root
				x, m := bisectionMethod(ai, bi, eps)

				// Output results
				fmt.Println("Bisection method")
				fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
				fmt.Printf("Initial approximation: %.6f\n", (ai+bi)/2)
				fmt.Printf("Number of steps: %d\n", m)
				fmt.Printf("Approximate solution: %.10f\n", x)
				fmt.Printf("Length of last segment: %.10f\n", math.Abs(bi-ai))
				fmt.Printf("Residual: %.16f\n\n", math.Abs(f(x)))
			}()
			func() {
				// Apply Newton's method to find root
				x0 := (ai + bi) / 2
				x, m := newtonMethod(x0, eps)

				// Output results
				fmt.Println("Newton's method")
				fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
				fmt.Printf("Initial approximation: %.6f\n", x0)
				fmt.Printf("Number of steps: %d\n", m)
				fmt.Printf("Approximate solution: %.10f\n", x)
				fmt.Printf("Residual: %.16f\n\n", math.Abs(f(x)))
			}()
			func() {
				// Apply the Modified Newton's Method to find root
				x0 := (ai + bi) / 2
				x, m := modifiedNewtonMethod(x0, eps)

				// Output results
				fmt.Println("Modified Newton's method")
				fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
				fmt.Printf("Initial approximation: %.6f\n", x0)
				fmt.Printf("Number of steps: %d\n", m)
				fmt.Printf("Approximate solution: %.10f\n", x)
				fmt.Printf("Residual: %.16f\n\n", math.Abs(f(x)))
			}()
			func() {
				// Apply the Secant Method to find root
				x0 := ai
				x1 := bi
				x, m := secantMethod(x0, x1, eps)

				// Output results
				fmt.Println("Secant method")
				fmt.Printf("Root found in interval [%.6f, %.6f]:\n", ai, bi)
				fmt.Printf("Initial approximation: %.6f and %.6f\n", x0, x1)
				fmt.Printf("Number of steps: %d\n", m)
				fmt.Printf("Approximate solution: %.10f\n", x)
				fmt.Printf("Residual: %.16f\n\n", math.Abs(f(x)))
			}()
		}
	}
}
