package fr.univtln.yhaouas846.IaSymbolique;

import java.util.HashSet;
import java.util.Set;

public class VariableSet {


    private Formula formula;
    private Set<Var> varSet = new HashSet<>();

    public VariableSet(Formula formula){
        this.formula = formula;
    }

    public void addVar(Var var){
        this.varSet.add(var);
    }

    @Override
    public String toString(){
        return varSet.toString();
    }
}
