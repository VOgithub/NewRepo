using CSharp_01;
using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp_01
{
    public class ClassMain
    {
        public static void Main(string[] args)

        {
            Console.OutputEncoding = Encoding.UTF8;
            Random random = new Random();
            //3 B. Praktika
            Console.WriteLine("Ülesanne 5. \n "); //Küsi kasutajalt 4 arvu ning väljasta nendest koostatud suurim neliarvuline arv.
            Console.WriteLine("Sisesta 4 arvu 1 ja 9 vahel: \n ");
            int Tmp = 0;
            int[] arvu = new int[4];
            for (int s = 0; s < arvu.Length; s++)
            {
                Console.Write(" Sisesta {0} arvu: ", s+1);
                Tmp = int.Parse(Console.ReadLine());
                //if (0 << Tmp >= 9)
                //{
                arvu[s] = Tmp;
                //    Console.WriteLine(arvu[s]);
                    
                //}
            }
            for (int s = 0;s < arvu.Length; s++)
            {
                //Console.Write("S -{0}: {1}   >> ", s, arvu[s]) ;
                for (int s1 = s + 1; s1 < arvu.Length ; s1++)
                {
                    //Console.WriteLine("S1 -{0} : {1}", s1, arvu[s1]) ;
                    if ( arvu[s1] > arvu[s] ) 
                    {
                        Tmp = arvu[s];
                        arvu[s] = arvu[s1];
                        arvu[s1] = Tmp;
                       // Console.Write(arvu[s]);

                    }
                    
                }
                //Console.WriteLine( arvu[s]+ " ");
                
            }
            Console.Write("\n Suurim arv - ");
            for (int s = 0; s < arvu.Length; s++)
            {
                Console.Write(arvu[s]) ;
            }
            Console.WriteLine();
            Console.ReadLine();
            Console.Clear();
                /// 
                Console.WriteLine("\nÜlesanne 4. \n "); // Mis arv mõtles välja arvuti? Kasuta vähemalt 5 katset, et seda teada. 
            int Arv = random.Next(1, 10);
            int Answer = 0;
            do
            {
                Console.Write(" Arve ära, mis arvu ma mõtles välja 1 ja 10 vahel..(spikker:{0}) Kirjuta: ",Arv);
                Answer = int.Parse(Console.ReadLine());
                if (Answer != Arv)
                {
                    Console.WriteLine("No, proovi uuesti!");
                }

            } while (Answer != Arv);
            Console.WriteLine("Tore, sa võid! \n");


            //Ulesanne 3. * Ütle kasutajale "Osta elevant ära!". Senikaua korda küsimust, kuni kasutaja lõpuks ise kirjutab "elevant". 
            Console.WriteLine("Ülesanne 3. Elevant");
            string El = "";

            do
            {
                Console.Write("Osta elevant ära! Sinu vastus ( print 'elevant' for exit) - ?  ");
                El = Console.ReadLine().ToLower();


            } while (El != "elevant");
            Console.WriteLine("Tore, sa ostsid elevandi ära! \n");
            
            //Console.Clear();

            Inimene[] mehed = new Inimene[4];
            mehed[1]    = new Inimene("Margus",25);
            mehed[2]    =   new Inimene("Mati",45);
            mehed[0] = new Inimene("Paul", 65);
            Inimene mees3 = new Inimene();  // teine variant
            mees3.Nimi = "Peeter";          //
            mees3.Vanus = 19;               //
            mehed[3] = mees3;               //

            foreach (Inimene mees in mehed)
            {
                Console.WriteLine(mees.Nimi + " " + mees.Vanus);

            }
            Console.ReadLine();


            ///3 osa. Praktika
            ///
            ///Ulesanne 1 * Loo  juhuslikult arvud N ja M ja sisesta massiivi arvud N'st M'ni. Trüki arvude ruudud ekraanile.
            ///N ja M arvud on vahemikus (-100,100).
           // Random random = new Random();
            Console.Clear();
            // Console.ForegroundColor= ConsoleColor.Yellow;
           
            int N = random.Next(1, 5);
            int M = random.Next(6, 15);
            int[] arvud_N_M = new int[M-N+1];

            Console.WriteLine(" N = {0}, M= {1}\n", N, M);

            for (int i = 0; i < arvud_N_M.Length;i++)
            {
                arvud_N_M[i] = N;
                Console.Write(" {0}", Math.Pow(arvud_N_M[i],2));
                N++;

            }


            // Ulesanne 2 * Küsi kasutajalt viis arvu, salvesta neid massiivi ning väljasta nende summa, aritmeetiline keskmine ja korrutis.
            Console.ReadLine() ;
            Console.Clear() ;
            Console.WriteLine("Ülesanne 2. Summ, Keskmine ja Korrutis");
            double[] Mass_5 = new double[5];
            double  Summa = 0;
            double Kesk = 0;
            double Korr = 1;

            for (int i = 0;i < 5;i++)
            {
                Console.Write("Sisesta {0} parameeter : ", i);
                Mass_5[i] = double.Parse(Console.ReadLine());
                //Console.WriteLine(Mass_5[i]);
                Summa = Summa + Mass_5[i];
                Kesk = Summa/(i+1);
                Korr = Korr * Mass_5[i];
                Console.WriteLine("Summ= {0}, Kesk = {1}, Korr = {2} ", Summa, Kesk, Korr);


            }




            ///3 osa Massivid
            //string[] nimed = new string[8] { "A", "B", "C", "D", "E", "F", "G", "H" };
            //nimed[2] = "Anna";
            //int nr = 0;
            //while (nr < 8)
            //{
            //    Console.WriteLine("Tere, {0} õpilane, while {1} < 8 " , nimed[nr], nr);
            //    nr++;
            //}
            //Console.WriteLine("\n");

            //for (int i = 0; i < nimed.Length; i++)
            //{
            //    Console.WriteLine("Tere, {0} õpilane, Lenght {1}", nimed[i], i);
            //}
            //Console.WriteLine("\n");
            //foreach (var nimi in nimed)
            //{
            //    Console.WriteLine("Tere, {0} õpilane, foreach", nimi);
            //}
            //Console.WriteLine("Named.Lenght = {0} \n", nimed.Length);
            //nr = 0;
            //do
            //{
            //    Console.WriteLine("Tere, {0} õpilane, do nr++", nimed[nr]);
            //    nr++;
            //} while (nr != nimed.Length);


            //3 osa
            //ConsoleKeyInfo key = new ConsoleKeyInfo();
            //do
            //{
            //    Console.WriteLine("Push a backspace button!");
            //    key= Console.ReadKey();  /* lubaja key!!*/

            //} while(key.Key !=ConsoleKey.Backspace);  /*object.svoistvo !=*/

            //int a=0; 
            //while(a<10)
            //{
            //    Console.WriteLine(a);
            //    a++;

            //}






            //2 osa

            //Inimene naine = new Inimene();
            //naine.Nimi = "Kati";
            //naine.Vanus = 18;

            //Inimene mees = new Inimene("Mati");
            //mees.Vanus = 100;
            //List<Inimene> inimesed= new List<Inimene>();
            //inimesed.Add(mees);
            //inimesed.Add(naine);
            //inimesed.Add(mees);
            //inimesed.Add(naine);
            //inimesed.Add(new Inimene() { Nimi = "Kadri", Vanus = 25 });

            //foreach(Inimene inimene in inimesed)  /*Variant 1*/
            //{
            //    Console.WriteLine(inimene.Nimi +", vanus on "+ inimene.Vanus);
            //}
            //Console.WriteLine("\n");
            //Dictionary<int, Inimene> opilased = new Dictionary<int, Inimene>();
            //opilased.Add(501, mees);
            //opilased.Add(601, naine);
            //opilased.Add(602, new Inimene() { Nimi = "Kadri", Vanus = 25 });
            //foreach (Inimene item in opilased.Values)   /*   Variant 2*/
            //{
            //    Console.WriteLine(item.Nimi );
            //}
            //Console.WriteLine("Teine variant -\n");
            //foreach (KeyValuePair<int,Inimene> item in opilased)   /* Variant 3*/
            //{
            //    Console.WriteLine(item.Key+ ": "+item.Value.Nimi+ "("+item.Value.Vanus+")");

            //}





            //1 B osa

            //ArrayList arrayList= new ArrayList();
            //arrayList.Add("Esimene");
            //arrayList.Add("Teine");
            //arrayList.Add("Kolmas");
            //Console.WriteLine("Mida otsime_");
            //string value = Console.ReadLine();
            //if (value != null)
            //{
            //    if (arrayList.Contains(value))
            //    {
            //        Console.WriteLine("Kokku: " + arrayList.Count);
            //        Console.WriteLine("Otsiv sõna - " + arrayList.IndexOf(value) + " kohal\n");

            //    }
            //}
            //else 
            //{
            //    Console.WriteLine("Vaja midagi otsida!");
            //}
            //arrayList.Insert(3,"Neljas");
            //arrayList.Insert(0, "Zero");
            //arrayList.RemoveAt(2);   // remove at 2 pozition
            //arrayList.Remove(value);

            //for(int i = 0;i < arrayList.Count; i++) 
            //{
            //    Console.WriteLine(" "+i+ " "+ arrayList[i]);

            //}


            //1 A osa


            //List<string> kuude_list = new List<string>();
            //try
            //{
            //    foreach (string rida in File.ReadAllLines(@"..\..\..\TextFile1.txt"))
            //    {
            //        kuude_list.Add(rida);

            //    }

            //}
            //catch (Exception)
            //{
            //    Console.WriteLine("Viga failiga!");
            //}
            //foreach (string kuu in kuude_list)
            //{
            //    Console.WriteLine(kuu);
            //}
            //kuude_list.Remove("Juuni");
            //Console.WriteLine("\n _________________\n");
            //foreach (string kuu in kuude_list)
            //{
            //    Console.WriteLine(kuu);
            //}



            //1 osa


            Console.WriteLine("\nHello, C#  World!\n");

            //string nimi = "Python";
            //Functsioonid.Tervitus(nimi);


            //int a = 0;
            //string tekst = "Tere";
            //char taht = 'A';
            //double arv = 3.55555;
            //float arv1 = 2;
            //int korrutis = Functsioonid.Korruta((int)arv, (int)arv1);
            //Console.WriteLine(korrutis);

            //Console.WriteLine(tekst);
            //Console.WriteLine(taht);
            //Console.Write("Sisesta uus parameeter a: ");
            //a = int.Parse(Console.ReadLine());

            //Console.Write("Tehe: ");
            //taht = char.Parse(Console.ReadLine());
            //if (taht == '+') // && - and, || - or, ! - not
            //{
            //    Console.WriteLine("Arvude {0}, {1} ja {2} summa={3}", a, arv, arv1, arv + arv1 + a);
            //}
            //else if (taht == '*')
            //{
            //    Console.WriteLine("Arvude {0}, {1} ja {2} korrutis={3}", a, arv, arv1, arv * arv1 * a);
            //}
            //else
            //{
            //    Console.WriteLine("Kirjuta ise!");
            //}
            ///*
            // nimi: Juku-ga lähame kinno! 
            // vanus: Kui vana Juku on. 
            // pilet: Tasuta,Laste,Täis,Soodus. Viga! kui <0, >123
            //*/
            //Console.WriteLine("Tere!\nMis on sinu nimi?");
            //nimi = Console.ReadLine();
            //Console.WriteLine("Tere " + nimi);
            //if (nimi.ToUpper() == "JUKU")
            //{
            //    Console.WriteLine("Lähme kinno!");
            //    try
            //    {
            //        Console.WriteLine("{0},\nKui vana sa oled?", nimi);
            //        int vanus = int.Parse(Console.ReadLine());
            //        if (vanus <= 0 || vanus > 123)
            //        { Console.WriteLine("Viga!"); }
            //        else if (vanus > 0 && vanus <= 6)
            //        { Console.WriteLine("Tasuta pilet!"); }
            //        else if (vanus <= 15)
            //        { Console.WriteLine("Lastepilet!"); }
            //        else if (vanus <= 65)
            //        { Console.WriteLine("Täispilet!"); }
            //        else if (vanus <= 100)
            //        { Console.WriteLine("Sooduspilet!"); }
            //    }
            //    catch (Exception e)
            //    {
            //        Console.WriteLine(e);
            //    }
            //}
            //else
            //{
            //    Console.WriteLine("Mõtle ise reaktsioon välja!");
            //}
            //Console.WriteLine("Switch'i kasutamine");
            //Random random = new Random();
            //int paeva_nr = random.Next(1, 7);
            //string paev;
            //Console.WriteLine(paeva_nr);
            //switch (paeva_nr)
            //{
            //    case 1: paev = "Esmaspäev"; break;
            //    case 2: paev = "Teisipäev"; break;
            //    case 3: paev = "Kolmapäev"; break;
            //    case 4: paev = "Neljapäev"; break;
            //    case 5: paev = "Reede"; break;
            //    case 6: paev = "Laupäev"; break;
            //    case 7: paev = "Pühapäev"; break;
            //    default:
            //        paev = "Tundmatu päev";
            //        break;
            //}
            //Console.WriteLine(paev);
        }
    }
}
