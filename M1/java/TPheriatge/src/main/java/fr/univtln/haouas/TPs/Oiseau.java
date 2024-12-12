package fr.univtln.haouas.TPs;

public abstract class Oiseau extends Animal{
    private int nbPlumes;
    public Oiseau(String nom, String id,int nbPlumes, int age) {
        super(nom, id, age);
        this.nbPlumes = nbPlumes;
    }

    public void crier(String espece) {
        System.out.println("Je suis un oiseau de l'espèce " + espece + " et je crie !");
    }

    @Override
    public String toString(){
        return super.toString() + " Tétrapode "+" nbPlumes: " + nbPlumes;
    }

    public String getInfo(){
        if (nbPlumes == 0)
            return super.getInfo() + " Je suis un Oiseau ";
        else
            return super.getInfo() + " Je suis un Oiseau avec " + nbPlumes + " plumes"+ " et mon nom est " + getNom();
    }

    @Override
    public String moyenExpression(){
        return " Je chante";
    }
}
