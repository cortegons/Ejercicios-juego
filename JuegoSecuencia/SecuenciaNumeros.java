import java.util.Random;
import java.util.Scanner;

public class SecuenciaNumeros
{
    static int[][] intentos = new int[13][4];
    static int[][] pistas = new int[12][2];
    public static void main(String[]args){
        Scanner sc = new Scanner(System.in);
        System.out.println("Adivina el número de 4 cifras");
        MatrizIntentos(NumRandom());
        for(int i = 1; i < intentos.length; i++){
            String entrada = sc.next();
            Conversion(entrada, i);
            MatrizPistas(intentos, i);
        }
    }

    public static int[] NumRandom(){
        int[] numeros = new int[4];
        Random rand = new Random();
        for(int i = 0; i < 4; i++){
            numeros[i] = rand.nextInt(9);
            if(i == 1){
                if(numeros[i] == numeros[0]) i--;
            }
            else if(i == 2){
                if(numeros[i] == numeros[0]||numeros[i]==numeros[1]) i--;
            }
            else if(i == 3){
                if(numeros[i] == numeros[0]||numeros[i]==numeros[1]||numeros[i]== numeros[2]) i--;
            }
        }
        return numeros;
    }

    public static void MatrizIntentos(int[] a){
        for(int i = 0; i < 4; i++){
            intentos[0][i] = a[i];
        }
    }

    public static void MatrizPistas(int[][] e, int fila){
        int aciertos = 0;
        int aprox = 0;
        for(int i = 0; i < 4; i++){
            if(e[fila][i] == e[0][i]){
                pistas[fila-1][0]++;
                aciertos++;
            }
            else if(e[fila][i] == e[0][0]||e[fila][i] == e[0][1]||e[fila][i] == e[0][2]||e[fila][i] == e[0][3]){
                pistas[fila-1][1]++;
                aprox++;
            }
            else continue;
        }
        if(aciertos == 4)MensajeFinal(true, fila);
        if(fila == 12)MensajeFinal(false, fila);
        else{
            System.out.println("Hubo " + pistas[fila-1][0] + " aciertos y " + pistas[fila-1][1] + " aproximaciones.");
            System.out.println("Te quedan " + (12 - fila) + " intentos.");
        }
    }

    public static void Conversion(String str,int pos){
        int[] convert = new int[str.length()];
        for(int i = 0; i < str.length();i++){
            convert[i] = Character.getNumericValue(str.charAt(i));
            intentos[pos][i] = convert[i];
        }
    }

    public static void MensajeFinal(boolean resultado, int intento){
        if(resultado) System.out.println("Felicitaciones, has ganado, número de intentos: " + intento);
        else {System.out.println("Se acabaron los intentos, has perdido.");
            System.out.println("El número era " + intentos[0][0] + "" + intentos[0][1] + "" + intentos[0][2] + "" + intentos[0][3]);
	}
            System.exit(0);
        
    }
}
