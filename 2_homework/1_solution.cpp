#include <iostream>


void expandArray(int* &arr, int &capacity)
{
	int newCapacity = capacity + 1;
	int* temp = new int[newCapacity];
	for (int j = 0; j < capacity; ++j)
	{
		temp[j] = arr[j];
	}
	delete[] arr;
	arr = temp;
	capacity = newCapacity;
}

void printReverseArray(int* arr, int count)
{
	for (int i = count-1; i >= 0; --i)
	{
		std::cout << arr[i] << " ";
	}	
}

int sumArray(int* arr, int count)
{
	int sum = 0;
	for (int i = 0; i < count; ++i)
	{
		sum += arr[i];
	}
	return sum;
}

int minElement(int* arr, int count)
{
	int min = arr[0];
	for (int i = 1; i < count; ++i)
	{
		if(arr[i] < min)
		{
			min = arr[i];
		}
	}
	return min;
}

int maxElement(int* arr, int count)
{
	int max = arr[0];
	for (int i = 1; i < count; ++i)
	{
		if(arr[i] > max)
		{
			max = arr[i];
		}
	}
	return max;
}

void addElement(int* &arr, int &count, int &capacity)
{
	expandArray(arr, capacity);
	std::cout << "Введите значение " << count << " элемента массива" << std::endl; 
	std::cin >> arr[count];
	count++;
}

void printArray(int* arr, int count)
{
	for (int i = 0; i < count; ++i)
	{
		std::cout << arr[i] << " ";
	}
}


void menu()
{
		std::cout << "\n0 - Выход из программы" << std::endl;
		std::cout << "1 - Добавить число в массив" << std::endl;
		std::cout << "2 - Вывести массив на экран" << std::endl;
		std::cout << "3 - Найти номер максимального элемента массива" << std::endl;
		std::cout << "4 - Найти минимальный элемент массива" << std::endl;
		std::cout << "5 - Посчитать сумму элементов массива" << std::endl;
		std::cout << "6 - Вывести массив в обратном порядке\n" << std::endl;
}

void processInput(int* &arr, int &capacity, int &count, bool &isTrue, int num)
{
	switch (num)
	{
		case 0:
		{
			isTrue = false;
			break;
		}
		case 1:
		{
			addElement(arr, count, capacity);
			break;
		}
		case 2:
		{
			printArray(arr, count);
			break;
		}
		case 3:
		{
			std::cout << "Max = " <<  maxElement(arr, count) << std::endl;
			break;
		}
		case 4:
		{
			std::cout << "Min = " << minElement(arr, count) << std::endl;
			break;
		}
		case 5:
		{
			std::cout << "Sum = " << sumArray(arr, count) << std::endl;
			break;
		}
		case 6:
		{
			printReverseArray(arr, count); 
			break;
		} 
	}
}

int main()
{
	int capacity = 0;
	int *arr = new int[capacity];
	int num = 0;
	int count = 0;
	bool isTrue = true;

	while (isTrue)
	{
		menu();
		std::cin >> num;
		
		processInput(arr, capacity, count, isTrue, num);
	}
	delete[] arr;
	return EXIT_SUCCESS;
}
