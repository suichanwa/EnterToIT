using System;

namespace HelloWorldIGuess
{
    class Program
    {
        static void Main()
        {
            int num1 = ActualCalcs.GetUserInput();
            int num2 = ActualCalcs.GetUserInput();

            ActualCalcs.ModifyNumbers(ref num1, ref num2);

            int result = DisplayingResults.PerformOperation(num1, num2);

            DisplayingResults.DisplayResult(result);
        }
    }
}

class Calculator
{
    public static int Add(int a, int b) => a + b;
    public static int Subtract(int a, int b) => a - b;
    public static int Multiply(int a, int b) => a * b;
    public static int Divide(int a, int b)
    {
        if (b == 0)
            throw new ArgumentException("Division by zero is not allowed.");
        return a / b;
    }
}

class ActualCalcs
{
    public static int GetUserInput()
    {
        int input;
        {
            Console.WriteLine("Enter a number:");
            return int.TryParse(Console.ReadLine()!, out input) ? input : 0;
        }
    }

    public static void ModifyNumbers(ref int a, ref int b)
    {
        Console.WriteLine("Do you want to double the first number? (y/n)");
        if (Console.ReadLine()?.ToLower() == "y")
            a *= 2;  

        Console.WriteLine("Do you want to double the second number? (y/n)");
        if (Console.ReadLine()?.ToLower() == "y")
            b *= 2;  
    }
}

class DisplayingResults
{
    public static int PerformOperation(int num1, int num2)
    {
        Console.WriteLine("Choose the operation:");
        Console.WriteLine("1. Add");
        Console.WriteLine("2. Subtract");
        Console.WriteLine("3. Multiply");
        Console.WriteLine("4. Divide");

        int choice = ActualCalcs.GetUserInput();

        switch (choice)
        {
            case 1: return Calculator.Add(num1, num2);
            case 2: return Calculator.Subtract(num1, num2);
            case 3: return Calculator.Multiply(num1, num2);
            case 4: return Calculator.Divide(num1, num2);
            default:
                Console.WriteLine("Invalid choice.");
                return 0;
        }
    }

    public static void DisplayResult(int result)
    {
        Console.WriteLine("Result: " + result);
    }
}
