#include <iostream>

using namespace std;

int main() {
    string nome;
    int idade;
    cout << "Escreva seu nome " ;
    //cin >> nome;
    getline(cin, nome);

    cout << "Escreva sua idade ";
    cin >> idade;
    cout << "Você se chama " << nome << " e tem " << idade << " anos! " << endl;
    return 0;
}