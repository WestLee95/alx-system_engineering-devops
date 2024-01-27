#include <stdio.h>

int main()
{
	const char *fizz = "Fizz";

	for(int i = 1; i <= 100; i++;)
	{
		if(i % 3 == 0)
		{
			printf("%s\n", fizz);
		}
		else
		{
			printf("%d\n", i);
		}

		return 0;
	}
}
