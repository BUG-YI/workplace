```xaml
<ListView 
                ItemsSource="{Binding Lis}"
                ScrollViewer.HorizontalScrollBarVisibility="Disabled"
                Grid.Row="1">
                
                <ListView.ItemsPanel>
                    <ItemsPanelTemplate>
                        <WrapPanel Orientation="Horizontal" HorizontalAlignment="Center"></WrapPanel>
                    </ItemsPanelTemplate>
                </ListView.ItemsPanel>
                
                <ListView.ItemContainerStyle>
                    <Style TargetType="ListViewItem">
                        <Setter Property="Height" Value="220"></Setter>
                        <Setter Property="Width" Value="200"></Setter>
                        
                        <Setter Property="Template">
                            <Setter.Value>
                                <ControlTemplate TargetType="ListViewItem">
                                    <Border
                                        Margin="15,10"
                                        BorderBrush="Black"
                                        CornerRadius="8"
                                        BorderThickness="1">
                                        <ContentPresenter></ContentPresenter>
                                    </Border>
                                </ControlTemplate>
                            </Setter.Value>
                        </Setter>
                    </Style>    
                </ListView.ItemContainerStyle>
                
                <ListView.ItemTemplate>
                    <DataTemplate>
                        <Border Tag="">
                            <Grid ShowGridLines="True">
                                <Grid.RowDefinitions>
                                    <RowDefinition></RowDefinition>
                                    <RowDefinition Height="Auto"></RowDefinition>
                                    <RowDefinition Height="Auto"></RowDefinition>
                                </Grid.RowDefinitions>
                                <Border>
                                    <Image
                                        Width="70"
                                        Source="/Assets/Image/hzm_white.png"
                                        VerticalAlignment="Center"
                                        ></Image>
                                </Border>
                                <Button 
                                    Grid.Row="0"
                                    Content="···"
                                    FontSize="20"
                                    Width="30"
                                    Height="20"
                                    Padding="0"
                                    BorderThickness="0"
                                    VerticalAlignment="Top"
                                    HorizontalAlignment="Right">
                                    <Button.Style>
                                        <Style TargetType="Button" BasedOn="{StaticResource {x:Type Button}}">
                                            <Style.Triggers>
                                                <Trigger Property="IsMouseOver" Value="True">
                                                    <Setter Property="BorderBrush" Value="Transparent"></Setter>
                                                    <Setter Property="Foreground" Value="Red"></Setter>
                                                </Trigger>
                                            </Style.Triggers>
                                        </Style>
                                    </Button.Style>
                                </Button>
                                <TextBlock
                                    Grid.Row="1"
                                    Text="{Binding}"
                                    FontSize="20"
                                    FontWeight="Bold"
                                    VerticalAlignment="Center"
                                    HorizontalAlignment="Center"></TextBlock>
                                <Button 
                                    Margin="0,10"
                                    Foreground="Black"
                                    Grid.Row="2"
                                    Content="启动"
                                    FontWeight="Bold"
                                    Click="StartApp"></Button>
                            </Grid>
                        </Border>
                    </DataTemplate>
                </ListView.ItemTemplate>
            </ListView>
```



```xaml
            <ItemsControl
                ItemsSource="{Binding Lis}"
                HorizontalAlignment="Center"
                Grid.Row="1">
                <ItemsControl.ItemsPanel>
                    <ItemsPanelTemplate>
                        <WrapPanel Orientation="Horizontal" />
                    </ItemsPanelTemplate>
                </ItemsControl.ItemsPanel>
            
                <ItemsControl.ItemTemplate>
                    <DataTemplate>
                        <Border Tag="{Binding}"
                                Width="180"
                                Height="220"
                                BorderBrush="Black"
                                BorderThickness="1"
                                Margin="10"
                                CornerRadius="8">
                            <Grid ShowGridLines="True">
                                <Grid.RowDefinitions>
                                    <RowDefinition></RowDefinition>
                                    <RowDefinition Height="Auto"></RowDefinition>
                                    <RowDefinition Height="Auto"></RowDefinition>
                                </Grid.RowDefinitions>
                                <Border>
                                    <Image
                                        Width="70"
                                        Source="/Assets/Image/hzm_white.png"
                                        VerticalAlignment="Center"
                                        ></Image>
                                </Border>
                                <Button
                                    Grid.Row="0"
                                    Content="···"
                                    FontSize="20"
                                    Width="30"
                                    Height="20"
                                    Padding="0"
                                    Click="ThreePinter"
                                    Command="{Binding DataContext.ChangeWindowCommand,ElementName=HomeP}"
                                    CommandParameter="{Binding}"
                                    BorderThickness="0"
                                    VerticalAlignment="Top"
                                    HorizontalAlignment="Right">
                                    <Button.Style>
                                        <Style TargetType="Button" BasedOn="{StaticResource {x:Type Button}}">
                                            <Style.Triggers>
                                                <Trigger Property="IsMouseOver" Value="True">
                                                    <Setter Property="BorderBrush" Value="Transparent"></Setter>
                                                    <Setter Property="Foreground" Value="Red"></Setter>
                                                </Trigger>
                                            </Style.Triggers>
                                        </Style>
                                    </Button.Style>
                                </Button>
                                <TextBlock
                                    Grid.Row="1"
                                    Text="{Binding}"
                                    FontSize="20"
                                    FontWeight="Bold"
                                    VerticalAlignment="Center"
                                    HorizontalAlignment="Center"></TextBlock>
                                <Button
                                    Margin="0,10"
                                    Foreground="Black"
                                    Grid.Row="2"
                                    Content="启动"
                                    FontWeight="Bold"
                                    Click="StartApp"></Button>
                            </Grid>
                        </Border>
                    </DataTemplate>
                </ItemsControl.ItemTemplate>
            </ItemsControl>
```


### image
#f0dc00 star