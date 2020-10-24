#include <iostream>
#include "ArrayList.h"

using namespace std;

void printMenu()
{
	cout << "МЕНЮ" << endl;
	cout << "0 - Выход из программы" << endl;
	cout << "1 - Добавить элемент" << endl;
	cout << "2 - Вывести массив" << endl;
	cout << "3 - Проверить, является ли массив симметричным" << endl;
	cout << "4 - Циклический сдвиг массива на n элементов. n>0 - сдвиг вправо, n<0 - сдвиг влево" << endl;
	cout << "5 - Проверить, может ли массив стать симметричным, если из него удалить один элемент" << endl;
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
				int element = 0;
				cin >> element;
				arr.add(element);
				break;
			}
		case 2:
			{
				cout << arr.toString() << endl;
				break;
			}
		case 3:
			{
				bool isTrue = true;
				for (int i = 0; i < (arr.length() - 1) / 2; ++i)
				{
					if (arr.get(i) != arr.get(arr.length() - 1 - i))
					{
						isTrue = false;
					}
				}
				if (isTrue == true) 
				{ 
					cout << "Является" << endl; 
				} else 
				{
					cout << "Не является" << endl;
				}
				break;
			}
		case 4:
			{
				int n = 0;
				cin >> n;
				if (n < 0)
				{	
					for (int i = 0; i < -n % arr.length(); ++i)
					{
						int buff = 0;
						buff = arr.get(0);
						for(int j = 0; j < arr.length() - 1; ++j)
						{
							arr.set(j, arr.get(j + 1));
						}
						arr.set(arr.length() - 1, buff);
					}
				}
				if (n > 0)
				{
					for (int i = 0; i < n % arr.length(); ++i)
					{
						int buff = 0;
						buff = arr.get(arr.length() - 1);
						for(int j = arr.length() - 1; j > 0; --j)
						{
							arr.set(j, arr.get(j - 1));
						}
						arr.set(0, buff);
					}
				}
				break;
			}
		case 5:
			{
				bool isSymmetrical = false;
				for (int i = 0; i < arr.length(); ++i)
				{
					int mem = arr.get(i);
					arr.remove(i);
					bool isTrue = true;
					for (int i = 0; i < (arr.length() - 1) / 2; ++i)
					{
						if (arr.get(i) != arr.get(arr.length() - 1 - i))
						{
							isTrue = false;
							break;
						}
					}
					arr.add(i, mem);
					if (isTrue)
					{
						isSymmetrical = true;
						break;
					}
				}
				if (isSymmetrical == true) 
				{ 
					cout << "Может" << endl; 
				} else 
				{
					cout << "Не может" << endl;
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
