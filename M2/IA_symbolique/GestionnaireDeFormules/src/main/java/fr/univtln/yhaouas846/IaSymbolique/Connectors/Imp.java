// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique.Connectors;

import fr.univtln.yhaouas846.IaSymbolique.F;
import fr.univtln.yhaouas846.IaSymbolique.Formula;
import fr.univtln.yhaouas846.IaSymbolique.Interpretation;
import fr.univtln.yhaouas846.IaSymbolique.NormalForms;


public class Imp extends Binary {
    public Imp(Formula l, Formula r){ super(l,r); }

    public boolean value(Interpretation interp){ return !left.value(interp) || right.value(interp); }

    public Formula toNormalForm(){ return F.or(new Not(left).toNormalForm(), right.toNormalForm()); }

    @Override
    public Formula toCNF() {
        return NormalForms.toCNF(this);
    }

    @Override
    public Formula toDNF() {
        return NormalForms.toDNF(this);
    }
    public String toHtml(){ return "(" + left.toHtml() + " &rightarrow; " + right.toHtml() + ")"; }
    public String toString(){ return "(" + left + " -> " + right + ")"; }
}