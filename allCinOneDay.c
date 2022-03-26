#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>

//structs



struct time
{
    int hour;
    int minute;
    int second;
};

struct time addminutes(struct time, int);

int timeTest(void){
    struct time addminutes(struct time, int);
     struct time current_time = {17, 38, 10};
    int minutes = 21;

    struct time result_time = addminutes(current_time, minutes);
    printf("%d:%d:%d \n", result_time.hour, result_time.minute, result_time.second);

    result_time = addminutes(current_time, 23);
    printf("%d:%d:%d \n", result_time.hour, result_time.minute, result_time.second);

    result_time = addminutes(current_time, 382);
    printf("%d:%d:%d \n", result_time.hour, result_time.minute, result_time.second);
    return 0;
}

struct time addminutes(struct time t, int minutes)
{
    struct time result ={t.hour, t.minute, t.second};
    int h, d;
    if(result.minute >=60)
    {
        h = result.minute / 60;
        result.minute -= 60 * h;
        result.hour +=h;
    }
    if(result.hour >=24)
    {
        d = result.hour / 24;
        result.hour -= 24 * d;
    }
    return result;
}


struct company
{
    char name[20];
    char country[30];
};

struct smartphone
{
    char title[20];
    int price;
    struct company manufacturer;
};

void workWithStructures(){
    struct smartphone phone = {"iPhone 8", 56000, "Apple", "USA"};
    printf("Enter phone title: ");
    scanf("%20s", &phone.title);
    printf("Enter price: ");
    scanf("%d", &phone.price);
    printf("Enter manufacturer: ");
    scanf("%s", &phone.manufacturer.name);
    printf("Enter country: ");
    scanf("%s", &phone.manufacturer.country);
}

//дроч с памятью

void display(char* format, ...)
{
    int d; 
    double f;
    va_list factor;         // указатель на необязательный параметр
    va_start(factor, format);   // устанавливаем указатель
     
    for(char *c = format;*c; c++)
    {
        if(*c!='%')
        {
            printf("%c", *c);
            continue;
        }
        switch(*++c)
        {
            case 'd': 
                d = va_arg(factor, int);
                printf("%d", d);
                break;
            case 'f': 
                f = va_arg(factor, double);
                printf("%.2lf", f);
                break;
            default:
                printf("%c", *c);
        }
    }
    va_end(factor);
}



int sum(int n, ...)
{
    int result = 0;
    // получаем указатель на параметр n
    for(int *ptr = &n; n>0; n--)
    {
        result+= *(++ptr);
    }
    return result;
}

void dynamicRam(void){
    int **table;
    int *row;

    int rowscount,  d;

    printf("Rows count=");
    scanf("%d", &rowscount);

    table = calloc(rowscount, sizeof(int*));
    row = malloc(sizeof(int)*rowscount);

    for(int i = 0; i < rowscount; i++){
        printf("\nColumns count for row %d=", i);
        scanf("%d", &row[i]);
        table[i] = calloc(row[i], sizeof(int));

        for(int j = 0; j = row[i]; j++){
            printf("table[%d][%d]=", i, j);
            scanf("%d", &d);
            table[i][j] = d;
        }
    }

    printf("\n");

    for(int i = 0; i < rowscount; i++){
        printf("%d");

        for(int j = 0; j<row[i]; j++)
        {printf("%d \t", table[i][j]);}
        free(table[i]);
    }

    free(table);
    free(row);

}


void vec(void){
    //it works like vetors in c++

    int *block;
    int n;

    printf("size of aray=");
    scanf("%d", &n);

    block = malloc(n * sizeof(int));
    
    for(int i = 0; i < 9; i++){
        printf("block[%d]=", i);
        scanf("%d", &block[i]);
    } 

    free(block);
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

void twiceFuncCheck() {
    int nums[] = {1, 2, 3, 4, 5};
    int length = sizeof(nums)/sizeof(nums[0]);
     
    twice(length, nums);
     
    for(int i=0; i<length; i++)
    { printf("%d \t", nums[i]);  }


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

void displa() {static int i = 0; i++; printf("i = %d \n", i);};

int main(void)
{   
    timeTest();
        
    return 0;
}
