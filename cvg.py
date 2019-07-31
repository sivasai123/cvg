import java.util.Scanner;
class example
{
	public static void main(String args[])
	{
		Scanner in=new Scanner(System.in);
		System.out.print("Enter any number : ");
		int number=in.nextInt();
		int i=1,count=0;
		while(i<=number)
		{
			if(number%i==0)
			{
				count++;
			}
			i++;
		}
		if(count>2)
		{
			System.out.println(number+" is composite number ");
		}
		else
		{
			System.out.println(number+" is not composite number");
		}
	}
}
