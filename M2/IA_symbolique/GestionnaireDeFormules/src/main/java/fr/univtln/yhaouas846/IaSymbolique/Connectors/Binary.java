// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique.Connectors;

import fr.univtln.yhaouas846.IaSymbolique.Formula;
import fr.univtln.yhaouas846.IaSymbolique.Interpretation;
import fr.univtln.yhaouas846.IaSymbolique.Var;

import java.util.HashSet;
import java.util.Set;

public abstract class Binary implements Formula {
    protected final Formula left, right;
    public Binary(Formula l, Formula r){ left = l; right = r; }

    public Formula left(){ return left; }
    public Formula right(){ return right; }

    public Set<Var> vars(){
        Set<Var> s = new HashSet<>(left.vars());
        s.addAll(right.vars());
        return s;
    }
}
