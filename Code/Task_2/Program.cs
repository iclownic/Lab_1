using System;
using System.Collections.Generic;

namespace Task_2
{
    internal class Program
    {
        static void Main(string[]_)
        {
            try
            {
                Dictionary<string, string> dic = new Dictionary<string, string>()
                {
                    {"France", "Paris"},
                    {"Germany", "Berlin"},
                    {"Italy", "Rome"},
                    {"Spain", "Madrid" }
                };

                List<string> country = new List<string>();
                List<string> capital = new List<string>();

                foreach (var item in dic)
                {
                    country.Add(item.Key);
                    capital.Add(item.Value);
                }

                for (int i = 0; i < dic.Count; i++)
                {
                    Console.WriteLine("Country: " + country[i]);
                    Console.WriteLine("Capital: " + capital[i] + "\n");
                }
            }

            catch (Exception ex)
            {
                Console.WriteLine($"Помилка: {ex.Message}");
            }

            Console.ReadKey();
        }
    }
}
