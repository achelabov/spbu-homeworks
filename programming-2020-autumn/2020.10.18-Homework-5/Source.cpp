#include <iostream>
#include "ArrayList.h"
#include <cstdlib>

using namespace std;

void printMenu()
{
	cout << "МЕНЮ" << endl;
	cout << "0 - Выход из программы" << endl;
	cout << "1 - Добавить в список 10 случайных положительных двузначных чисел" << endl;
	cout << "2 - Добавить в список 10 случайных отрицательных чисел" << endl;
	cout << "3 - Поменять местами первый минимальный и последний максимальный элемент" << endl;
	cout << "4 - Перемешать все элементы массива" << endl;
	cout << "5 - Заменить каждый отрицательный элемент массива на 0" << endl;
}

void processChoice(ArrayList& arr, int choice)
{
	switch (choice)
	{
		case 0:
			{
				exit(0);
			}
		case 1:
			{
				int min = 10;
				int max = 99;
				for (int i = 0; i < 10; ++i)
				{
					arr.add(rand() % (max - min + 1) + min);
				}
				cout << arr.toString() << endl;
				break;
			}
		case 2:
			{
				int min = -99;
				int max = -10;
				for (int i = 0; i < 10; ++i)
				{
					arr.add(rand() % (max - min + 1) + min);
				}
				cout << arr.toString() << endl;
				break;
			}
		case 3:
			{
				int min = arr.get(0);
				int minIndex = 0;
				for (int i = 0; i < arr.length(); ++i)
				{
					if (arr.get(i) < min)
					{
						min = arr.get(i);
						minIndex = i;
					}

				}
				int max = arr.get(0);
				int maxIndex = 0;
				for (int i = 0; i < arr.length(); ++i)
				{
					if (arr.get(i) >= max)
					{
						max = arr.get(i);
						maxIndex = i;
					}

				}
				arr.swap(minIndex, maxIndex);
				cout << arr.toString() << endl;
				break;
			}
		case 4:
			{
				bool isUsed[arr.length()] =  { 0 };
				for (int i = 0; i < arr.length(); ++i)
				{
					int rnd = rand() % (arr.length() - i + 1) + i;
					if (isUsed[rnd])
					{
						arr.swap(i, rnd);
						isUsed[rnd] = true;
					} else
					{
						--i;
					}
				}
				cout << arr.toString() << endl;
				break;
			}
		case 5:
			{
				for (int i = 0; i < arr.length(); ++i)
				{
					if (arr.get(i) < 0)
					{
						arr.set(i, 0);
					}
				}
				cout << arr.toString() << endl;
			}
	}

}

int main()
{
	ArrayList a;
	int choice = 0;

	do
	{
		printMenu();
		cin >> choice;
		processChoice(a, choice);

	} while (choice != 0);

	return EXIT_SUCCESS;
}
