using System.Windows;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace HZMAPP.ViewModels;

public partial class LoginVM:ObservableObject
{
    [ObservableProperty] 
    private string username = "";

    [ObservableProperty] 
    private string password = "";

    [RelayCommand]
    private void Login()
    {
        if (Username.Equals("a") && Password.Equals("a"))
        {
            MessageBox.Show("success");
        }
        else
        {
            MessageBox.Show("failed");
        }
    }
}