#include <iostream>
#include <cstdlib>

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

void output(int* arr, int count)
{
	for (int i = 0; i < count; ++i)
	{
		std::cout << arr[i] << " ";
	}
}

void addElements(int* &arr, int &count, int &capacity, int n, int a, int b)
{
<<<<<<< HEAD
=======
	int n, a, b;
	std::cin >> n >> a >> b;

>>>>>>> cff8254e61b647e5d61d40273e1a2692282a53da
	for (int i = 0; i < n; ++i)
	{
		expandArray(arr, capacity);
		arr[count] = a + rand() % (b - a);
		count++;
	}
}

void reverseArray(int* &arr, int count)
{
	for (int i = 0; i < count / 2; i++)
    	{
        	int tmp = arr[i];
       		arr[i] = arr[count-i-1];
        	arr[count-i-1] = tmp;
    	}
}

void swapElements(int* &arr, int count)
{
	for (int i = 1; i < count; i += 2)
	{
		int tmp = arr[i];
		arr[i] = arr[i-1];
		arr[i-1] = tmp;	
	}
}

void shiftArray(int* &arr, int count)
{
	int tmp = arr[count-1];
	
	for (int i = count - 1; i > 0; --i)
	{
		arr[i] = arr[i-1];
	}

	arr[0] = tmp;
}

void twoHalfsArray(int* &arr, int count, int n)
{
	for (int i = 0; i < n / 2; ++i)
	{
		int tmp = arr[i];
		arr[i] = arr[n-i-1];
		arr[n-i-1] = tmp;
	}

	for (int i = 0; i < (count - n - 1) / 2; ++i)
	{
		int tmp = arr[n+i+1];
		arr[n+i+1] = arr[count-i-1];
		arr[count-i-1] = tmp;
	}
}

void menu()
{
		std::cout << "\n0 - Выход из программы" << std::endl;
		std::cout << "1 - Добавить в массив n случайных чисел в промежутке от a до b (n, a, b вводится с клавиатуры)" << std::endl;
		std::cout << "2 - Развернуть массив" << std::endl;
		std::cout << "3 - Поменять элементы массива местами в парах" << std::endl;
		std::cout << "4 - Циклический сдвиг вправо на 1" << std::endl;
		std::cout << "5 - Развернуть две половинки массива. n - индекс элемента, разделяющего половинки" << std::endl;
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
			int n, a, b;
			std::cin >> n >> a >> b;
			addElements(arr, count, capacity, n, a, b);
			output(arr, count);
			break;
		}
		case 2:
		{
			reverseArray(arr, count);
			output(arr, count);
			break;
		}
		case 3:
		{
			swapElements(arr, count);
			output(arr, count);
			break;
		}
		case 4:
		{
			shiftArray(arr,count);
			output(arr, count);
			break;
		}
		case 5:
		{
			int n; 
			std::cin >> n;
			twoHalfsArray(arr, count, n);
			output(arr, count);
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
