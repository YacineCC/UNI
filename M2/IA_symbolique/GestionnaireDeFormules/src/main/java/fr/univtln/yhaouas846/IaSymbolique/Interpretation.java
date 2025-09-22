package fr.univtln.yhaouas846.IaSymbolique;

public class Interpretation {
    private Boolean value;

    public Interpretation(Boolean value){
        this.value = value;
    }

    @Override
    public String toString(){
        return this.value.toString();
    }
}
