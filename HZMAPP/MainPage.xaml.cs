using Microsoft.UI.Xaml.Controls;

// To learn more about WinUI, the WinUI project structure,
// and more about our project templates, see: http://aka.ms/winui-project-info.

namespace HZMAPP;

/// <summary>
/// The main content page displayed inside the application window.
/// Add your UI logic, event handlers, and data binding here.
/// </summary>
public sealed partial class MainPage : Page
{
    public MainPage()
    {
        InitializeComponent();

        ContentPage.Navigate(typeof(HomePage));

        // TODO: Add your initialization logic here.
    }


    private void NavigationView_OnSelectionChanged(NavigationView sender, NavigationViewSelectionChangedEventArgs args)
    {
        if (args.SelectedItem is NavigationViewItem item && item.Tag is string tag)
        {
            Type page = tag switch
            {
                "home" => typeof(HomePage),
                "setting" => typeof(SettingPage),
                _ => typeof(HomePage)
            };

            ContentPage.Navigate(page);
        }
    }
}
