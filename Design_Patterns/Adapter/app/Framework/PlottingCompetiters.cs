using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterDemo.Framework
{
  public class PlottingCompetitors : IGraphic
  {
    public void Generate(Spreadsheet doc)
    {
      Console.WriteLine("Showing Plotting graphic");
    }
  }
}