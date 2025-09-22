package fr.univtln.yhaouas846.IaSymbolique;

public class Var {

    private String name;
    private Interpretation interpretation;

    public Var(String name, Interpretation interpretation) {
        this.name = name;
        this.interpretation = interpretation;
    }
    public Var(String name) {
        this.name = name;
    }


    @Override
    public String toString() {
        return this.name + " : " + this.interpretation.toString();
    }
}
