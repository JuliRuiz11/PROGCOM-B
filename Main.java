class MAain Positivo {
    static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese un Número: ");
        double Número = scanner.nextDouble();
        
        System.out.println("\n--- Método 1: if/else ---");
        if (Número >= 0) {
            System.out.println(Número + " Es un número positivo");
        } else {
            System.out.println(Número + " NO es un número positivo");
        }
        
        System.out.println("\n--- Método 2: if/else if ---");
        if (Número > 0) {
            System.out.println(Número + " Es positivo");
        } else if (Número == 0) {
            System.out.println(Número + " Es cero (no positivo ni negativo)");
        } else {
            System.out.println(Número + " Es negativo");
        }

    2.
import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        int Número1;
        Scanner input1 = new Scanner(System.in);
        System.out.print("Ingresa el 1 número: ");
        Numero1 = input1.nextInt();

        int Número2;
        Scanner input2 = new Scanner(System.in);
        System.out.print("Ingresa el 2 número: ");
        Número2 = input2.nextInt();

        if(Número1 > Número2){
            System.out.println("El número 1 es mayor!");
        }
        else if(Número1 == Número2) {
            System.out.println("Los números son iguales");
        }
        else{
            System.out.println("El número 2 es menor");
        }
    }
}

        3. 
import java.util.Scanner;
public class ejercicio 3 {
    public static void main(String[] args) {
        int Edad;
        Scanner input = new Scanner(System.in);
        System.out.print("Ingresa una edad: ");
        Edad = input.nextInt();

        if(Edad >= 18){
            System.out.println("Uestd es mayor de edad");
        }
        else {
            System.out.println("Usted es menor de edad");
        }
    }
}
        4. 
public class Ejercicio 4 {
    public static void main(String[] args) {
        int Calificación;
        Scanner input = new Scanner(System.in);
        System.out.print("Ingresa una calificación: ");
        Calificación = input.nextInt();

        if(Calificación > 100){
            System.out.println("Calificación invalida!");
        }
        else if(Calificación >= 60) {
            System.out.println("Usted aprobo");
        }
        else {
            System.out.println("Usted NO aprobo");
        }
