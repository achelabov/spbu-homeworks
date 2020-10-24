#include "ArrayList.h"

ArrayList::ArrayList(const ArrayList& list)
{
	count = list.count;
	capacity = list.capacity;
	data = list.data;
	str = nullptr;
}

ArrayList::~ArrayList()
{
	if (str != nullptr)
	{
		delete[] str;
	}
	delete[] data;
}

int ArrayList::numLength(int number)
{
	int result = 0;
	while (number % 10 != 0)
	{
		number /= 10;
		++result;
	}
	return result != 0 ? result : -1;
}

void ArrayList::addSymbolToStr(int& index, char symbol)
{
	str[index] = symbol;
	++index;
}

void ArrayList::addNumberToStr(int& index, int number)
{
	int length = numLength(number);
	for (int i = 0; i < length; ++i)
	{
		int digit = number % 10;
		str[index + length - 1 - i] = '0' + digit;
		number /= 10;
	}
	index += length;
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

char* ArrayList::toString()
{
	if (str != nullptr)
	{
		delete[] str;
		str = nullptr;
	}
	int countNum = 0;
	int countSymbol = 0;
	for (int i = 0; i < count; ++i)
	{
		countNum += numLength(data[i]);
		if (data[i] < 0)
		{
			countSymbol += 1;
		}
		if (i != count - 1)
		{
			countSymbol += 2;
		}
	}
	int length = 7 + numLength(count) + numLength(capacity) + countNum + countSymbol; //7 = [/] {}'\0'
	str = new char[length];
	int index = 0;
	addSymbolToStr(index, '[');
	addNumberToStr(index, count);
	addSymbolToStr(index, '/');
	addNumberToStr(index, capacity);
	addSymbolToStr(index, ']');
	addSymbolToStr(index, ' ');
	addSymbolToStr(index, '{');
	for (int i = 0; i < count; ++i)
	{
		if (data[i] >= 0)
		{	
			addNumberToStr(index, data[i]);
		} else
		{
			addSymbolToStr(index, '-');
			addNumberToStr(index, -data[i]);
		}
		if (i != count - 1)
		{
			addSymbolToStr(index, ',');
			addSymbolToStr(index, ' ');
		}
	}
	addSymbolToStr(index, '}');
	addSymbolToStr(index, '\0');
	return str;
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
	int indexElement = data[index];
	if (count == capacity)
	{
		expand();
						
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

	}	return true;
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

