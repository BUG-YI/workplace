using System.Windows;
using System.Windows.Controls;
using HZMAPP.ViewModels;

namespace HZMAPP.Views.LR;

public partial class Login : Page
{
    public Login()
    {
        InitializeComponent();
    }

    private void PasswordBox_OnPasswordChanged(object sender, RoutedEventArgs e)
    {
        if (DataContext is LoginVM vm)
        {
            vm.Password = ((PasswordBox)sender).Password;
        }
    }
}