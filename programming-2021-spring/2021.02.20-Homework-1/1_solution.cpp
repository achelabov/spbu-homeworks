#include <iostream>

using namespace std;

char* printBits(void* data, size_t size)
{
	char* dest = new char[1 + 8 * size];
	char* ptr = dest;
	uint8_t* b = (uint8_t*)(data) + size - 1;
  

	for (size_t bit = 8 * size; bit--; ptr++)
	{
		*ptr = (*b & (1 << (bit & 7))) ? '1' : '0';
		if (!(bit % 8)) b--;
	} 
  
	dest[8 * size] = 0;
	return dest;
}

int main()
{
	cout << "Int: ";
	int i = 0;
	cin >> i;
	cout << printBits(&i, sizeof(i)) << endl;

	cout << "Long: ";
	long l = 0;
	cin >> l;
	cout << printBits(&l, sizeof(l)) << endl;
	
	cout << "Long long: ";
	long long ll = 0;
	cin >> ll;
	cout << printBits(&ll, sizeof(ll)) << endl;
	
	cout << "Float: ";
	float f = 0.0f;
	cin >> f;
	cout << printBits(&f, sizeof(f)) << endl;
	
	cout << "Double: ";
	double d = 0.0;
	cin >> d;
	cout << printBits(&d, sizeof(d)) << endl;

	cout << "Long double: ";
	long double ld = 0.0;
	cin >> ld;
	cout << printBits(&ld, sizeof(ld)) << endl;

	return 0;
}
