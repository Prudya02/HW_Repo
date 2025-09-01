import java.util.*;
import java.io.*;
enum Genre {rock, opera, symphony, pop, country, techno, pank, folk};
class wrongRate extends Exception{}
class wrongLength extends Exception{}
class wrongYear extends Exception{}
class Comparer_length implements Comparator <Music>
{
    @Override
    public int compare(Music A, Music B)
    {
        if(A.get_length() == B.get_length())
            return 0;
        if(A.get_length() > B.get_length())
            return -1;
        return 1;
    }
}
class Comparer_name implements Comparator <Music>
{
    @Override
    public int compare(Music A, Music B)
    {
        return A.get_name().compareTo(B.get_name());
    }
}
class Music
{
    protected final int id;
    protected final int length;
    protected int rate;
    protected final Genre genre;
    protected final String name;
    protected int RemakeYear = 0;
    protected final String Author;  
    protected final String Performer;  
    protected static int count = 0;
    public Music (String name, Genre genre, String Author, String Performer, int length, int rate) throws wrongRate, wrongLength
    {
        if ((rate < 0)||(rate > 100)) 
            throw new wrongRate();
        if (length<0)
            throw new wrongLength();
        count++;
        this.id = count;
        this.length = length;
        this.rate = rate;
        this.name = name;
        this.genre = genre;
        this.Author = Author;
        this.Performer = Performer;
    }
    public Music (Music music) throws wrongRate, wrongLength
    {
        if ((music.rate < 0)||(music.rate > 100)) 
            throw new wrongRate();
        if (music.length<0)
            throw new wrongLength();
        count++;
        this.id = count;
        this.length = music.length;
        this.rate = music.rate;
        this.genre = music.genre;
        this.Author = music.Author;
        this.name = music.name;
        this.Performer = music.Performer;
    }
    public String get_name(){
        return this.name;
    }
    public String get_Author(){
        return this.Author;
    }
    public String get_Performer(){
        return this.Performer;
    }
    public Genre get_genre(){
        return this.genre;
    }
    public int get_length(){
        return this.length;
    }
    public int get_rate(){
        return this.rate;
    }
    public static int get_count(){
        return count;
    }
    public int get_id(){
        return this.id;
    }
    public void set_rate(int new_rate){
        this.rate = new_rate;
    }
    public String get_remake_composer()
    {
	    return "У данной песни нет ремейка";
    }
    public int get_remake_year()
    {
	    return RemakeYear;
    }
    @Override
        public String toString()
        {
            return this.id + " Имя автора - " + this.Author +
            ". Название произведения - " + this.name +
            ". Создана в жанре " + this.genre + " и первым исполнителем является " +
            this.Performer + ".\n Длительность композиции - " + this.length + " секунд(ы). Рейтинг - " +this.rate +"\n";
        }   
}
class RemakeComp extends Music 
{
    private final String RemakeComposer;
    private final int RemakeYear;
    public RemakeComp(String name, Genre genre, String Author, String Performer, int length, int rate, int RemakeYear, String RemakeComposer) throws wrongRate, wrongLength, wrongYear
    {
        super(name, genre, Author, Performer, length, rate);
      /*  if ((rate < 0)||(rate > 100)) 
            throw new wrongRate();
        if (length<0)
            throw new wrongLength();*/
        if (RemakeYear<0)
            throw new wrongYear();
        this.RemakeComposer = RemakeComposer;
        this.RemakeYear = RemakeYear;
    }
    @Override
        public String toString()
        {
            return this.id + " Имя автора - " + this.Author +
            ". Название произведения - " + this.name +
            ". Создана в жанре " + this.genre + " и первым исполнителем является " +
            this.Performer + ".\n Длительность композиции - " + this.length + " секунд(ы). Рейтинг - "
            + this.rate + ". Год ремейка: " + this.RemakeYear + ". Имя исполнителя ремейка: " + this.RemakeComposer + "\n";
        }       
    
