using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Enc_consol
{
    class Program
    {
        static void Main(string[] args) {
            Console.WriteLine("Welcome to the Encoder calculator consol application to check functionality before gui" +
                "\nWhat DPI:\n");
            Console.WriteLine( );
            string S_DPI = Console.ReadLine( );
            int DPI = Convert.ToInt32(S_DPI);
            Console.WriteLine(  "{0}", DPI  );



            Console.WriteLine("How many pulses per meter:\n");
            Console.WriteLine();
            string S_PPM = Console.ReadLine();
            int PPM = Convert.ToInt32(S_PPM);
            PPM = (PPM / 39); 
            Console.WriteLine("{0}", PPM);




            // Keep Console open until I close it
            Console.WriteLine("Press any key to close");
            Console.ReadKey();
        
    }
    }
}
