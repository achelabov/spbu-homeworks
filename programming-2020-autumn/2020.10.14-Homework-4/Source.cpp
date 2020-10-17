#include<iostream>
#include<clocale>
#include<ctime>
#include"ArrayList.h"

using namespace std;

void printMenu()
{
	cout << "МЕНЮ" << endl;
	cout << "0 - Выход из программы" << endl;
	cout << "1 - Вывести массив на экран" << endl;
	cout << "2 - Добавить элемент" << endl;
	cout << "3 - Добавить элемент в позицию" << endl;
	cout << "4 - Удалить элемент по индексу" << endl;
	cout << "5 - Найти элемент" << endl;
	cout << "6 - Добавить несколько элементов" << endl;
	cout << "7 - Добавить несколько элементов, начиная с некоторой позиции" << endl;
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
			arr.print();
			break;
		}
		case 2:
		{
			int element = 0;
			std::cin >> element;
			arr.add(element);
			break;
		}
		case 3:
		{
			int index = 0;
			int element = 0;
			std::cin >> index >> element;
			arr.add(index, element);
			break;
		}
		case 4:
		{
			int index = 0;
			std::cin >> index;
			arr.remove(index);
			break;
		}
		case 5:
		{
			int element = 0;
			std::cin >> element;
			std::cout << arr.indexOf(element) << std::endl;
			break;
		}
		case 6:
		{
			int number = 0;
			std::cin >> number;
			for (int i = 0; i < number; ++i)
			{
				int element = 0;
				std::cin >> element;
				arr.add(element);
			}
			break;
		}
		case 7:
		{
			int number = 0;
			int index = 0;
			std::cin >> number >> index;
			for (int i = 0; i < number; ++i)
			{
				int element = 0;
				std::cin >> element;
				arr.add(index, element);
				++index;
			}
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
