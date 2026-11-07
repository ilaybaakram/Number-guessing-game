#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
    int secret_num;
    int guess;
    char option;

    /* Seed the random number generator once, at the start of the program. */
    srand((unsigned int)time(NULL));

    printf("----- NUMBER GUESSING GAME -----\n");

    do
    {
        secret_num = rand() % 100 + 1; /* A new secret number from 1 to 100 */
        printf("\nI've picked a number between 1 and 100. Can you guess it?\n");

        do
        {
            printf("Enter your guess (between 1-100): ");

            if (scanf("%d", &guess) != 1)
            {
                printf("Please enter a valid whole number.\n");
                while (getchar() != '\n')
                    ;
                guess = 0;
                continue;
            }

            if (guess < 1 || guess > 100)
            {
                printf("Invalid number! Your guess must be between 1 and 100.\n");
            }
            else if (guess == secret_num)
            {
                printf("\n🎊 YOU GOT IT! 🎊\n");
            }
            else
            {
                int difference = abs(secret_num - guess);

                if (guess < secret_num)
                    printf("A little higher! ");
                else
                    printf("A little lower! ");

                if (difference <= 5)
                    printf("You're VERY close! 💗\n");
                else if (difference <= 15)
                    printf("Getting warmer! ✨\n");
                else
                    printf("Not quite there yet. Keep trying!\n");
            }

        } while (guess != secret_num);

        printf("Congratulations! 🏆\n");
        printf("Do you want to play again? (Y for yes / N for no): ");
        scanf(" %c", &option);

    } while (option == 'Y' || option == 'y');

    printf("\nThank you for playing. Have a lovely day! 💜\n");
    return 0;
}
