import os
import re
import socket
import subprocess

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, hook
from libqtile import extension
from typing import List  # noqa: F401

from libqtile.utils import guess_terminal
terminal = guess_terminal()

mod = "mod4" ### The Modkey.

wmname = "Qtile" ### Naming my Window Manager.

nord0 = "#2E3440" ## Polar night
nord1 = "#3B4252" ## Brighter polar night
nord2 = "#434C5E" ## Even brighter polar night
nord3 = "#4C566A" ## Brightest polar night
nord4 = "#D8DEE9" ## Snow storm
nord5 = "#E5E9F0" ## Brighter snowstorm
nord6 = "#ECEFF4" ## Brightest snowstorm
nord7 = "#8FBCBB" ## Frost teal
nord8 = "#88C0D0" ## Frost Cyan
nord9 = "#81A1C1" ## Frost light blue
nord10 = "#5E81AC" ## Frost deep blue
nord11 = "#BF616A" ## Aurora red
nord12 = "#D08770" ## Aurora orange
nord13 = "#EBCB8B" ## Aurora yellow
nord14 = "#A3BE8C" ## Aurora green
nord15 = "#B48EAD" ## Aurora puprle

keys = [

    # Switch between windows in current stack pane
    Key([mod], "k", 
        lazy.layout.down()),

    Key([mod], "j", 
        lazy.layout.up()),

    # Increase/Decrease Master Window Size
    Key([mod], "l", 
        lazy.layout.grow()),
        
    Key([mod], "h", 
        lazy.layout.shrink()),

    # Put the focused window to/from floating mode
    Key([mod], "t", 
        lazy.window.toggle_floating()),
    
    # Move windows up or down in current stack
    Key([mod, "shift"], "k", 
        lazy.layout.shuffle_down()),

    Key([mod, "shift"], "j", 
        lazy.layout.shuffle_up()),

    # Normalize layout in monadtall
    Key([mod], "n", lazy.layout.normalize()),

    # Maximize layout in monadtall
    Key([mod], "o", lazy.layout.maximize()),

    # Make the focused window Fullscreen.
    Key([mod], "f",
        lazy.window.toggle_fullscreen()),

    # Open a Terminal
    Key([mod], "Return",  
        lazy.spawn(terminal)),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout()),

    Key([mod], "q", 
        lazy.window.kill()),  

    Key([mod, "shift"], "r", 
        lazy.restart()),

    # Brightness keys
    Key([], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl s +2%")),

    Key([], "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl s 2%-")),
    
    # Sound
    Key([], "XF86AudioMute", 
        lazy.spawn("ponymix mute")),

    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("ponymix decrease 5"),
        lazy.spawn("ponymix unmute")),

    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("ponymix increase 5"),
        lazy.spawn("ponymix unmute")),

    # Lock The Screen 
    Key([mod, "control"], "3",
       lazy.spawn("gdm")),

    # Launch Pavucontrol
    Key([mod, "control"], "p",
        lazy.spawn("pavucontrol")),

    Key([mod], "d", 
        lazy.spawn("rofi -show run")),


    Key([mod], "Print", lazy.spawn('spectacle')),
]

