import java.io.*;

public class eutazas {
    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new FileReader("utasadat.txt"));

        int[] megallo = new int[2000];
        String[] datum = new String[2000];
        int[] azonosito = new int[2000];
        String[] tipus = new String[2000];
        int[] ervenyesseg = new int[2000];

        String sor;
        String[] darabSor = new String[2000];
        int count = 0;

        while((sor = reader.readLine()) != null) {
            count++;
            darabSor = sor.split(" ");
            megallo[count - 1] = Integer.parseInt(darabSor[0]);
            datum[count - 1] = darabSor[1];
            azonosito[count - 1] = Integer.parseInt(darabSor[2]);
            tipus[count - 1] = darabSor[3];
            ervenyesseg[count - 1] = Integer.parseInt(darabSor[4]);
        }
        reader.close();

        System.out.println("2.feladat");

        int i = count;

        for(int j = 1; j <= count; j++) {
            if(azonosito[j - 1] == 0) {
                i--;
            }
        }

        System.out.println("A buszra " + i + " utas akart felszállni.");

        System.out.println("3.feladat");

        int b = 0;

        for(int a = 1; a <= count; a++) {
            if(tipus[a - 1].equals("JGY")) {
                if (ervenyesseg[a - 1] == 0) {
                    b++;
                }
            } else if(!(tipus[a - 1].equals("JGY"))) {
                int utazasDatum = Integer.parseInt(datum[a - 1].substring(0, 8));
                if ((ervenyesseg[a - 1] - utazasDatum) < 0) {
                    b++;
                }
            }
        }
        System.out.println("A buszra " + b + " utas nem szállhatott fel.");

        System.out.println("4.feladat");

       int[] utasCount = new int[30];

       for(int g = 0; g <= 29; g++) {
           utasCount[g] = 0;
       }

       for(int h = 1; h <= count; h++){
           utasCount[megallo[h - 1]]++;
       }

       int max = 0;

       for(int z = 1; z <= 29; z++){
           if(utasCount[z] > utasCount[max]) {
               max = z;
           }
       }

        System.out.println("A legtöbb utas (" + utasCount[max] + " fő) a " + max + ". megállóban próbált felszálllni.");

        System.out.println("5.feladat");

       int kedvezmenyes = 0;
       int ingyenes = 0;

       for(int x = 1; x <= count; x++) {
           int utazasdatuma = Integer.parseInt(datum[x - 1].substring(0, 8));
           if(!(tipus[x - 1].equals("JGY"))) {
               if((ervenyesseg[x - 1] - utazasdatuma) >= 0) {
                   if(tipus[x - 1].equals("TAB") || tipus[x - 1].equals("NYB")) {
                       kedvezmenyes++;
                   }
                   if(tipus[x - 1].equals("NYP") || tipus[x - 1].equals("RVS") || tipus[x - 1].equals("GYK")) {
                       ingyenes++;
                   }
               }
           }
       }

        System.out.println("Ingyenesen utazók száma: " + ingyenes + " fő");
        System.out.println("A kedvezményesen utazók száma: " + kedvezmenyes + " fő");

        PrintWriter writer = new PrintWriter(new FileWriter("figyelmeztetes.txt"));

        for(int y = 1; y <= count; y++) {
            int utDatum = Integer.parseInt(datum[y - 1].substring(0, 8));
           if(!tipus[y - 1].equals("JGY")) {
               int n1 = utDatum % 100;
               int h1 = utDatum / 100;
               int e1 = h1 / 100;
               int n2 = ervenyesseg[y - 1] % 100;
               int h2 = ervenyesseg[y - 1] / 100;
               int e2 = h2 / 100;
               h2 = h2 % 100;

               if(napokszama(e1, h1, n1, e2, h2, n2) <= 3) {
                   writer.println(azonosito[y - 1] + " " + e2 + "-" + h2 + "-" + n2);
               }
           }
        }
        writer.close();
    }

    public static int napokszama (int e1, int h1, int n1, int e2, int h2, int n2) {
        h1 = (h1 + 9) % 12;
        e1 = e1 - h1 / 10;
       int d1 = 365 * e1 + e1 / 4 - e1 / 100 + e1 / 400 + (h1 * 306 + 5) / 10 + n1 - 1;
       h2 = (h2 + 9) % 12;
       e2 = e2 - h2 / 10;
       int d2 = 365 * e2 + e2 / 4 - e2 / 100 + e2 / 400 + (h2 * 306 + 5) / 10 + n2 - 1;
       return d2 - d1;
    }
}
