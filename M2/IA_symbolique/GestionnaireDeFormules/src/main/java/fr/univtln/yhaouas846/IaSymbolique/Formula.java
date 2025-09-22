package fr.univtln.yhaouas846.IaSymbolique;

public class Formula {

    public enum Connector {NOT, AND, OR, IMP, EQUIV}
    private Connector connector;
    private Formula subFormulaLeft;
    private Formula subFormulaRight;
    private Interpretation interpretation;
    private VariableSet varSet;


    public Formula(Var var){
        this.subFormulaLeft = null;
        VariableSet
    }

    public Formula(Formula subFormula, Connector connector){
        this.subFormulaLeft = subFormula;
        this.connector = connector;
    }

    public Formula(Formula subFormulaLeft, Connector connector, Formula subFormulaRight){
        this.subFormulaLeft = subFormulaLeft;
        this.connector = connector;
        this.subFormulaRight = subFormulaRight;
    }

    @Override
    public String toString(){
        return this.subFormulaLeft.toString() + this.connector.toString() + this.subFormulaRight.toString();
    }



}
