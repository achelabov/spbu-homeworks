package main

import (
	"fmt"
	"math"
)

func main() {
	var m int
	var a, b, F float64

	// Ввод параметров задачи
	fmt.Println("Введите количество узлов (m+1):")
	fmt.Scanln(&m)

	fmt.Println("Введите начальное значение a:")
	fmt.Scanln(&a)

	fmt.Println("Введите конечное значение b:")
	fmt.Scanln(&b)

	fmt.Println("Введите значение F:")
	fmt.Scanln(&F)

	// Вычисление шага h
	h := (b - a) / float64(m)

	// Создание узлов и вычисление значений функции в узлах
	x := make([]float64, m+1)
	y := make([]float64, m+1)
	for i := 0; i <= m; i++ {
		x[i] = a + float64(i)*h
		y[i] = f(x[i])
	}

	// Решение уравнения Pn(x) = F методом секущих
	x0 := a
	x1 := b
	epsilon := 0.0001 // Точность
	root, err := secantMethod(x0, x1, F, x, y, m+1, epsilon)
	if err != nil {
		fmt.Println("Ошибка:", err)
		return
	}

	// Вычисление невязки для найденного корня
	res := residual(root, F)

	// Вывод результата
	fmt.Printf("Корень уравнения Pn(x) = F: %.6f\n", root)
	fmt.Printf("Невязка при найденном корне: %.6f\n", res)
}

// Функция для интерполяции методом Лагранжа
func lagrangeInterpolation(x []float64, y []float64, n int, xVal float64) float64 {
	result := 0.0
	for i := 0; i < n; i++ {
		term := y[i]
		for j := 0; j < n; j++ {
			if j != i {
				term *= (xVal - x[j]) / (x[i] - x[j])
			}
		}
		result += term
	}
	return result
}

// Функция для вычисления значения функции f(x)
func f(x float64) float64 {
	// Ваша функция f(x) здесь
	return x*x - 2 // Пример: синус
}

// Функция для вычисления значения интерполяционного многочлена Pn(x)
func Pn(x []float64, y []float64, n int, xVal float64) float64 {
	return lagrangeInterpolation(x, y, n, xVal)
}

// Функция для вычисления значения невязки rn(x)
func residual(x float64, fVal float64) float64 {
	return math.Abs(f(x) - fVal)
}

// Метод секущих для решения уравнения Pn(x) = F
func secantMethod(x0 float64, x1 float64, F float64, x []float64, y []float64, n int, epsilon float64) (float64, error) {
	fx0 := Pn(x, y, n, x0) - F
	fx1 := Pn(x, y, n, x1) - F
	x2 := 0.0

	for math.Abs(x1-x0) >= epsilon {
		if fx1-fx0 == 0 {
			return 0, fmt.Errorf("division by zero")
		}
		x2 = x1 - fx1*(x1-x0)/(fx1-fx0)
		x0 = x1
		fx0 = fx1
		x1 = x2
		fx1 = Pn(x, y, n, x2) - F
	}
	return x2, nil
}
