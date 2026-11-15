using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;
using HZMAPP.Models;

namespace HZMAPP.ViewModels;

public partial class AppDetailVM:ObservableObject
{
    
    [ObservableProperty] private ApplicationsM _stars = new ApplicationsM
    {
        Name = "",
        Star = new Dictionary<string, object>()
        {
            {"1","71"},
            {"2","31"},
            {"3","61"},
            {"4","21"},
            {"5","21"},
        }
    };
    
    [ObservableProperty]
    private ApplicationsM _preImage = new ApplicationsM { Name = "s", ImageAddr = "/Assets/Test/1.jpg"};
    public ObservableCollection<ApplicationsM> ApplicationsDetail { get; }= new ObservableCollection<ApplicationsM>
    {
        new ApplicationsM
        {
            Name = "s2df",
            ImageAddr = "/Assets/Test/1.jpg"
        },
        new ApplicationsM
        {
            Name = "sd1f",
            ImageAddr = "/Assets/Test/2.jpg"
        },
        new ApplicationsM
        {
            Name = "s3df",
            ImageAddr = "/Assets/Test/3.jpg"
        },
        new ApplicationsM
        {
            Name = "sd4f",
            ImageAddr = "/Assets/Test/4.jpg"
        }
    };

    [RelayCommand]
    private void ChangePreImage(ApplicationsM m)
    {
        PreImage = new ApplicationsM
        {
            Name = "",
            ImageAddr = m.ImageAddr
        };
        Console.WriteLine(m.ImageAddr);
    }
}