#include "ArrayList.h"
#include "cassert"

ArrayList::ArrayList()
{
	count = 0;
	capacity = 10;
	data = new int[10];
}

ArrayList::~ArrayList()
{
	delete[] data;
}

void expand(int*& data, int& capacity)
{
	int* newData = new int[capacity * 2];
	for (int i = 0; i < capacity; ++i)
	{
		newData[i] = data[i];
	}
	delete[] data;
	data = newData;
	capacity *= 2;
}

bool isCorrect(int index, int count)
{
	return index < count && index >= 0;
}

void ArrayList::add(int element)
{
	if (count == capacity)
	{
		expand(data, capacity);
	}
	data[count] = element;
	++count;
}

bool ArrayList::add(int index, int element)
{
	assert(isCorrect(index, count));
	int indexElement = data[index];
	if (count == capacity)
	{
		expand(data, capacity);
	}
	for (int i = count; i > index; --i)
	{
		data[i] = data[i - 1];
	}
	data[indexElement] = element;
	++count;
	return true; 
}

bool ArrayList::addAll(ArrayList& list)
{
	for (int i = 0; i < list.count; ++i)
	{
		if (count == capacity)
		{
			expand(data, capacity);
		}
		data[count + i] = list.data[i];
	}
	return list.count != 0;
}

bool ArrayList::addAll(int index, ArrayList& list)
{
	assert(isCorrect(index, count));
	while (capacity < count + list.count)
	{
		expand(data, capacity);
	}
	for (int i = count + list.count; i > index; --i)
	{
		data[i] = data[i - 1];
	}
	for (int i = 0; i < count + list.count - index; ++i)
	{
		data[index + i] = list.data[i];
	}
	return true;
}

bool ArrayList::contains(int element)
{
	int isContains = false;
	for (int i = 0; i < count; ++i)
	{
		if (data[i] = element)
		{
			isContains = true;
			break;
		}
	}
	return isContains;
}

int ArrayList::get(int index)
{
	return index < count && index >= 0 ? data[index] : -1;
}

void ArrayList::clear()
{
	count = 0;
	capacity = 10;
	delete[] data;
	data = new int[10];
}

int ArrayList::indexOf(int element)
{
	int index = -1;
	for (int i = 0; i < count; ++i)
	{
		if (data[i] == element)
		{
			index = i;
		}
	}
	return index;
}

bool ArrayList::isEmpty()
{
	return count == 0;
}

bool ArrayList::remove(int index)
{
	assert(isCorrect(index, count));
	for (int i = index; i < count; ++i)
	{
		data[i] = data[i + 1];
	}
	--count;
	return true;
}

bool ArrayList::swap(int index1, int index2)
{
	int tmp = data[index1];
	data[index1] = data[index2];
	data[index2] = tmp;
	return index1 < count && index2 < count && index1 >= 0 && index2 >= 0;
}

void ArrayList::print()
{
	printf("[%d/%d]{", count, capacity);
	for (int i = 0; i < count; ++i)
	{
		printf("%d%s", data[i], (i == count - 1? "" : ", "));
	}
	printf("}\n");
}