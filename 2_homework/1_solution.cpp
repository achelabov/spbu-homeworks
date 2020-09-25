#include <iostream>

void printReverseArray(int* &arr, int *count)
{
	for (int i = *count-1; i >= 0; --i)
	{
		std::cout << arr[i] << " ";
	}	
}

int sumArray(int* &arr, int *count)
{
	int sum = 0;
	for (int i = 0; i < *count; ++i)
	{
		sum += arr[i];
	}
	return sum;
}

int minElement(int* &arr, int *count)
{
	int min = arr[0];
	for (int i = 1; i < *count; ++i)
	{
		if(arr[i] < min)
		{
			min = arr[i];
		}
	}
	return min;
}

int maxElement(int* &arr, int *count)
{
	int max = arr[0];
	for (int i = 1; i < *count; ++i)
	{
		if(arr[i] > max)
		{
			max = arr[i];
		}
	}
	return max;
}

void addElement(int* &arr, int *count)
{
	std::cout << "Введите значение " << *count << " элемента массива" << std::endl; 
	std::cin >> arr[*count];
}

void printArray(int* &arr, int *capacity, int *count)
{
	for (int i = 0; i < *count; ++i)
	{
		std::cout << arr[i] << " ";
	}
}

void expandArray(int* &arr, int *capacity)
{
	int newCapacity = *capacity + 1;
	int* temp = new int[newCapacity];
	for (int j = 0; j < *capacity; ++j)
	{
		temp[j] = arr[j];
	}
	delete[] arr;
	arr = temp;
	*capacity = newCapacity;
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


int main()
{
	int capacity = 0;
	int *arr = new int[capacity];
	int num = 0;
	int count = 0;
	int isTrue = true;

	while (isTrue)
	{
		menu();
		std::cin >> num;
		
		if (count == capacity)
		{
			expandArray(arr, &capacity);
		
		}

		switch (num)
		{
			case 0:
			{
				isTrue = false;
				break;
			}
			case 1:
			{
				addElement(arr, &count);
				count++;
				break;
			}
			case 2:
			{
				printArray(arr, &capacity, &count);
				break;
			}
			case 3:
			{
				std::cout << "Max = " <<  maxElement(arr, &count) << std::endl;
				break;
			}
			case 4:
			{
				std::cout << "Min = " << minElement(arr, &count) << std::endl;
				break;
			}
			case 5:
			{
				std::cout << "Sum  = " << sumArray(arr, &count) << std::endl;
				break;
			}
			case 6:
			{
				printReverseArray(arr, &count); 
				break;
			} 
		
		}
	
	}
	delete[] arr;
	return EXIT_SUCCESS;
}
