namespace HZMAPP.Models;

public class ApplicationsM
{
    public required string Name { get; set; }
    public string? Information { get; set; }
    public string? ImageAddr { get; set; }
    public Dictionary<string,object>? Star { get; set; }
}