import java.time.LocalDate;
import java.util.Scanner;

public class First {
    public static void main(String[] args) {
        String prenom = "Alexa";
        int age = 52;
        double note = 15.5;
        boolean estMajeur = true;
        char sexe = 'F';
        LocalDate maintenant = LocalDate.now();
        LocalDate dateNaissance = LocalDate.of(1973, 5, 22);

        System.out.println("Bonjour " + prenom + ", tu as "+ age + "ans, ta note au controle est de "+ note +", tu es né le : "+ dateNaissance );


        System.out.println("Veuillez corriger les informations en cas d'erreur.");
        Scanner sc = new Scanner(System.in);
        System.out.print("Entrez votre nom : ");
        prenom = sc.nextLine();
        System.out.print("Entrez votre age : ");
        age = sc.nextInt();
        System.out.print("Entrez votre note : ");
        note = sc.nextDouble();
        System.out.print("Entrez votre sexe : ");
        sexe = sc.next().charAt(0);
        // vider le buffet avant de lire une ligne
        sc.nextLine();
        System.out.print("Quelle est ta date de naissance (format jj/mm/aaaa) : ");
        String date = sc.nextLine();

    }
}
