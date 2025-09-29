// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique.Constants;

import fr.univtln.yhaouas846.IaSymbolique.Formula;
import fr.univtln.yhaouas846.IaSymbolique.Interpretation;
import fr.univtln.yhaouas846.IaSymbolique.Var;

import java.util.Collections;
import java.util.Set;

public class TrueConst implements Formula {
    public boolean value(Interpretation interp){ return true; }
    public Set<Var> vars(){ return Collections.emptySet(); }
    public Formula toNormalForm(){ return this; }
    public Formula toCNF(){ return this; }
    public Formula toDNF(){ return this; }
    public String toHtml(){ return "⊤"; }
    public String toString(){ return "T"; }
}
