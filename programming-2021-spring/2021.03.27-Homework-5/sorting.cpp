#include <iostream>

int maxElement(int* array, int size)
{
    int max = array[0];
    for (int i = 1; i < size; ++i)
    {
        if (array[i] > max) 
        {
            max = array[i];
        }
    }
    return max;
}

void countingSort(int* array, int size) 
{
    int k = maxElement(array, size);
 	int c[k+1] = { 0 };
 	for (int i = 0; i < size; ++i) 
    {
 		++c[array[i]];
 	}

 	int b = 0;
 	for (int i = 0; i < k + 1; ++i)
    {
 		for (int j = 0; j < c[i]; ++j) 
        {
 			array[b++] = i;
 		}
 	}
 }

void quickSort(int* array, int size) {
    int i = 0;
    int j = size - 1;
    int temp = 0;
    int p = array[size >> 1];

    do 
    {
        while (array[i] < p) i++;
        while (array[j] > p) j--;

        if (i <= j) 
        {
            //swap(array[i], array[j]);
            temp = array[i]; 
            array[i] = array[j]; 
            array[j] = temp;
            i++; 
            j--;
        }
    } while (i <= j);

    if (j > 0) quickSort(array, j);
    if (size > i) quickSort(array + i, size - i);
}

void merge(const int* cArray, const int* qArray, size_t cSize, size_t qSize, int* resultArray) {
    size_t i, j, k;
    i = j = k = 0;

    while (i < cSize && j < qSize) 
    {
        if (cArray[i] < qArray[j]) 
        {
            resultArray[k++] = cArray[i++];
        } else 
        {
            resultArray[k++] = qArray[j++];
        }
    }

    while (i < cSize) 
    {
        resultArray[k++] = cArray[i++];
    }
    while (j < qSize) 
    {
        resultArray[k++] = qArray[j++];
    }
}

void fillArray(int* array, int size)
{
    for (int i = 0; i < size; array[i] = rand() % 90 + 10, ++i);
}

void printArray(int* array, int size)
{
    for (int i = 0; i < size; std::cout << array[i] << ' ', ++i);
    std::cout << std::endl;
}

int main()
{
    size_t countingSize = 10;
    int* countingArray = new int[countingSize];
    fillArray(countingArray, countingSize);
    printArray(countingArray, countingSize);
    countingSort(countingArray, countingSize);
    printArray(countingArray, countingSize);

    std::cout << std::endl;

    size_t quickSize = 10;
    int* quickArray = new int[quickSize];
    fillArray(quickArray, quickSize);
    printArray(quickArray, quickSize);
    quickSort(quickArray, quickSize);
    printArray(quickArray, quickSize);

    std::cout << std:: endl;
    
    size_t mergeSize = countingSize + quickSize;
    int* mergeArray = new int[mergeSize];
    merge(countingArray, quickArray, countingSize, quickSize, mergeArray);
    printArray(mergeArray, mergeSize);

    delete[] countingArray;
    delete[] quickArray;
    delete[] mergeArray;

    return EXIT_SUCCESS;
}
