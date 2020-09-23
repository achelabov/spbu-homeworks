#include <iostream>
#define MAX_NUM 999999

void tickets(int n)
{
//	int size = 7;
//	char* num = (char*)malloc(sizeof(char) * size); 
	int i, j, k;
	int num[7];
	char output[7] = "000000";
	for(i = 0; i < MAX_NUM; ++i)
	{
		for(k = i, j = 0; j < 6; ++j, k /= 10)
		{
			num[j]= k%10;
			output[j] = k%10 + '0';
//			*(num+j)=(char)(k%10);
		}
//		*(num+6)='\0';
		if(num[0]+num[1]+num[2] == n && num[3]+num[4]+num[5] == n)
		{
			std::cout << output << std::endl;
		}
	}
//	free(num);
}

int main()
{
	int n;
	std::cin >> n;
	tickets(n);
	return EXIT_SUCCESS;
}
