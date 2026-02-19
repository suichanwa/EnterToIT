using System;
using System.IO;

//create file if not exists
File.Create("example.txt").Close();

//add text to file
File.WriteAllText("example.txt", "Hello, World!");

//Read n output
File.ReadAllText("example.txt");
Console.WriteLine(File.ReadAllText("example.txt"));

//delete file
File.Delete("example.txt");