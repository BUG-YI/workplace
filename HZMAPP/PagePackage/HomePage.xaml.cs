using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Microsoft.UI;
using Microsoft.UI.Xaml;
using Microsoft.UI.Xaml.Controls;
using Microsoft.UI.Xaml.Controls.Primitives;
using Microsoft.UI.Xaml.Data;
using Microsoft.UI.Xaml.Input;
using Microsoft.UI.Xaml.Media;
using Microsoft.UI.Xaml.Navigation;
using Windows.UI;
using ABI.Windows.Media.Devices;
using HZMAPP.Models;
using Microsoft.UI.Xaml.Media.Imaging;


// To learn more about WinUI, the WinUI project structure,
// and more about our project templates, see: http://aka.ms/winui-project-info.

namespace HZMAPP;

/// <summary>
/// An empty page that can be used on its own or navigated to within a Frame.
/// </summary>
public sealed partial class HomePage : Page
{

    public HomePageModel Model = new HomePageModel();
    public ObservableCollection<string> PunchRecords { get; } = new();

    private CancellationTokenSource? _cts;
    private PeriodicTimer? _timer;
    private bool _isRunning = false;
    
    
    public HomePage()
    {
        InitializeComponent();
        
        SignIn();
    }

    private async void ClickIn(object sender, RoutedEventArgs e)
    {
        if (sender is Button btn)
        {
            string[] readAllLines = await File.ReadAllLinesAsync("StaticResource/HomePage/签到语句.txt");
            if (!btn.Content.Equals("已打卡"))
            {
                Random r=new Random();

                var panel = new StackPanel
                {
                    Orientation = Orientation.Vertical,
                    MinHeight = 180,
                    Spacing = 20
                };
                panel.Children.Add(new Image
                {
                    Source = new BitmapImage(new Uri("ms-appx:///Assets/HomePageAssets/signin.gif")),
                    Width = 100,
                    Height = 100,
                });
                panel.Children.Add(new TextBlock
                {
                    Text = readAllLines[r.Next(readAllLines.Length)],
                    HorizontalAlignment = HorizontalAlignment.Center
                });
                CancelChangeSignState();
                var dialog = new ContentDialog  
                {
                    Title = "打卡成功！",
                    Content = panel,
                    PrimaryButtonText = "NB",
                    
                    XamlRoot = this.Content.XamlRoot
                };
                
                dialog.Resources["ContentDialogBackground"] = new SolidColorBrush(Color.FromArgb(255,57, 57, 57));
                dialog.Resources["ContentDialogTopOverlay"] = new SolidColorBrush(Color.FromArgb(255,57, 57, 57));
                
                btn.Content = "已打卡";

                ContentDialogResult result = await dialog.ShowAsync();
                ChangeSignState();
            }
            else
            {
                var dialog = new ContentDialog
                {
                    Title = "💡 Tip",
                    Content = "今日已成功打卡，请勿重复签到",
                    PrimaryButtonText = "我知道了",
            
                    XamlRoot = this.Content.XamlRoot
                };
                dialog.Resources["ContentDialogBackground"] = new SolidColorBrush(Color.FromArgb(255,136 ,137 ,141));
                dialog.Resources["ContentDialogTopOverlay"] = new SolidColorBrush(Color.FromArgb(255,136 ,137 ,141));
                await dialog.ShowAsync();
            }
        }
    }

    private async void ChangeSignState()
    {
        if (_isRunning)return;
        _isRunning = true;
        _cts = new CancellationTokenSource();
        _timer = new PeriodicTimer(TimeSpan.FromSeconds(10));
        try
        {
            while (await _timer.WaitForNextTickAsync(_cts.Token))
            {
                SignI.Text = "打卡";
            }
        }
        catch (Exception e)
        {
            Console.WriteLine(e);
        }
    }

    private void CancelChangeSignState()
    {
        if (!_isRunning)return;
        _cts?.Cancel();
        _timer?.Dispose();
        _isRunning = false;
        SignI.Text = "打卡";
    }

    private async void SignIn()
    {
        string[] lis = await File.ReadAllLinesAsync("StaticResource/HomePage/PunchRecords.txt");
        foreach (var v in lis)
        {
            Console.WriteLine(v);
            PunchRecords.Add(v);
        }
    }

    private void GetNowTime()
    {
        string time = DateTime.Now.ToString("HH:mm:ss");
    }
    
    protected override void OnNavigatedFrom(NavigationEventArgs e)
    {
        // _timer.Stop();
        base.OnNavigatedFrom(e);
    }
}