group_names = [("1", {'layout': 'monadtall'}),
               ("2", {'layout': 'monadtall'}),
               ("3", {'layout': 'monadtall'}),
               ("4", {'layout': 'monadtall'}),
               ("5", {'layout': 'monadtall'}),
               ("6", {'layout': 'monadtall'}),
               ("7", {'layout': 'monadtall'}),
               ("8", {'layout': 'monadtall'}),
               ("9", {'layout': 'monadtall'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names] 

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group.
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group.


### DEFAULT THEME SETTINGS FOR LAYOUTS ###
layout_theme = {"border_width": 0,
                "margin": 5,
                "border_focus" : nord4,
                "border_normal": nord0,
                }

### LAYOUTS ###
layouts = [

    layout.MonadTall(**layout_theme,
                     change_ratio = 0.07,
                     ),
    layout.MonadWide(**layout_theme,
                     change_ratio = 0.07,
                     ),
                       
    ]
widget_defaults = dict(
    font='terminus',
    fontsize=13,
    padding=5,
    background="#2E3440",
    margin = 5,
)
extension_defaults = widget_defaults.copy()

def open_nmtui(qtile):
    qtile.cmd_spawn('alacritty -e nmtui')

def open_pavucontrol(qtile):
    qtile.cmd_spawn('pavucontrol')

def open_gotop(qtile):
    qtile.cmd_spawn('alacritty -e gotop')
    
screens = [
    Screen(
        top=bar.Bar(
            [
            widget.GroupBox(
                    fontsize = 13,
                    borderwidth = 2,
                    active = nord9,
                    inactive = nord3,
                    rounded = True,
                    highlight_color = nord1,
                    highlight_method = "line",
                    foreground = nord9,
                    background = nord0,
                    padding = 3,
                    block_highlight_text_color = nord4,
                    other_current_screen_border = nord7,
                    other_screen_border = nord4,
                    this_current_screen_border = nord1,
                    urgent_border = nord11,
                    margin = 3,
                    disable_drag = False,
            ),

#            widget.DebugInfo(
#                    foreground = nord3
#            ),

            widget.WindowName(
                    foreground = nord10,
                    padding = 3,
                    show_state = True,
                    background = nord0,
                    fontsize = 12
            ),

            widget.TextBox(
                    text='',
                    fontsize = 30,
                    foreground = "#B48EAD",
                    padding = 5,
                    mouse_callbacks = {'Button1': open_nmtui},
            ),

            widget.Net(
                    format = '{down} ↓↑',
                    padding = 5,
                    foreground = "#D8DEE9",
                    update_interval = 5.0
            ),  

            widget.Sep(
            		foreground =  '#D8DEE9',
            		size_percent = 60,
            		padding = 10,
            ),

                 widget.TextBox(
                    text = '',
                    fontsize = 26,
                    foreground = "#8FBCBB",
                    padding = 5,
            ),

            widget.Battery(
                    format = "{percent:2.0%}",
                    padding = 4,
                    foreground = "#D8DEE9",
            ),

             widget.Sep(
                    foreground = "#D8DEE9",
                    size_percent = 60,
                    padding = 10,
            ),

             widget.TextBox(
                    text = '',
                    fontsize = 19,
                    foreground = nord11,
                    padding = 5,
            ),

            widget.ThermalSensor(
                   metric = True,
                   foreground_alert = nord4,
                   foreground = nord3,
                    
            ),

             widget.Sep(
                    foreground = "#D8DEE9",
                    size_percent = 60,
                    padding = 10,
            ),

            widget.TextBox(
                    text = '',
                    fontsize = 26,
                    foreground = "#EBCB8B",
                    padding = 5,
            ),
                 
            widget.Memory(
                    padding = 5,
                    foreground = "#D8DEE9",
                    update_interval = 5.0,
            ),

            widget.Sep(
                    foreground = "#D8DEE9",
                    size_percent = 60,
                    padding = 10,
            ),

            
            widget.TextBox(
                    text = '',
                    fontsize = 24,
                    foreground = "#88C0D0",
                    padding = 5,
                    mouse_callbacks = {'Button1': open_gotop},
            ),
                
            widget.CPU(
                    format='{freq_current}GHz',
                    foreground = "#D8DEE9",
                    padding = 5,
                    update_interval = 5.0,
            ),

            widget.Sep(
                    foreground = "#D8DEE9",
                    size_percent = 60,
                    padding = 10,
            ),

            widget.TextBox(
                    text = '',
                    fontsize = 26,
                    foreground = "#5E81AC",
                    padding = 5,
            ),
                 
            widget.Clock(format='%I:%M %p %a, %d',
                    padding = 5,
                    foreground = "#D8DEE9",
            ),

            widget.Sep(
                    foreground = "#D8DEE9",
                    size_percent = 60,
                    padding = 10,
            ),
                 
            widget.CurrentLayoutIcon(
                    scale = 0.7,
                    padding = 0,
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            ),

            widget.CurrentLayout(
                    padding = 5,
                    foreground = nord4,
            ),
                
                ],
            23,
         ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'Nitrogen'},
    {'wmclass': 'Pavucontrol'},
    {'wmclass': 'Gnome-screenshot'},
    {'wmclass': 'Gimp'},
    {'wmclass': 'Spotify'},
    {'wmclass': 'Gpick'},
    {'wmclass': 'Xarchiver'},
    
], border_width = 0, border_focus = nord4, border_normal = nord0)
auto_fullscreen = True
focus_on_window_activation = "urgent"

@hook.subscribe.startup_once
def autostart():
        home = os.path.expanduser('~/.config/qtile/autostart.sh')
        subprocess.call([home])
