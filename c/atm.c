#include <stdio.h>
#include <stdbool.h>


int main(){

    int pin = 7788, user_pin;
    double balance = 500.00; // 500$
    int attempts = 0;
    int option;
    double withdraw;

    while (attempts < 3){
        printf("Enter PINCODE: ");
        scanf("%d", &user_pin);

        if (user_pin == pin){
            break;
        } else {
            attempts++;
            printf("Incorrect PIN! Attempts left: %d\n", 3 - attempts);
        }

        if (attempts == 3){
            printf("Your Card is Blocked!\n");
            return 0;
        }

    }

    while (1){
        printf("\n1 - View Balance\n2 - Withdraw Money\n0 - Exit\n\n>> ");
        scanf(" %d", &option);

        if (option == 0){
            printf("Goodbye!\n");
            break;
        } else if (option == 1){
            printf("\nBalance: $%.2f\n", balance);
        } else if (option == 2){
            printf("Enter amount to withdraw: ");
            scanf("%lf", &withdraw);

            if (withdraw > balance){
                printf("Insufficient!\n");
            } else if (withdraw <= 0){
                printf("Invalid amount!\n");
            } else {
                balance -= withdraw;
                printf("\nSuccess! Balance: $%.2f\n", balance);
            }

        } else {
            printf("Invalid!\n");
        }
    }
    return 0;
}
