#include <stdio.h>

void printPairs(int arr[]){
    for(int i = 0; sizeof(*arr); i++){
        for(int j = 0; j < sizeof(*arr); j++){
            printf("%d %d\n", arr[i], arr[j]);
        }
    }
}

void foo(int arr[]){
    int sum = 0;
    int product = 1;
 
    for(int i = 0; i < sizeof(*arr); i++){
        sum += arr[i];
    }
    for(int i = 0; i < sizeof(*arr); i++){
        product *= arr[i];
    }

    printf("%d\n", sum);
    printf("%d\n", product);
}

int main(){
    int arr[] = {1, 2, 3, 4, 5};
    //foo(arr);

    printPairs(arr);
    return 0;


}
