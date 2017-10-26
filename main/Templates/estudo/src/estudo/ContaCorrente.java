/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package estudo;

/**
 *
 * @author yan.santos
 */
public class ContaCorrente {

  int numero;
  private double saldo;
  String nomeTitular;

  int getNumero() {

    return this.numero;
  }

  void setNumero(int pNumero) {

    this.numero = pNumero;

  }

  String getNome() {

    return this.nomeTitular;
  }

  void setNomeTitular(String pNomeTitular) {

    this.nomeTitular = pNomeTitular;

  }

  double getSaldo() {

    return this.saldo;
  }

  void depositar(double valor) {

    this.saldo += valor;

  }

}
