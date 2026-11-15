using System.Collections.ObjectModel;
using System.Windows.Media;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using HZMAPP.Models;

namespace HZMAPP.ViewModels;

public partial class AppstorePageVM:ObservableObject
{
    public ObservableCollection<AppstorePageM> AppstorePageMs { get; } = new ();
    public ObservableCollection<int> Apps { get; } = new() { 1,2,2,3};
    public AppstorePageVM()
    {
        var myLis = new List<AppstorePageM>
        {
            new AppstorePageM
            {
                Name = "Python",
                Version = ["3.17", "3.12","124","09"]
            },
            new AppstorePageM
            {
                Name = "asf",
                Version = ["1.2"]
            }
        };

        var processedList = myLis.Select((item, i) =>
        {
            item.ItemColor = i % 2 == 0 ? Brushes.Wheat : Brushes.Aquamarine;
            return item;
        });

        foreach (var m in processedList)
        {
            AppstorePageMs.Add(m);
        }
        
        
    }
}