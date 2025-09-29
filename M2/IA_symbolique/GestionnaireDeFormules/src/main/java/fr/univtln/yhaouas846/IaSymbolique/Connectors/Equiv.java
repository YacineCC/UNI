// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique.Connectors;

import fr.univtln.yhaouas846.IaSymbolique.F;
import fr.univtln.yhaouas846.IaSymbolique.Formula;
import fr.univtln.yhaouas846.IaSymbolique.Interpretation;
import fr.univtln.yhaouas846.IaSymbolique.NormalForms;


public class Equiv extends Binary {
    public Equiv(Formula l, Formula r){ super(l,r); }

    public boolean value(Interpretation interp){ return left.value(interp) == right.value(interp); }

    public Formula toNormalForm(){
        Formula t1 = F.and(left.toNormalForm(), right.toNormalForm());
        Formula t2 = F.and(new Not(left).toNormalForm(), new Not(right).toNormalForm());
        return F.or(t1, t2);
    }

    @Override
    public Formula toCNF() {
        return NormalForms.toCNF(this);
    }

    @Override
    public Formula toDNF() {
        return NormalForms.toDNF(this);
    }

    public String toHtml(){ return "(" + left.toHtml() + " &leftrightarrow; " + right.toHtml() + ")"; }
    public String toString(){ return "(" + left + " <-> " + right + ")"; }
}