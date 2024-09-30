import java.util.Scanner;
public class DaysOfTheWeek{

    public static void main(String[] args){

	Scanner input = new Scanner(System.in);
	
	System.out.println("Enter todays day");	
	
	int dayInNumbers = input.nextInt();

	System.out.print("Enter number of days elapsed since today ");

        int futureDayInNumbers = input.nextInt() + dayInNumbers;

	String day = getDay(dayInNumbers);

	String futureDay = getDay(futureDayInNumbers);

	
System.out.print("Todays day is "+ day+ " and the future day is "+futureDay );

    }

    public static String getDay( int dayInNumbers){
	
	String day = "";

	switch(dayInNumbers){

		case 0 : day = "Sunday";break;

		case 1 : day = "Monday";break;

		case 2 : day = "Tuesday";break;

		case 3 : day = "Wednesday";break;

		case 4 : day = "Thursday";break;

		case 5 : day = "Friday";break;

		case 6 : day = "Saturday";break;

	}

	return day;

    }

}