package main

import (
	"fmt"
	"math"
)

// Функция для вычисления значения функции f(x)
func f(x float64) float64 {
	return math.Exp(6 * x) // Функция f(x) = e^(6x)
}

// Функция для вычисления первой производной f'(x) по формуле численного дифференцирования (центральная разность)
func firstDerivative(x, h float64) float64 {
	return (f(x+h) - f(x-h)) / (2 * h)
}

// Функция для вычисления второй производной f”(x) по формуле численного дифференцирования (центральная разность)
func secondDerivative(x, h float64) float64 {
	return (f(x+h) - 2*f(x) + f(x-h)) / (h * h)
}

func main() {
	var m int
	var a, h float64

	// Ввод параметров задачи
	fmt.Println("Введите количество узлов m:")
	fmt.Scanln(&m)

	fmt.Println("Введите начальное значение a:")
	fmt.Scanln(&a)

	fmt.Println("Введите шаг h:")
	fmt.Scanln(&h)

	// Вывод заголовка таблицы
	fmt.Println("Таблица значений функции, первой и второй производных:")
	fmt.Printf("%10s | %10s | %10s | %10s | %10s | %10s | %10s\n", "xi", "f(xi)", "f'(xi)", "|f'(xi) - f'(xi)|", "f''(xi)", "|f''(xi) - f''(xi)|")

	// Вывод значений функции и её производных в узлах xi таблицы
	for i := 0; i <= m; i++ {
		xi := a + float64(i)*h
		fi := f(xi)
		fiPrime := firstDerivative(xi, h)
		fiDoublePrime := secondDerivative(xi, h)

		// Истинные значения производных
		trueFiPrime := 6 * math.Exp(6*xi)
		trueFiDoublePrime := 36 * math.Exp(6*xi)

		// Погрешности
		diffFiPrime := math.Abs(trueFiPrime - fiPrime)
		diffFiDoublePrime := math.Abs(trueFiDoublePrime - fiDoublePrime)

		// Вывод строк таблицы
		fmt.Printf("%10.6f | %10.6f | %10.6f | %10.6f | %10.6f | %10.6f | %10.6f\n", xi, fi, fiPrime, diffFiPrime, fiDoublePrime, diffFiDoublePrime)
	}
}
