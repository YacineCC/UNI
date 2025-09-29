// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
package fr.univtln.yhaouas846.IaSymbolique;

import fr.univtln.yhaouas846.IaSymbolique.Connectors.*;
import fr.univtln.yhaouas846.IaSymbolique.Constants.FalseConst;
import fr.univtln.yhaouas846.IaSymbolique.Constants.TrueConst;

import java.util.ArrayList;
import java.util.List;


public class F {
    public static Formula TRUE = new TrueConst();
    public static Formula FALSE = new FalseConst();

    public static Formula var(String name){ return new Var(name); }
    public static Formula not(Formula f){ return new Not(f); }
    public static Formula and(Formula a, Formula b){ return new And(a,b); }
    public static Formula or(Formula a, Formula b){ return new Or(a,b); }
    public static Formula imp(Formula a, Formula b){ return new Imp(a,b); }
    public static Formula equiv(Formula a, Formula b){ return new Equiv(a,b); }

}

