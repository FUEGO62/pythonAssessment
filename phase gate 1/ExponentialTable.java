public class ExponentialTable{

    public static void main(String[] args){

	int a = 1;

	int b = 2; 

	String space = "    ";

	System.out.println("a    b    a**b");

	for(int count = 0; count < 5; count++){

		System.out.println(a+space+b+space+ (int)Math.pow(a,b));
		a ++;
		b ++;

	}

    }

}