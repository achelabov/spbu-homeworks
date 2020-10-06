#include <iostream>
#include <cstdlib>

int* initArray(int capacity = 10)
{
	int* result = new int[capacity + 2]{ 0 };
	*(result + 1) = capacity;
	result += 2;
	return result;
}

void deleteArray(int* arr)
{
	delete[](arr - 2);
}

void expandArray(int* &arr)
{
	int* temp = initArray(2 * (*(arr - 1)));
	for (int i = 0; i < *(arr - 1); ++i)
	{
		*(temp + i) = *(arr + i);
	}
	*(temp - 2) = *(arr - 2);
	deleteArray(arr);
	arr = temp;
}

void addElement(int*& arr, int element)
{
	if (*(arr - 2) == *(arr - 1))
	{
		expandArray(arr);
	}
	*(arr + *(arr - 2)) = element;
	++(*(arr - 2));
}

void addRandomElements(int* &arr, int n, int min, int max)
{
	for (int i = 0; i < n; ++i)
	{
		addElement(arr, rand() % (max - min + 1) + min);
	}
}

void printArray(int* arr)
{
	std::cout << "[" << *(arr - 2) << "/" << *(arr - 1) << "] {";
	for (int i = 0; i < *(arr - 2); ++i)
	{
		std::cout << *(arr + i) << (i == *(arr - 2) - 1 ? "}\n" : ", ");
	}
}

void addElements(int* &arr, int count)
{
	for (int i = 0; i < count; ++i)
	{
		int element = 0;
		std::cout << "Введите значение " << i << " элемента" << std::endl;
		std::cin >> element;
		addElement(arr, element);
	}
}

int search(int* arr, int element, int start = 0)
{
	for (int i = 0; i < *(arr - 2); ++i)
	{
		if (*(arr + i) == element)
		{
			return i;
		}
	}
	return -1;
}

void add(int* &arr, int* addedArr)
{
	int i = 0;
	int j = 0;
	for (i = *(arr - 2), j = 0; i < (*(arr - 2) + *(addedArr - 2)); ++i, ++j)
	{
		if (*(arr - 2)  == *(arr - 1))
		{
			expandArray(arr);
		}
		*(arr + i) = *(addedArr + j);
	}
	*(arr - 2) += *(addedArr - 2);
}

int extract(int* &arr, int index)
{
	int indexElement = *(arr + index);

	for (int i = index + 1; i < *(arr - 2); ++i)
	{
		*(arr + i - 1) = *(arr + i); 
	}

	--(*(arr - 2));
	return index >= *(arr - 2) || index < 0 ? 1 : indexElement;
}

int insert(int* &arr, int index, int element)
{
	if (*(arr - 2) == *(arr - 1))
	{
		expandArray(arr);
	}

	for (int i = *(arr - 2); i > index; --i)
	{
		*(arr + i) = *(arr + i - 1);
	}

	*(arr + index) = element;
	++(*(arr - 2));
	return index >= *(arr - 2) || index < 0 ? 1 : 0;
}

int deleteGroup(int* &arr, int startIndex, int count = 1)
{
	for (int i = startIndex; i < startIndex + count; ++i)
	{
		extract(arr, i);
	}
	return startIndex >= *(arr - 2) || startIndex < 0 ? 1 : 0;
}

int* unify(int* a, int* b)
{
	int i = 0;
	int j = 0;
	int k = 0;
	int count = *(a - 2) + *(b - 3);
	int* arr = initArray(count);
	*(arr - 2) = count;
	for (i = 0, j = 1, k = 0; i < count; i += 2, j += 2, ++k)
	{
		*(arr + i) = *(a + k);
		*(arr + j) = *(b + k);
	}
	printArray(arr);
	return arr;
}

int subSequence(int* a, int* b)
{
	int output = -1;
	int i = 0;
	while (search(a, *b, i) <= (*(a - 2) - *(b - 2)))
	{
		output = search(a, *b, i);
		for (int j = 0; j < *(b - 2); j++)
		{
			if (*(a + search(a, *b, i) + j) != *(b + j))
			{
				output = -1;
			}
		}
		if (output != -1)
		{
			return output;
		}
		++i;
	}

	return output;
}
void menu()
{
	std::cout << "МЕНЮ" << std::endl;
	std::cout << "0 - Выход из программы" << std::endl;
	std::cout << "1 - Ввести несколько элемнетов с клавиатуры" << std::endl;
	std::cout << "2 - Добавить в массив n случайных чисел в промежутке от a до b(n, a, b вводится с клавиатуры)" << std::endl;
	std::cout << "3 - Вывести массив на экран" << std::endl;
	std::cout << "4 - Поиск индекса элемента" << std::endl;
	std::cout << "5 - Добавление массив к массиву" << std::endl;
	std::cout << "6 - Объединение массивов" << std::endl;
	std::cout << "7 - Вставка элемента в массив" << std::endl;
	std::cout << "8 - Удаление нескольких подряд идущих элементов массива" << std::endl;
	std::cout << "9 - Поиск подпоследовательности" << std::endl;
}

int*& choiceArray(int* &firstArray, int* &secondArray)
{
	int choice = 0;
	std::cout << "С каким массивом вы хотите работать? (1,2)" << std::endl;
	std::cin >> choice;
	return choice == 1 ? firstArray : secondArray;
}

void processInput(int* &firstArray, int* &secondArray, int input, bool &isTrue)
{
	int* &arr = choiceArray(firstArray, secondArray);
	switch (input)
	{
		case 0:
		{
			isTrue = false;
			break;
		}
		case 1:
		{
			int count = 0;
			std::cout << "Введить кол-во элементов" << std::endl;
			std::cin >> count;
			addElements(arr, count);
			break;
		}
		case 2:
		{
			int n = 0;
			int a = 0;
			int b = 0;
			std::cin >> n >> a >> b;
			addRandomElements(arr, n, a, b);
			break;
		}
		case 3:
		{
			printArray(arr);
			break;
		}
		case 4:
		{
			int element = 0;
			int start = 0;
			std::cout << "Введите значение элемента, индекс которого хотите найти" << std::endl;
			std::cin >> element;
			std::cout << "С какого элемента начать поиск?" << std::endl;
			std::cin >> start;
			std::cout << search(arr, element) << std::endl;
			break;
		}
		case 5:
		{
			add(firstArray, secondArray);
			break;
		}
		case 6:
		{
			unify(firstArray, secondArray);
			break;
		}
		case 7:
		{
			int index = 0;
			int element = 0;
			std::cout << "Введите индекс элемента" << std::endl;
			std::cin >> index;
			std::cout << "Введите значение " << index << " элемента" << std::endl;
			std::cin >> element;
			insert(arr, index, element);	
			break;
		}
		case 8:
		{
			int startIndex = 0;
			int count = 0;
			std::cout << "Введите индекс элемента" << std::endl;
			std::cin >> startIndex;
			std::cout << "Введите кол-во чисел" << std::endl;
			std::cin >> count;
			deleteGroup(arr, startIndex, count);	
			break;
		}
		case 9:
		{
			std::cout << subSequence(firstArray, secondArray) << std::endl;
		}
	}
}

int main()
{
	int* firstArray = initArray(10);
	int* secondArray = initArray(10);
	bool isTrue = true;
	int input = 0;

	while (isTrue)
	{
		menu();
		std::cin >> input;

		processInput(firstArray, secondArray, input, isTrue);
	}		
	deleteArray(firstArray);
	deleteArray(secondArray);
	return EXIT_SUCCESS;
}
