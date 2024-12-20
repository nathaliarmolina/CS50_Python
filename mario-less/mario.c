#include <cs50.h>
#include <stdio.h>

int main(void)
{

    int h = 0;
    int i, j, k;

    {

        do
        {
            h = get_int("Height: ");
        }
        while (h < 1 || h > 8);

        for (i = 1; i <= h; i++)
        {
            for (j = h - i; j >= 1; j--)
            {
                printf(" ");
            }
            for (k = 1; k <= i; k++)
            {
                printf("#");
            }

            printf("\n");
        }
    }
}