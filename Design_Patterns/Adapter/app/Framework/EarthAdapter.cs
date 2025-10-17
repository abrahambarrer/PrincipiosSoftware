using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AdapterDemo.App.Plugins;

namespace AdapterDemo.App.Framework
{
  public class EarthAdapter : IGraphic
  {
    private Earth earth;

    public EarthAdapte(Earth earth) {
      this.earth = earth;
    }

    public void Generate(Spreadsheet doc)
    {
      earth.Render(doc);
    }
  }
}