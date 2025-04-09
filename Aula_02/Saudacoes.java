package Aula_02;

import java.util.Scanner;

public class Saudacoes {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Escreva seu nome: ");
        String nome = scanner.nextLine();
        
        System.out.print("Escreva sua idade: ");
        int idade = scanner.nextInt();
        
        System.out.println("Você se chama " + nome + " e tem " + idade + " anos!");
        
        scanner.close();
    }
}