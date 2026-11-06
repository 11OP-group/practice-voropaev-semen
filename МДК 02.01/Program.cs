using System;
namespace GladiatorBattle
{
    internal class Program
    {
        static Random rand = new Random();
        static void Main(string[] args)
        {
            double health1, health2, armor1, armor2;
            double attack1, attack2;
            double endHealth1, endHealth2;

            Console.WriteLine("Введите начальное здоровье первого гладиатора:");
            health1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Введите крепость брони первого гладиатора (0-100):");
            armor1 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Введите начальное здоровье второго гладиатора:");
            health2 = Convert.ToDouble(Console.ReadLine());

            Console.WriteLine("Введите крепость брони второго гладиатора (0-100):");
            armor2 = Convert.ToDouble(Console.ReadLine());

            if (health1 <= 0 || health2 <= 0 ||
                armor1 < 0 || armor1 > 100 ||
                armor2 < 0 || armor2 > 100)
            {
                Console.WriteLine("Ошибка! Проверьте введённые данные.");
                Console.ReadKey();
                return;
            }

            attack1 = rand.Next(10, 31);
            attack2 = rand.Next(10, 31);

            endHealth1 = health1 - attack2 * (1 - armor1 / 100);
            endHealth2 = health2 - attack1 * (1 - armor2 / 100);

            endHealth1 = Math.Max(0, endHealth1);
            endHealth2 = Math.Max(0, endHealth2);

            Console.WriteLine("\n--- Результаты боя ---");
            Console.WriteLine($"Атака первого гладиатора: {attack1}");
            Console.WriteLine($"Атака второго гладиатора: {attack2}");
            Console.WriteLine($"Здоровье первого: {endHealth1:F1}");
            Console.WriteLine($"Здоровье второго: {endHealth2:F1}");

            if (endHealth1 > endHealth2)
            {
                Console.WriteLine("Победил первый гладиатор!");
            }
            else if (endHealth2 > endHealth1)
            {
                Console.WriteLine("Победил второй гладиатор!");
            }
            else
            {
                Console.WriteLine("Ничья!");
            }

            Console.ReadKey();
        }

    }
}