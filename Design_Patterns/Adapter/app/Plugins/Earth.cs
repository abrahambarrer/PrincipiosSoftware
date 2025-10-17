using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdapterDemo.App.Plugins
{
  public class Earth
  {
    public void Render(Spreeadsheet _document)
    {
      Console.WriteLine("Rendering Earth visible");
    }
  }
}