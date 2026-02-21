// usage: ./zeropadtext 16 abcd 
// 000000000000abcd
// zeropadtext 8 abcd
// 0000abcd

#include <stdio.h>
#include <stdlib.h>
int print_padleftzeroes(const char *s, size_t width)
{
    size_t n = strlen(s);
    if(width < n)
        return -1;
    while(width > n)
    {
        putchar('0');
        width--;
    }
    fputs(s, stdout);
    putchar('\n');
    return 0;
}
int main(int argc, char** argv) {
	print_padleftzeroes(argv[2],atoi(argv[1]));
}
