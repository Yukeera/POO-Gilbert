using System;

class Program
{
    static void Main()
    {
        string nome;
        int idade;

        Console.Write("Escreva seu nome: ");
        nome = Console.ReadLine();

        Console.Write("Escreva sua idade: ");
        idade = Convert.ToInt32(Console.ReadLine());

        Console.WriteLine("Você se chama " + nome + " e tem " + idade + " anos!");
    }
}