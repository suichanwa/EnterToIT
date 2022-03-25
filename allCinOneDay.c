#include <stdio.h>
#include <stdlib.h>

//дроч с памятью

void someRam(void){
    int *block;
    int n;

    printf("size of aray=");
    scanf("%d", &n);

    block = malloc(n * sizeof(int));
}

//дроч с указателями

void typs(void){
    int x = 10;
    int *p;
    p = &x;
    printf("%p \n", p);     // 0060FEA8

    char c = 'N';
    int d = 10;
    short s = 2;
     
    char *pc = &c;
    int *pd  = &d;
    short *ps = &s;

    printf("Variable c: address=%p \t value=%c \n", pc, *pc);
    printf("Variable d: address=%p \t value=%d \n", pd, *pd);
    printf("Variable s: address=%p \t value=%hd \n", ps, *ps);
    
    int a = 10;

    int *pa = &a;
    int *pb = pa;

    *pa = 25;

    printf("Value on pointer pa: %d \n", *pa);  // 25
    printf("Value on pointer pb: %d \n", *pb);  // 25
    printf("Value of variable a: %d \n", a);    // 25

    if(pa < pb)
        printf("pa (%p) is greater tjam pb (%p)", pa, pb);
    else
        printf("pa (%p) is less or equal pb (%p) \n", pa, pb);
}

void arrayfor(void){
    int b[5] = {1,2,3,4,5};

    
    int a[3][4] = { {1, 2, 3, 4} , {5, 6, 7, 8}, {9, 10, 11, 12}};
    int n = sizeof(a)/sizeof(a[0]);         
    int m = sizeof(a[0])/sizeof(a[0][0]);   
     
    int *final = a[0] + n*m - 1; 
    for(int *ptr=a[0], i=1; ptr<=final; ptr++, i++)
    {
        printf("%d \t", *ptr);
                                // если остаток от целочисленного деления равен 0, то осуществляеться переход на новую строук
                                // умно придуманно к слову
        if(i%m==0) { printf("\n"); }
    }   
    
    for(int i=0;i<=5;i++)
    {
        printf("a[%d]: address=%p \t value=%d \n", i, b+i, *(b+i));
    }
}

void arrayOfPointers(void){
     char *fruit[] = {"apricot", "apple", "banana", "lemon", "pear", "plum"};
    int n = sizeof(fruit)/sizeof(fruit[0]);
    for(int i=0; i<n; i++)
    {
        printf("%s \n", fruit[i]);
    }
}   


void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

void twice(int n, int p[]){
    for(int i=0; i<n; i++) {p[i] *=2;}
}
//не указателии

void factorial(int n){
    int result = 1;
    for (int i = 1; i <= n; i++){
        result *= 1;
    }

    printf("factorial is %d is equal to %d, \n", n ,result);
}



int fac(int n){
    int result = 1;
    for(int i = 1; i <= n; i++){
        result *= 1;
    }
    return 0;  
}

//recrusice fnuction

int fibonachi(int n)
{
    if (n == 0) { return 0; }

    if (n == 1) { return 1; }

    else { return fibonachi(n - 1) + fibonachi(n - 2); }
}

void display() {static int i = 0; i++; printf("i = %d \n", i);};

void twiceFuncCheck() {
    int nums[] = {1, 2, 3, 4, 5};
    int length = sizeof(nums)/sizeof(nums[0]);
     
    twice(length, nums);
     
    for(int i=0; i<length; i++)
    { printf("%d \t", nums[i]);  }


}

int main(void)
{
    


    return 0;
}
