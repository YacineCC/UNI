package fr.univtln.haouas.TPs;

public class Aigle extends Oiseau implements ICarnivore{
    private String couleur;

    public Aigle(String nom, String id, int nbPlumes,String couleur, int age) {
        super(nom, id, nbPlumes, age);
        this.couleur = couleur;
    }

    @Override
    public void crier() {
        super.crier("Aigle");
    }
    @Override
    public String toString(){
        return super.toString() +" Aigle " + "couleur: " + couleur;
    }

    public String getInfo(){
        return super.getInfo() + " Je suis un Aigle de couleur " + couleur+ " et mon nom est " + getNom();
    }
    @Override
    public String moyenExpression(){
        return super.moyenExpression() + " Je Glapit ? Glatit ??";
    }

    @Override
    public void manger(Animal x) {
        System.out.println("Je déchire " + x.getNom());
    }
}
