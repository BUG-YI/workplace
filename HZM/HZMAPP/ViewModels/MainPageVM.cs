using System.Collections.ObjectModel;
using System.Windows.Input;
using CommunityToolkit.Mvvm.Input;
using HZMAPP.Models;

namespace HZMAPP.ViewModels;

public class MainPageVM
{
    public ObservableCollection<MainPageM> NavbarTitle { get; } = new ObservableCollection<MainPageM>
    {
        new MainPageM{ Title = "首页", Tag = "home"},
        new MainPageM{ Title = "应用", Tag = "app"},
        new MainPageM{ Title = "应用商城", Tag = "sources"},
        new MainPageM{ Title = "设置", Tag = "settings"}
    };
}