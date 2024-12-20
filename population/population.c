#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size

    int start;
    int end;
    int years = 0;

    do
    {

        start = get_int("Start Size of Llamas: ");
    }

    while (start < 9);

    // TODO: Prompt for end size

    do
    {

        end = get_int("End Size of Llamas: ");
    }

    while (end < start);

    // TODO: Calculate number of years until we reach threshold

    while (start < end)
    {

        start = start + (start / 3) - (start / 4);
        years++;
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
