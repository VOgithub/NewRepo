using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_01
{
    public class Functsioonid
    {
        public static void Tervitus(string nimi) 
        {
            Console.WriteLine("Tere kallis, {0}", nimi);
        }

        public static int Korruta(int arv1,int arv2) 
        {  //vozvrat int arv1*arv2
            return arv1*arv2;
        }
    }
}
