using System.Windows.Controls;
using System.Windows;
using System.Diagnostics;
using System.Drawing;
using System.Windows.Input;
using HZMAPP.ViewModels;
using HZMAPP.Views.AppDetail;

namespace HZMAPP.Views.AppStore;

public partial class AppStorePage : Page
{
    public AppStorePage()
    {
        InitializeComponent();
    }


    private void UIElement_OnMouseLeftButtonDown(object sender, MouseButtonEventArgs e)
    {
        AppDetailWindow win = new AppDetailWindow();
        win.Owner = Window.GetWindow(this);
        win.ShowDialog();
    }
}