// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;

import java.util.Collections;
import java.util.Objects;
import java.util.Set;

public class Var implements Formula {
    private final String name;
    public Var(String name){ this.name = name; }

    public String name(){ return name; }

    @Override
    public boolean equals(Object obj){
        if (this.name == null || obj == null || obj.getClass() != this.getClass()) {
            return false;
        }
        final Var var = (Var) obj;
        return Objects.equals(this.name, var.name);
    }

    public boolean value(Interpretation interp){ return interp.get(this); }
    public Set<Var> vars(){ return Collections.singleton(this); }
    public Formula toNormalForm(){ return this; }
    public Formula toCNF(){ return this; }
    public Formula toDNF(){ return this; }
    public String toHtml(){ return name; }
    public String toString(){ return name; }
}
