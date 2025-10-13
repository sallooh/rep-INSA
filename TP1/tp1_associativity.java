import java.util.Random;

public class tp1_associativity {
    public static void main(String[] args) {
        int n = 10000; // nombre de répétitions
        int success = 0;
        Random rand = new Random();

        for (int i = 0; i < n; i++) {
            double x = rand.nextDouble() * 2e16 - 1e16; // entre -1e16 et 1e16
            double y = rand.nextDouble() * 2e16 - 1e16;
            double z = rand.nextDouble() * 2e16 - 1e16;

            double a = (x + y) + z;
            double b = x + (y + z);

            if (a == b) {
                success++;
            }
        }

        double pourcentage = (success * 100.0) / n;

        System.out.println("Sur " + n + " tests :");
        System.out.println(" - Succès exacts : " + success);
        System.out.printf(" - Pourcentage de réussite : %.6f%%\n", pourcentage);
    }
}
