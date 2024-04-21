package main

import (
	"fmt"
	"math"
	"sort"
)

func main() {
	fmt.Println("Problem of algebraic interpolation")
	fmt.Println("Option number 13")

	// read input values from user
	var m, n int
	var a, b, x float64

	fmt.Print("Enter the number of values in the table (m+1): ")
	fmt.Scan(&m)

	fmt.Print("Enter the ends of the interval [a, b]: ")
	fmt.Scan(&a, &b)

	fmt.Println("The initial table of function values:")
	table := generateTable(m+1, a, b)
	printTable(table)

	fmt.Print("Enter the interpolation point x: ")
	fmt.Scan(&x)

	fmt.Print("Enter the degree of the interpolation polynomial (n<=m): ")
	fmt.Scan(&n)

	// sort table by distance from x
	sort.Slice(table, func(i, j int) bool {
		return math.Abs(table[i].x-x) < math.Abs(table[j].x-x)
	})

	// select first n+1 nodes for interpolation
	nodes := table[:n+1]

	// calculate interpolation polynomial using Lagrange representation
	pl := lagrangePolynomial(nodes)

	// calculate interpolation polynomial using Newton representation
	pn := newtonPolynomial(nodes)

	// calculate actual errors
	errL := math.Abs(f(x) - pl(x))
	errN := math.Abs(f(x) - pn(x))

	// print results
	fmt.Println("Sorted table of function values:")
	printTable(nodes)
	fmt.Printf("Interpolation polynomial (Lagrange form): PnL(x) = %.26f\n", pl(x))
	fmt.Printf("Absolute actual error (Lagrange form): |f(x) - PnL(x)| = %.26f\n", errL)
	fmt.Printf("Interpolation polynomial (Newton form): PnN(x) = %.26f\n", pn(x))
	fmt.Printf("Absolute actual error (Newton form): |f(x) - PnN(x)| = %.26f\n", errN)

	// ask user if they want to continue
	for {
		var choice string
		fmt.Print("Enter 'y' to enter new values of x and n, or any other key to exit: ")
		fmt.Scan(&choice)
		if choice != "y" {
			break
		}

		fmt.Print("Enter the new value of x: ")
		fmt.Scan(&x)

		fmt.Print("Enter the new value of n: ")
		fmt.Scan(&n)

		// sort table by distance from new x value
		sort.Slice(table, func(i, j int) bool {
			return math.Abs(table[i].x-x) < math.Abs(table[j].x-x)
		})

		// select first n+1 nodes for interpolation
		nodes = table[:n+1]

		// calculate interpolation polynomial using Lagrange representation
		pl = lagrangePolynomial(nodes)

		// calculate interpolation polynomial using Newton representation
		pn = newtonPolynomial(nodes)

		// calculate actual errors
		errL = math.Abs(f(x) - pl(x))
		errN = math.Abs(f(x) - pn(x))

		// print results
		fmt.Println("Sorted table of function values:")
		printTable(nodes)
		fmt.Printf("Interpolation polynomial (Lagrange form): PnL(x) = %.26f, f(x)=%.26f\n", pl(x), f(x))
		fmt.Printf("Absolute actual error (Lagrange form): |f(x) - PnL(x)| = %.26f\n", errL)
		fmt.Printf("Interpolation polynomial (Newton form): PnN(x) = %.26f, f(x)=%.26f\n", pn(x), f(x))
		fmt.Printf("Absolute actual error (Newton form): |f(x) - PnN(x)| = %.26f\n", errN)
	}
}

// represents a point (x, f(x))
type point struct {
	x, fx float64
}

// f(x) = ln(1+x)-e^x
func f(x float64) float64 {
	return math.Log(1+x) - math.Exp(x)
}

// generates a table of function values for x in [a, b]
func generateTable(m int, a, b float64) []point {
	table := make([]point, m)
	dx := (b - a) / float64(m-1)
	for i := 0; i < m; i++ {
		x := a + float64(i)*dx
		table[i] = point{x, f(x)}
	}
	return table
}

// prints a table of function values
func printTable(table []point) {
	for _, p := range table {
		fmt.Printf("x = %v, f(x) = %v\n", p.x, p.fx)
	}
}

// calculates the Lagrange polynomial for the given nodes
func lagrangePolynomial(nodes []point) func(x float64) float64 {
	n := len(nodes) - 1
	return func(x float64) float64 {
		var sum float64
		for i := 0; i <= n; i++ {
			prod := nodes[i].fx
			for j := 0; j <= n; j++ {
				if i != j {
					prod *= (x - nodes[j].x) / (nodes[i].x - nodes[j].x)
				}
			}
			sum += prod
		}
		return sum
	}
}

// calculates the Newton polynomial for the given nodes
func newtonPolynomial(nodes []point) func(float64) float64 {
	// calculate divided differences
	n := len(nodes)
	coeffs := make([]float64, n)
	for i := 0; i < n; i++ {
		coeffs[i] = nodes[i].fx
	}
	for j := 1; j < n; j++ {
		for i := n - 1; i >= j; i-- {
			coeffs[i] = (coeffs[i] - coeffs[i-1]) / (nodes[i].x - nodes[i-j].x)
		}
	}

	// return a function that calculates the Newton polynomial for a given x value
	return func(x float64) float64 {
		result := coeffs[n-1]
		for i := n - 2; i >= 0; i-- {
			result = coeffs[i] + (x-nodes[i].x)*result
		}
		return result
	}
}
