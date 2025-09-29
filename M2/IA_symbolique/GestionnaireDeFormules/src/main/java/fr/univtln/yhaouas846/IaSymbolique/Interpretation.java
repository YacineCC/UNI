// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;



public class Interpretation {
    private final Map<Formula, Boolean> map;

    public Interpretation() { map = new HashMap<>(); }
    public Interpretation(Map<Formula, Boolean> base){ map = new HashMap<>(base); }

    public void put(Formula f, Boolean val){ map.put(f, val); }
    public boolean get(Formula var){
        Boolean b = map.get(var);
        if (b == null) throw new IllegalArgumentException("Variable not present: " + var);
        return b;
    }

    public Set<Formula> vars(){ return map.keySet(); }
    @Override
    public String toString(){ return map.toString(); }
}
