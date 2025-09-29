// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique.Connectors;

import fr.univtln.yhaouas846.IaSymbolique.*;

import java.util.Set;


public class Not implements Formula {
    private final Formula f;
    public Not(Formula f){ this.f = f; }

    public Formula getF(){ return f; }
    public boolean value(Interpretation interp){ return !f.value(interp); }
    public Set<Var> vars(){ return f.vars(); }

    public Formula toNormalForm(){
        if (f instanceof Not) return ((Not)f).getF().toNormalForm();
        if (f instanceof And a) return F.or(new Not(a.left()).toNormalForm(), new Not(a.right()).toNormalForm());
        if (f instanceof Or o) return F.and(new Not(o.left()).toNormalForm(), new Not(o.right()).toNormalForm());
        if (f instanceof Imp i) return F.and(i.left().toNormalForm(), new Not(i.right()).toNormalForm());
        if (f instanceof Equiv e) {
            Formula t1 = F.and(e.left(), new Not(e.right()));
            Formula t2 = F.and(new Not(e.left()), e.right());
            return F.or(t1.toNormalForm(), t2.toNormalForm());
        }
        return this;
    }

    @Override
    public Formula toCNF() {
        return NormalForms.toCNF(this);
    }

    @Override
    public Formula toDNF() {
        return NormalForms.toDNF(this);
    }

    public String toHtml(){ return "&not;" + f.toHtml(); }
    public String toString(){ return "(!" + f + ")"; }
}