#include <iostream>
#include "ArrayList.h"

using namespace std;

void printMenu()
{
	cout << "МЕНЮ" << endl;
	cout << "0 - Выход из программы" << endl;
	cout << "1 - Вывод списка в поток" << endl;
	cout << "2, 3 - Добавление элемента в конец списка" << endl;
	cout << "4 - Добавление элемента в начало списка" << endl;
	cout << "5 - Удаление последнего вхождения элемента" << endl;
	cout << "6 - Присвоение" << endl;
	cout << "7 - Сложение списков" << endl;
	cout << "8 - Удаление первого элемента из списка" << endl;
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
				cout << arr << endl;
				break;
			}
		case 2:
			{
				int element = 0;
				cin >> element;
				arr += element;
				break;
			}
		case 3:
			{
				int element = 0;
				cin >> element;
				arr = arr + element;
				break;
			}
		case 4:
			{
				int element = 0;
				cin >> element;
				arr = element + arr;
				break;
			}
		case 5:
			{
				int element = 0;
				cin >> element;
				arr -= element;
				break;
			}
		case 6:
			{
				ArrayList list;
				// list.add(...)
				arr = list;
				break;
			}
		case 7:
			{
				arr = arr + arr;
				break;
			}
		case 8:
			{
				int element = 0;
				cin >> element;
				arr = element - arr;
				break;
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
