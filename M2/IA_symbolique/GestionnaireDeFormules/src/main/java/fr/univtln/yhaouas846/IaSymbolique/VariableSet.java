// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;

import java.util.*;


public class VariableSet {
    private final Set<Var> vars;

    public VariableSet(Formula f) {
        this.vars = new HashSet<>(f.vars());
    }



    public List<Interpretation> getInterpretations() {
        List<Interpretation> res = new ArrayList<>();
        int x;
        int j;
        for(int i=0; i < (1 << this.vars.size()); i = i + 1){
            x = i;
            j =  0;
            List<Boolean> tmp = new ArrayList<>();
            while (x > 0 && j < this.vars.size())
            {
                if ((x & 1) == 1){
                    tmp.add(true);
                }
                else {
                    tmp.add(false);
                }
            }
            j = 0;

            Map<Formula, Boolean> tmpMap = new HashMap<>();
            for(Formula var:vars){
                tmpMap.put(var, tmp.get(j));
                j = j+1;
            }
            Interpretation tmpInterp = new Interpretation(tmpMap);
            res.add(tmpInterp);
        }

        return res;
    }

    @Override
    public String toString(){
        return vars.toString();
    }

    // Toutes les 2^n interprétations possibles pour Les n variables.
    // Par exemple pour n = 3 : [0, 0, 0], [0, 0, 1], [0, 1, 0] etc.
}

