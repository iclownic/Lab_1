using System;
using System.Collections.Generic;

namespace Task_1
{
    internal class Program
    {       
        static void Main(string[]_)
        {
            try
            {
                List<string> text = new List<string>()
                {
                    "Banana",
                    "banana",
                    "BANANA",
                    "I love banana",
                    "Apple",
                };

                for (int i = 0; i < text.Count; i++)
                    text[i] = text[i].ToLower();

                for (int i = 0; i < text.Count; i++)
                {
                    while (i != text.LastIndexOf(text[i]))
                    {
                        text.RemoveAt(text.LastIndexOf(text[i]));
                    }
                }

                foreach (var word in text)
                {
                    Console.WriteLine(word);
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
