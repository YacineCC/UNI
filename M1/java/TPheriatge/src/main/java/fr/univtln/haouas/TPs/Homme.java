package fr.univtln.haouas.TPs;

public class Homme extends  Mammifere implements IOmnivore{
    private int iQ;

    public Homme(String nom, String id,int gestation,int iQ, int age) {
        super(nom, id, gestation, age);
        this.iQ = iQ;
    }

    public Homme()
    {
        super();
        this.iQ = 0;
    }

    @Override
    public void crier() {
        super.crier("Homme");
    }
    @Override
    public String toString(){
        return super.toString() +" Homme "+ " iQ: " + iQ;
    }

    @Override
    public String getInfo(){
        if (iQ == 0)
            return super.getInfo() + " Je suis un Homme ";
        else
            return super.getInfo() + " Je suis un Homme de iQ " + iQ+ " et mon nom est " + getNom();

    }
    @Override
    public String moyenExpression(){
        return super.moyenExpression() + " Je parlent";
    }

    /**
     * @param x manger un animal
     */
    @Override
    public void manger(Animal x) {
        System.out.println("Je mange " + x.getNom() + " en tant que carnivore");

    }

    /**
     * @param x manger un plante
     */
    @Override
    public void manger(Plante x) {
        System.out.println("Je mange " + x.getNom() + " en tant que herbivore");

    }
}
