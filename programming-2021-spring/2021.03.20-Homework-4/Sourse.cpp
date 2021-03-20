#include <iostream>

void swap(int& a, int& b)
{
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}

void printArray(int* arr, int length)
{
    for (int i = 0; i < length; std::cout << arr[i] << ' ', ++i);
    std::cout << std::endl;
}

void fillArray(int* arr, int length)
{
    for (int i = 0; i < length; arr[i] = rand() % 90 + 10, ++i);
}

void mixArray(int* arr, int length)
{
    for (int i = 0; i < length; swap(arr[i], arr[rand() % length]), ++i);
}

void printCount(int a, int b)
{
    std::cout << "Comparison's count: " << a / 1000 << std::endl;
    std::cout << "Permutation's count: " << b / 1000 << std::endl;
}

void bubbleSort(int* arr, int length, int& comparisonBubble, int& permutationBubble)
{
	for (int i = 0; i < length - 1; ++i)
	{
		for (int j = 0; j < length - i - 1; ++j)
        {
            ++comparisonBubble;
			if (arr[j] > arr[j + 1])
			{
			
                swap(arr[j], arr[j + 1]);
                ++permutationBubble;
            }
		}
	}
}

void insertionSort(int* a, int len, int& comparisonInsertion, int& permutationInsertion)
{
	for (int i = 1; i < len; ++i)
	{
		int t = a[i];
		int j = i;
		while (j > 0 && a[j - 1] > t)
		{
			++comparisonInsertion;
			a[j] = a[j - 1];
			--j;
		}
		a[j] = t;
		++permutationInsertion;
	}
}

void selectionSort(int* a, int len, int& comparisonSelection, int& permutationSelection)
{
	for (int i = 0; i < len - 1; ++i)
	{
		int index = i;
		for (int j = i + 1; j < len; ++j)
		{
			++comparisonSelection;
			if (a[j] < a[index])
			{
				index = j;
			}
		}
		swap(a[i], a[index]);
		++permutationSelection;
	}
}

void sort(int* arr, int length, int& comparison, int& permutation, void (*sortingFunction)(int*, int, int&, int&))
{
    for (int i = 0; i < 1000; ++i)
    {
        mixArray(arr, length);
        sortingFunction(arr, length, comparison, permutation);
    }
}

int main()
{
    for (int length = 5; length <= 20; length += 5)
    {
        int* arr = new int[length];
        fillArray(arr, length);

        std::cout << "Bubble sort:" << std::endl;
        int comparisonBubble = 0;
        int permutationBubble = 0;
        sort(arr, length, comparisonBubble, permutationBubble, bubbleSort);
        printCount(comparisonBubble, permutationBubble);

        std::cout << "Insertion sort:" << std::endl;
        int comparisonInsertion = 0;
        int permutationInsertion = 0;
        sort(arr, length, comparisonInsertion, permutationInsertion, insertionSort);
        printCount(comparisonInsertion, permutationInsertion);

        std::cout << "Selection sort:" << std::endl;
        int comparisonSelection = 0;
        int permutationSelection = 0;
        sort(arr, length, comparisonSelection, permutationSelection, selectionSort);
        printCount(comparisonSelection, permutationSelection);

        std::cout << std::endl;

        delete[] arr;
    }

    return EXIT_SUCCESS;
}
