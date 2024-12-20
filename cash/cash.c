#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents); // 25 c
int calculate_dimes(int cents);    // 10 c
int calculate_nickels(int cents);  // 5 c
int calculate_pennies(int cents);  // 1c

int c;

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    do
    {
        c = get_int("Total cents: ");
    }

    while (c < 1);

    return c;
}

int calculate_quarters(int cents)
{
    int quarters = cents / 25;
    if (quarters > 0)
    {
        printf("%i\n", quarters);
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = cents / 10;
    if (dimes > 0)
    {
        printf("%i\n", dimes);
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = cents / 5;
    if (nickels > 0)
    {
        printf("%i\n", nickels);
    }
    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = cents / 1;
    if (pennies > 0)
    {
        printf("%i\n", pennies);
    }
    return pennies;
}
