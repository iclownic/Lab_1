using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Task_3
{
    internal class Program
    {
        static void Main(string[]_)
        {            
            try
            {
                List<int> list = new List<int>() { -21, 33, 146, 53, 4 };
                var selectedList = list.Where(i => i > 0).Select(i => i % 10).Distinct();

                foreach (var i in selectedList)
                {
                    Console.WriteLine(i);
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