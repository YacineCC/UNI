// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;


import java.util.Set;

public interface Formula {
    boolean value(Interpretation interp);
    Set<Var> vars();
    Formula toNormalForm();
    Formula toCNF();
    Formula toDNF();
    String toHtml();
    String toString();

}
