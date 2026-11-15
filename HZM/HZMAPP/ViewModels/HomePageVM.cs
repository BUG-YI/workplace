using System.Collections.ObjectModel;
using System.Runtime.CompilerServices;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace HZMAPP.ViewModels;

public partial class HomePageVM
{
    public ObservableCollection<int> Lis { get; } = new ObservableCollection<int>() { 1,2,3,4,5,6 };

    private string[] NewWindows { get; } = [];

    [RelayCommand]
    private void ChangeWindow()
    {
        
    }

    [RelayCommand]
    private void StartApp()
    {
        
    }
}