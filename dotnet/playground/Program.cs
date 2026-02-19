var gamekinda = new gameKinda();
gamekinda.PrintPlayerName(new PLayerName());

//print touple shit
var autism = new Autism();
autism.PrintTuple();

public struct PLayerName
{
    public string Name;
    public string Surname;
}

class gameKinda
{
    public void PrintPlayerName(PLayerName player)
    {
        Console.WriteLine("Enter your name: ");
        player.Name = Console.ReadLine();
        Console.WriteLine("Enter your surname: ");
        player.Surname = Console.ReadLine();
        Console.WriteLine($"Your name is {player.Name} {player.Surname}");
    }
}

//typle shit

class Autism{
(int, string, bool) tuple  = (1, "Hello", true);

    public void PrintTuple(){
        Console.WriteLine(tuple.Item1); // Output: 1
        Console.WriteLine(tuple.Item2); // Output: Hello
        Console.WriteLine(tuple.Item3); // Output: True
    }
}


