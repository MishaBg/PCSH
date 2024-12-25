using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figures
{
    class Rectangle : Figure, IPrint
    {
        /// <summary>
        /// Высота
        /// </summary>
        private double _height;

        public double height
        {
            get => _height;
            set
            {
                if (value > 0)
                {
                    _height = value;
                }
            }
        }


        /// <summary>
        /// Ширина
        /// </summary>
        private double _width;

        public double width
        {
            get => _width;
            set
            {
                if (value > 0)
                {
                    _width = value;
                }
            }
        }
        /// <summary>
        /// Основной конструктор
        /// </summary>
        /// <param name="ph">Высота</param>
        /// <param name="pw">Ширина</param>
        public Rectangle(double ph, double pw)
        {
            this.height = ph;
            this.width = pw;
            this.Type = "Прямоугольник";
        }

        /// <summary>
        /// Вычисление площади
        /// </summary>
        public override double Area()
        {
            return this.width * this.height;
        }

        public void Print()
        {
            Console.WriteLine(this.ToString());
        }
    }
}