    public RemakeComp(Music music, String RemakeComposer, int RemakeYear) throws wrongRate, wrongLength, wrongYear
    {
        super(music);
       /* if ((rate < 0)||(rate > 100)) 
            throw new wrongRate();
        if (length < 0)
            throw new wrongLength();*/
        if (RemakeYear < 0)
            throw new wrongYear();
        this.RemakeComposer = RemakeComposer;
        this.RemakeYear = RemakeYear;
    }
    @Override
        public String get_remake_composer()
        {
	        return this.RemakeComposer;
        }
    @Override
        public int get_remake_year()
        {
	        return this.RemakeYear;
        }
}
class CD_Player
{
    private String name;
    private String adress;
    private Music []collection;
    public CD_Player (String name, String adress, Music[]collection) throws IOException, wrongYear, wrongRate, wrongLength
    {
        this.name = name;
        this.adress = adress;
        this.collection = new Music[collection.length];
        System.arraycopy(collection, 0, this.collection, 0, collection.length);
        //for (int i = 0; i<collection.length;i++)
           //this.collection[i] = new Music (collection[i]);
    }
    @Override
        public String toString()
        {
            return "CD-Player: " + this.name + " adress: " + this.adress + "\n" + Arrays.toString(this.collection);
        }
    public String getMusicbyAuthor(String Author) //автор
    {
        StringBuffer sb = new StringBuffer();
        for (Music a: this.collection)
            if (a.get_Author().equalsIgnoreCase(Author))
                sb.append(a);
            return sb.toString();
    }
    public String getMusicbyGenre(Genre genre) //жанр
    {
        StringBuffer sb = new StringBuffer();
        for (Music a: this.collection)
            if (a.get_genre() == genre)
                sb.append(a);
            return sb.toString();
    }
    public String getMusicbyRate(int rate_min, int rate_max) //рейтинг
    {
        StringBuffer sb = new StringBuffer();
        for (Music a: this.collection)
            if ((a.get_rate() >= rate_min) && (a.get_rate() <= rate_max))
                sb.append(a);
            return sb.toString();
    }
    public void sortbyname()
    {
        Arrays.sort(this.collection, new Comparer_name());
    }
    public void sortbylength()
    {
        Arrays.sort(this.collection, new Comparer_length());
    }
}
public class Main
{
	public static void main(String[] args) 
	{
	    try	
	    {
	        FileInputStream ifr = new FileInputStream("input.txt");
            Scanner sr = new Scanner (ifr);
            PrintStream pw = new PrintStream("output.txt");
	        Music []collection = new Music[6];
	        int i = 0;
	        /*
	        {
	            new Music("Сладкое моё дитя",Genre.rock,"Ганс эн Роузес", "Аксель Роуз", 356, 90, 2015, Жасмин Томпсон),
	            new Music("Девица-весна", Genre.folk, "Таверна", "Кирилл Бард", 186, 85),
	            new Music("Грязь", Genre.rock, "Ария", "Валерий Кипелов", 283, 80),
	            new Music("Призрак Оперы", Genre.opera, "Эндрю Ллойд", "Майкл Кроуфорд",259, 87),
	            new Music("Маленький", Genre.pop, "Дайте танк", "Дмитрий Мозжухин", 244, 91),
	            new Music("Штиль", Genre.rock,"Ария","Валерий Кипелов", 293, 86)
	        };*/
	        while (sr.hasNext())
	        {
	            String str = sr.nextLine();
	            String []a = str.split("; ");
	            String name = a[0];
	            Genre genre = Genre.valueOf(a[1]);
	            String Author = a[2];
	            String Performer = a[3];
	            int length = Integer.parseInt(a[4]);
	            int rate = Integer.parseInt(a[5]);
	            if (a.length<=6)
	                collection[i++]= new Music(name, genre, Author, Performer,length,rate);
	            else 
	            {
	                int RemakeYear = Integer.parseInt(a[6]);
	                String RemakeComposer = a[7];
	                collection[i++] = new RemakeComp(name, genre, Author, Performer,length,rate, RemakeYear, RemakeComposer);
	            }
	        }
	        CD_Player playlist1 = new CD_Player("cd_player_1", "здесь могла быть ваша сслыка", collection);
	        
	        System.out.println("\n1 - Все композиции:");
	        pw.println("\n1 - Все композиции:");
	        //System.out.println(Arrays.toString(collection));
	        System.out.println(playlist1);
            pw.println(playlist1);
            
	        System.out.println("\n2 - произведения Арии:");
	        pw.println("\n2 - произведения Арии:");
            String name = "Ария";
            System.out.println(playlist1.getMusicbyAuthor(name));
            pw.println(playlist1.getMusicbyAuthor(name));
            
            System.out.println("\n3 - композиции жанра Рок:");
            pw.println("\n3 - произведения жанра Рок:");
            System.out.println(playlist1.getMusicbyGenre(Genre.rock));
            pw.println(playlist1.getMusicbyGenre(Genre.rock));
            
            System.out.println("\n4 - композиции с рейтнгом от 88 до 96: ");
            pw.println("\n4 - композиции с рейтнгом от 88 до 96: ");
            System.out.println(playlist1.getMusicbyRate(88, 96));
            pw.println(playlist1.getMusicbyRate(88, 96));
            
            System.out.println("\n5 - композиции по убыванию продолжительности:");
            pw.println("\n5 - композиции по убыванию продолжительности:");
            playlist1.sortbylength();
            System.out.println(playlist1);
            pw.println(playlist1);
            
            System.out.println("\n6 - композиции в алфавитном порядке: ");
            pw.println("\n6 - композиции в алфавитном порядке: ");
            playlist1.sortbyname();
            System.out.println(playlist1);
            pw.println(playlist1);
            System.out.println("Количество композиций в коллекции := " + Music.get_count()+'\n');
            pw.println("Количество композиций в коллекции := " + Music.get_count()+'\n');
            System.out.println("Изменим рейтинг 4-ой песни на 99");
            pw.println("Изменим рейтинг 4-ой песни на 99");
            collection[3].set_rate(99);
            for(Music ph : collection)
                if(ph.get_id() == 4)
                {
                    System.out.print(ph);
                    pw.println(ph);
                }
            System.out.print("Год ремейка песни Сладкое моё дитя: ");
            pw.print("Год ремейка песни Сладкое моё дитя: ");
            for(int j = 0; j < collection.length; j++)
            {
                if (collection[j].get_name().equalsIgnoreCase("Сладкое моё дитя"))
                    {
                       System.out.println(collection[j].get_remake_year());
                       pw.println(collection[j].get_remake_year());
                    }
            }
            System.out.print("Исполнитель ремейка песни Штиль: ");
            pw.print("Исполнитель ремейка песни Штиль: ");
            for(int j = 0; j < collection.length; j++)
            {
                if (collection[j].get_name().equalsIgnoreCase("Штиль"))
                {
                       System.out.println(collection[j].get_remake_composer());
                       pw.println(collection[j].get_remake_composer());
                }
            }
            System.out.print("Исполнитель ремейка песни Девица-весна: ");
            pw.print("Исполнитель ремейка песни Девица-весна: ");
            for(int j = 0; j < collection.length; j++)
            {
                if (collection[j].get_name().equalsIgnoreCase("Девица-весна"))
                {
                       System.out.println(collection[j].get_remake_composer());
                       pw.println(collection[j].get_remake_composer());
                }
            }
            System.out.println("Количество песен в вашей коллекции: " + Music.get_count());
            pw.println("Количество песен в вашей коллекции: " + Music.get_count());
	    }
	    catch (wrongLength e)
	    {
	        System.out.println("Некоторые композиции имеют отрицательую длительность");
	    }
	    catch (wrongYear e)
	    {
	        System.out.println("Ваша песня слишком старая или ещё не вышла");
	    }
	    catch (wrongRate e)
	    {
	        System.out.println("Ваш рейтинг для песни вышел за пределы [0; 100]");
	    }
	    catch (IOException e)
	    {
	        System.out.println("Не удалось открыть файл!");
	    }
	}
}


