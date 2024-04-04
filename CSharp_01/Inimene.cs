using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_01
{
    public class Inimene
    {
        public string Nimi { get; set; }
        public int Vanus { get; set; }

        public Inimene() { }
        public Inimene(string nimi) 
        {
            Nimi = nimi;
        }
        public Inimene(string nimi, int vanus) // if vanus=100 then 100 for all  if not concreted
        {
            Nimi = nimi;
            Vanus = vanus;
        }
    }
}
