/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package estudo;

import javax.swing.JOptionPane;

/**
 *
 * @author yan.santos
 */
public class Estudo {

  /**
   * @param args the command line arguments
   */
  public static void main(String[] args) {
    // TODO code application logic here

    ContaCorrente minhaConta = new ContaCorrente();
    
    String Nome = JOptionPane.showInputDialog("Digite seu nome");
    minhaConta.setNomeTitular(Nome);
    
    String cntNum = JOptionPane.showInputDialog("Digite o número da conta");
    minhaConta.setNumero(Integer.parseInt(cntNum));
    
    String deposito = JOptionPane.showInputDialog("Digite o valor do depósito");
    minhaConta.depositar(Integer.parseInt(deposito));
    
    
    JOptionPane.showMessageDialog(null, "Seu nome é: " + minhaConta.getNome() + "\nSeu saldo é de: " +
            minhaConta.getSaldo(), "Informações da Conta", JOptionPane.OK_OPTION);
    
    JOptionPane.showMessageDialog(null, "Deseja realizar um novo pedido?", "Informações", JOptionPane.OK_OPTION);
  }
}