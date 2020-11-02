#include "ArrayList.h"

ArrayList::ArrayList(const ArrayList& list)
{
	count = list.count;
	capacity = list.capacity;
	data = new int[capacity] { 0 };
	for (int i = 0; i < count; ++i)
	{
		data[i] = list.data[i];
	}
}

ArrayList::~ArrayList()
{
	delete[] data;
}

void ArrayList::expand()
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
		expand();					
	}
	data[count] = element;
	++count;
}

bool ArrayList::add(int index, int element)
{
	if (isCorrect(index, count) == false)
	{
		return false;
	}
	if (count == capacity)
	{
		expand();
	}
	for (int i = count; i > index; --i)
	{
		data[i] = data[i - 1];			
	}
	data[index] = element;
	++count;
	return true; 
}

bool ArrayList::addAll(ArrayList& list)
{
	while (capacity < count + list.count)
	{
		expand();
	}
	for (int i = 0; i < list.count; ++i)
	{
		add(list.get(i));
	}
	return list.count != 0;
}

bool ArrayList::addAll(int index, ArrayList& list)
{
	if (isCorrect(index, count) == false)
	{
		return false;
	}
	while (capacity < count + list.count)
	{
		expand();
	}
	for (int i = count - 1; i >= index; --i)
	{
		data[i + list.count] = data[i];
	}
	count += list.count;
	for (int i = 0; i < list.count; ++i)
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

bool ArrayList::set(int index, int element)
{
	if (isCorrect(index, count) == false)
	{
		return false;
	}
	data[index] = element;
	return true;
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
	for (int i = count - 1; i >= 0; --i)
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
	if (isCorrect(index, count) == false)
	{
		return false;
	}
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

int ArrayList::length()
{
	return count;
}

void ArrayList::operator+=(int item)
{
	add(item);
}

void ArrayList::operator-=(int item)
{
	remove(indexOf(item));
}

ArrayList& ArrayList::operator=(const ArrayList& list)
{
	count = list.count;
	capacity = list.capacity;
	data = new int[capacity] { 0 };
	for (int i = 0; i < count; ++i)
	{
		data[i] = list.data[i];
	}
	return *this; 
}

ArrayList operator+(const ArrayList& list, int item)
{
	ArrayList result;
	result.count = list.count;
	result.capacity = list.capacity;
	result.data = new int[list.capacity] { 0 };
	for (int i = 0; i < list.count; ++i)
	{
		result.data[i] = list.data[i];
	}
	result.add(item);
	return result;
}

ArrayList operator+(int item, const ArrayList& list)
{
	ArrayList result;
	result.count = list.count;
	result.capacity = list.capacity;
	result.data = new int[list.capacity] { 0 };
	for (int i = 0; i < list.count; ++i)
	{
		result.data[i] = list.data[i];
	}
	result.add(0, item);
	return result;
}

ArrayList operator+(const ArrayList& list1, const ArrayList& list2)
{
	ArrayList result;
	result.count = list1.count + list2.count;
	result.capacity = list1.capacity + list2.capacity;
	result.data = new int[result.capacity] { 0 };
	for (int i = 0; i < list1.count; ++i)
	{
		result.data[i] = list1.data[i];
	}
	for (int i = list1.count; i < result.count; ++i)
	{
		result.data[i] = list2.data[i - list1.count];
	}
	return result;
} 

ArrayList operator-(int item, const ArrayList& list)
{
	ArrayList result;
	result.count = list.count;
	result.capacity = list.capacity;
	result.data = new int[list.capacity] { 0 };
	for (int i = 0; i < list.count; ++i)
	{
		result.data[i] = list.data[i];
	}
	result.remove(result.indexOf(item));
	return result;
}

std::ostream& operator<<(std::ostream& stream, const ArrayList& list)
{
	for (int i = 0; i < list.count; ++i)
	{
		stream << list.data[i] << " ";
	}
	return stream;
}
