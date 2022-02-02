using System;
using static System.Console;

class Program {
  static void Main(string[] args) {
    Write("Number of rows: ");
    int r = int.Parse(ReadLine()); // 5

    Write("\nNumebr of cols: ");
    int c = int.Parse(ReadLine()); // 3

    int count = r * c;             // 15 -> how many primes we want
    int current = 0;               // starting value for primes from 0..count

    var ret = new int[r, c];       // 2d array return value
    while (count != 0) {
      if (isPrime(current)) {
        insert(ret, current); count -= 1;
      }
      current += 1;
    }

    // Output
    for(int i = 0; i < r; ++i) {
      for(int j = 0; j < c; ++j)
        Write(ret[i, j] + " ");
      WriteLine();
    }
  }

  public static void insert(int[,] ret, int val) {
    for(int i = 0; i < ret.GetLength(0); ++i) {
      for(int j = 0; j < ret.GetLength(1); ++j) {
        if (ret[i, j] == 0) { ret[i, j] = val; return; }
      }
    }
  }

  public static bool isPrime(int n) {
    if (n <= 1)
      return false;
    else if (n % 2 == 0)
      return n == 2;

    for(int i = 3; i <= Math.Sqrt(n); i += 2)
      if (n % i == 0) return false;

    return true;
  }
}
