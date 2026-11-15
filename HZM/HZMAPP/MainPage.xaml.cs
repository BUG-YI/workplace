using System.Collections.Specialized;
using System.ComponentModel;
using System.Runtime.CompilerServices;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using HZMAPP.Models;
using HZMAPP.ViewModels;
using HZMAPP.Views.AppDetail;
using HZMAPP.Views.Apps;
using HZMAPP.Views.AppStore;
using HZMAPP.Views.Home;

namespace HZMAPP;

public partial class MainPage : Page

{

    public MainPage()
    {
        InitializeComponent();
        ContentPage.Navigate(new AppStorePage());
    }

    private void Navbar_Mouse(object sender, MouseEventArgs e)
    {
        
    }

    private void Selector_OnSelectionChanged(object sender, SelectionChangedEventArgs e)
    {
        if (sender is ListView listView && listView.SelectedItem is MainPageM item)
        {
            PageT.Text = item.Title;
            switch (item.Tag)
            {
                case "home":
                    ContentPage.Navigate(new Home());
                    break;
                
                case "app":
                    ContentPage.Navigate(new Apps());
                    break;
                
                case "sources":
                    ContentPage.Navigate(new AppStorePage());
                    break;
                
                case "settings":
                    ContentPage.Navigate(new AppDetailPage());
                    
                _:
                    break;
            }
        }
    }
}