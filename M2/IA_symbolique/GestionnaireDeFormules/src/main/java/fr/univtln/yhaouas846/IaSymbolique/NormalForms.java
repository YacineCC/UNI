package fr.univtln.yhaouas846.IaSymbolique;


import fr.univtln.yhaouas846.IaSymbolique.Connectors.*;
import fr.univtln.yhaouas846.IaSymbolique.Constants.FalseConst;
import fr.univtln.yhaouas846.IaSymbolique.Constants.TrueConst;
// Utilisation d'une IA Génrative (ChatGPT) pour ce TP
//
import java.util.*;
public class NormalForms {

    // ----------------------------
    // CNF
    // ----------------------------
    public static Formula toCNF(Formula f) {
        f = f.toNormalForm();
        f = distributeOrOverAnd(f);
        f = flattenAndOr(f);
        f = simplifyConstants(f);
        f = removeDuplicateLiterals(f);
        return f;
    }

    // ----------------------------
    // DNF
    // ----------------------------
    public static Formula toDNF(Formula f) {
        f = f.toNormalForm();
        f = distributeAndOverOr(f);
        f = flattenAndOr(f);
        f = simplifyConstants(f);
        f = removeDuplicateLiterals(f);
        return f;
    }

    // ----------------------------
    // Distribution CNF : Or sur And
    // ----------------------------
    private static Formula distributeOrOverAnd(Formula f) {
        if (f instanceof Or o) {
            Formula l = o.left();
            Formula r = o.right();

            if (l instanceof And a) {
                return new And(
                        distributeOrOverAnd(new Or(a.left(), r)),
                        distributeOrOverAnd(new Or(a.right(), r))
                );
            }
            if (r instanceof And a) {
                return new And(
                        distributeOrOverAnd(new Or(l, a.left())),
                        distributeOrOverAnd(new Or(l, a.right()))
                );
            }

            return new Or(distributeOrOverAnd(l), distributeOrOverAnd(r));
        }

        if (f instanceof And a) {
            return new And(distributeOrOverAnd(a.left()), distributeOrOverAnd(a.right()));
        }

        return f;
    }

    // ----------------------------
    // Distribution DNF : And sur Or
    // ----------------------------
    private static Formula distributeAndOverOr(Formula f) {
        if (f instanceof And a) {
            Formula l = a.left();
            Formula r = a.right();

            if (l instanceof Or o) {
                return new Or(
                        distributeAndOverOr(new And(o.left(), r)),
                        distributeAndOverOr(new And(o.right(), r))
                );
            }
            if (r instanceof Or o) {
                return new Or(
                        distributeAndOverOr(new And(l, o.left())),
                        distributeAndOverOr(new And(l, o.right()))
                );
            }

            return new And(distributeAndOverOr(l), distributeAndOverOr(r));
        }

        if (f instanceof Or o) {
            return new Or(distributeAndOverOr(o.left()), distributeAndOverOr(o.right()));
        }

        return f;
    }

    // ----------------------------
    // Aplatir les And et Or imbriqués
    // ----------------------------
    private static Formula flattenAndOr(Formula f) {
        if (f instanceof And a) {
            List<Formula> terms = new ArrayList<>();
            collectAndTerms(a, terms);
            Formula res = terms.get(0);
            for (int i = 1; i < terms.size(); i++) res = new And(res, terms.get(i));
            return res;
        }
        if (f instanceof Or o) {
            List<Formula> terms = new ArrayList<>();
            collectOrTerms(o, terms);
            Formula res = terms.get(0);
            for (int i = 1; i < terms.size(); i++) res = new Or(res, terms.get(i));
            return res;
        }
        return f;
    }

    private static void collectAndTerms(Formula f, List<Formula> terms) {
        if (f instanceof And a) {
            collectAndTerms(a.left(), terms);
            collectAndTerms(a.right(), terms);
        } else {
            terms.add(f);
        }
    }

    private static void collectOrTerms(Formula f, List<Formula> terms) {
        if (f instanceof Or o) {
            collectOrTerms(o.left(), terms);
            collectOrTerms(o.right(), terms);
        } else {
            terms.add(f);
        }
    }

    // ----------------------------
    // Simplification des constantes ⊤ et ⊥
    // ----------------------------
    private static Formula simplifyConstants(Formula f) {
        if (f instanceof And a) {
            Formula l = simplifyConstants(a.left());
            Formula r = simplifyConstants(a.right());
            if (l instanceof TrueConst) return r;
            if (r instanceof TrueConst) return l;
            if (l instanceof FalseConst || r instanceof FalseConst) return new FalseConst();
            return new And(l, r);
        }
        if (f instanceof Or o) {
            Formula l = simplifyConstants(o.left());
            Formula r = simplifyConstants(o.right());
            if (l instanceof FalseConst) return r;
            if (r instanceof FalseConst) return l;
            if (l instanceof TrueConst || r instanceof TrueConst) return new TrueConst();
            return new Or(l, r);
        }
        if (f instanceof Not n) {
            Formula inner = simplifyConstants(n.getF());
            if (inner instanceof TrueConst) return new FalseConst();
            if (inner instanceof FalseConst) return new TrueConst();
            return new Not(inner);
        }
        return f;
    }

    // ----------------------------
    // Éliminer les littéraux dupliqués dans les clauses
    // ----------------------------
    private static Formula removeDuplicateLiterals(Formula f) {
        if (f instanceof And a) {
            return new And(removeDuplicateLiterals(a.left()), removeDuplicateLiterals(a.right()));
        }
        if (f instanceof Or o) {
            List<Formula> termsList = new ArrayList<>();
            collectOrTerms(o, termsList);

            // éliminer doublons
            Set<Formula> set = new LinkedHashSet<>(termsList);
            List<Formula> list = new ArrayList<>(set);

            if (list.isEmpty()) {
                return new FalseConst(); // Or vide = ⊥
            }

            Formula res = list.get(0);
            for (int i = 1; i < list.size(); i++) {
                res = new Or(res, list.get(i));
            }
            return res;
        }
        return f;
    }

}

