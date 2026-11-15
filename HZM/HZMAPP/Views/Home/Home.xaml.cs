using System.Collections.ObjectModel;
using System.Windows;
using System.Windows.Controls;

namespace HZMAPP.Views.Home;

public partial class Home : Page
{
    public Home()
    {
        InitializeComponent();
    }

    private void SignIn(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn)
        {
            if ("0".Equals(btn.Tag))
            {
                Console.WriteLine(123);
            }
            else
            {
                Console.WriteLine("asdf");
            }
        }
    }

    private void StartApp(object sender, RoutedEventArgs e)
    {
        Console.WriteLine("start");
        if (sender is Button btn)
        {
            var d = btn.DataContext;
            Console.WriteLine(d);
        }
    }

    private void ThreePinter(object sender, RoutedEventArgs e)
    {
        Console.WriteLine("pinter");
        if (sender is Button btn)
        {
            var d = btn.DataContext;
            
        }
    }
}