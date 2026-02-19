using System;

namespace GenericsExample
{
    class Program
    {
        static void Main(string[] args)
        {
            Box<int> intBox = new Box<int>();
            Container<string> stringContainer = new Container<string>();
            Pair<int, string> pair = new Pair<int, string>();

            int num = GetUserInputNoutput.GetUserInput();
            GetUserInputNoutput.DisplayResult(num);
        }
    }

    class Box<T>
    {
        public T Size;
    }

    class Container<T>
    {
        public T Content;
    }

    class Pair<T1, T2>
    {
        public T1 First;
        public T2 Second;
    }

    class GetUserInputNoutput
    {
        public static int GetUserInput()
        {
            int input;
            Console.WriteLine("Enter a number:");
            return int.TryParse(Console.ReadLine()!, out input) ? input : 0;
        }

        public static void DisplayResult(int result)
        {
            Console.WriteLine($"The result is: {result}");
        }
    }
}
