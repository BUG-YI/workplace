using System.Windows;
using System.Windows.Controls;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using HZMAPP.Models;
using HZMAPP.ViewModels;

namespace HZMAPP.Views.AppDetail;

public partial class AppDetailWindow : Window
{
    public AppDetailWindow()
    {
        InitializeComponent();
    }

    private void CloseThisWindow(object sender, MouseButtonEventArgs e)
    {
        this.Close();
    }

    private void WindowMove(object sender, MouseButtonEventArgs e)
    {
        if (e.ButtonState == MouseButtonState.Pressed)
        {
            this.DragMove();
        }
    }

    private void UIElement_OnPreviewMouseWheel(object sender, MouseWheelEventArgs e)
    {
        var h = sender as ScrollViewer;
        if (h != null)
        {
            h.ScrollToHorizontalOffset(h.HorizontalOffset - e.Delta * .3);
            e.Handled = true;
        }
    }

    private void PreviewPicture(object sender, MouseButtonEventArgs e)
    {
        if (sender is FrameworkElement{DataContext:ApplicationsM app} border)
        {
            if (DataContext is AppDetailVM vm)
            {
                vm.ChangePreImageCommand.Execute(app);
            }
        }
    }
}