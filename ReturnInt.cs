using System;
using System.Linq;

public delegate string ReturnStr();

public class ReturnInt {
	public static Func<int> RetRndNum; 
	public static Func<int> IterNum;

	public static ReturnStr	GetName;

	public static void Main(string[] args) {
		foreach(var r in Enumerable.Range(1,100).Select(i =>
					new Random(new Random(Environment.TickCount).Next(0,10000)).Next(0, 100))) {
			Console.WriteLine( r);
		}
		RetRndNum = {return new Random().Next(0,10);};

		GetName = () => {
			return 
		
	}
}

