using AdapterDemo.Framework;
using AdapterDemo.App.Plugins;

var dashboard = new Dashboard(new Spreadsheet());
dashboard.Render(new EarthAdapter(new Earth()));