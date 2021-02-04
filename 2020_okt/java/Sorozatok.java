import java.io.*;
import java.util.Scanner;

public class Sorozatok {

    public static void main(String[] args) throws IOException {

        BufferedReader reader = new BufferedReader(new FileReader("lista.txt"));

        String[] releaseDate = new String[400];
        String[] title = new String[400];
        String[] seasonEpisode = new String[400];
        int[] length = new int[400];
        int[] isWatched = new int[400];

       int count = 0;
       String line;

       while((line = reader.readLine()) != null) {
           count++;
           releaseDate[count - 1] = line;
           title[count - 1] = reader.readLine();
           seasonEpisode[count - 1] = reader.readLine();
           length[count - 1] = Integer.parseInt(reader.readLine());
           isWatched[count - 1] = Integer.parseInt(reader.readLine());
       }
        reader.close();

        System.out.println("2.feladat");

        int knownReleaseDate = count;

        for(int i = 1; i <= count; i++) {
            if(releaseDate[i - 1].equals("NI")) {
                knownReleaseDate--;
            }
        }

        System.out.println("A listában " + knownReleaseDate + " db vetítési dátummal rendelkező epizód van.");

        System.out.println("3.feladat");

        int watched = 0;

        for(int j = 1; j <= count; j++) {
            if(isWatched[j - 1] == 1) {
                watched++;
            }
        }

        double percentage = (double)watched / (double)count * 100;

        System.out.println("A listában lévő epizódok " + String.format("%.2f", percentage) + "%-át látta.");

        System.out.println("4. feladat");

        int watchedInTime = 0;

        for(int k = 1; k <= count; k++) {
            if(isWatched[k - 1] == 1) {
                watchedInTime += length[k - 1];
            }
        }

        int day = 0;
        int hour = 0;
        int minute = 0;

        minute = watchedInTime % 60;
        hour = watchedInTime / 60;
        day = hour / 24;
        hour = hour % 24;

        System.out.println("Sorozatnézéssel " + day + " napot " + hour + " órát és " + minute + " percet töltött.");

        System.out.println("5. feladat");

        System.out.println("Adjon meg egy dátumot! Dátum = ");

        Scanner scanner = new Scanner(System.in);

        String date = scanner.nextLine();

        for(int l = 1; l <= count; l++){
            if(releaseDate[l - 1].compareTo(date) <= 0) {
                if(isWatched[l - 1] == 0) {
                    System.out.println(seasonEpisode[l - 1] + "\t" + title[l - 1]);
                }
            }
        }

        System.out.println("7. feladat");

        System.out.println("Adja meg a hét egy napját (például cs)! Nap = ");

        String choosenDay = scanner.nextLine();

        int currentYear;
        int currentMonth;
        int currentDay;

        String[] filmList = new String[400];
        String currentFilm;

        int filmListCount = 0;

        for(int z = 1; z <= count; z++) {
            if(!(releaseDate[z - 1].equals("NI"))) {
               currentYear = Integer.parseInt(releaseDate[z - 1].substring(0, 4));
               currentMonth = Integer.parseInt(releaseDate[z - 1].substring(5, 7));
               currentDay = Integer.parseInt(releaseDate[z - 1].substring(8));

               if(hetnapja(currentYear, currentMonth, currentDay).equals(choosenDay)) {
                   currentFilm = title[z - 1];
                   int g = 1;
                   while(g <= filmListCount && !(filmList[g - 1].equals(currentFilm))) {
                       g++;
                   }
                   if(g > filmListCount) {
                       filmListCount++;
                       filmList[g - 1] = currentFilm;
                   }
               }
            }
        }
        if(filmListCount > 0) {
            System.out.println("A következő sorozatokat vetítik ezen a napon: \n");
            for(int f = 1; f <= filmListCount; f++) {
                System.out.println(filmList[f - 1]);
            }
        } else {
            System.out.println("Az adott napon nem került adásba sorozat.");
        }
        scanner.close();

        //    8. feladat

        String[] allFilmList = new String[400];
        int allFilmListCount = 0;

        int[] sumLength = new int[400];
        int[] sumEpisode = new int[400];

        for(int r = 1; r <= count; r++) {
            currentFilm = title[r - 1];

            int e = 1;
            while(e <= allFilmListCount && !(allFilmList[e - 1].equals(currentFilm))) {
                e++;
            }
            if(e <= allFilmListCount) {
                sumLength[e - 1] += length[r - 1];
                sumEpisode[e - 1]++;
            } else {
                allFilmListCount++;
                allFilmList[allFilmListCount - 1] = currentFilm;
                sumLength[allFilmListCount - 1] = length[r - 1];
                sumEpisode[allFilmListCount - 1] = 1;
            }
        }

        PrintWriter writer = new PrintWriter(new FileWriter("summa.txt"));

        for(int u = 1; u <= allFilmListCount; u++) {
            writer.println(allFilmList[u - 1] + " " + sumLength[u - 1] + " " + sumEpisode[u - 1]);
        }

        writer.close();
    }

    public static String hetnapja(int ev, int ho, int nap) {
        String[] napok = {"v", "h", "k", "sze", "cs", "p", "szo"};
        int[] honapok = {0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4};

        if(ho < 3){
            ev--;
        }
        return napok[(ev + ev / 4 - ev / 100 + ev / 400 + honapok[ho - 1] + nap) % 7];
    }
}
