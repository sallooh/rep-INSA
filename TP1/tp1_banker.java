public class tp1_banker {
    public static void main(String[] args) {
        int n = 50; // nombre d'années
        double montant = Math.E; // valeur exacte de e

        // Boucle sur chaque année
        for (int k = 1; k <= n; k++) {
            montant = (montant - 1) * k;
        }

        // Frais final pour récupérer l'argent
        montant -= 1;

        System.out.println("Après " + n + " ans, vous aurez environ : " + montant);
    }
}
