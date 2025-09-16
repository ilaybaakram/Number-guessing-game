#include <stdio.h>
int main()
{
    int secret_num = 42;
    int guess;
    char option;

    printf("-----NUMBER GUESSING GAME-----\n");

    do
    {
        do
        {
            printf("Enter your guess (between 1-100): ");
            scanf("%d", &guess);

            if (guess == secret_num)
            {
                printf("🎊YOU GOT IT🎊\n");
            }
            else if (guess >= 1 && guess <= 20)
            {
                printf("TOO LOW.....\n");
            }
            else if (guess >= 21 && guess <= 29)
            {
                printf("CLOSE.....\n");
            }
            else if (guess >= 30 && guess <= 39) 
            {
                printf("SLIGHTLY LOW.....\n");
            }
            else if (guess >= 40 && guess <= 45)
            {
                printf("VERY CLOSE.....\n");
            }
            else if (guess >= 46 && guess <= 54)
            {
                printf("CLOSE.....\n");
            }
            else if (guess >= 55 && guess <= 100)
            {
                printf("TOO HIGH.....\n");
            }
            else
                printf("INVALID NUMBER!!! (Must be between 1-100)\n");

        } while (guess != secret_num);

        printf("CONGRATULATIONS🏆\n");
        printf("Do you want to want to play again (Y for yes : N for no)");
        scanf(" %c", &option);

    } while (option == 'Y' || option == 'y');

    printf("Thank you for playing NUMBER GUESSING GAME!!!\n");

    return 0;
}