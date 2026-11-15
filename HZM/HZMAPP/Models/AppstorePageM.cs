using System.Windows.Media;

namespace HZMAPP.Models;

public class AppstorePageM
{
    public string? Name { get; set; }
    public required string[] Version { get; set; }

    public Brush ItemColor { get; set; } = Brushes.White;
}