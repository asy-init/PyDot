# PyDot

`PyDot` is an intuitive terminal-based dotfile manager.

## Installation

```
git clone https://github.com/asy-init/PyDot
```

## Usage
<br>

##### ( will post to stable once i fix a few bugs)
<br>


```cpp

$ pydot list

$ pydot add <file/dir>

$ pydot rm <file/dir>

$ pydot status

$ pydot zip
```
```diff
# Examples

$ pydot list

alacritty
polybar
.ssh

$ pydot add ~/.config/alacritty

Scanning Templates...

Is ~/.config/alacritty config for alacritty on path /bin/alacritty? [Y/n]

>> y

+ ~/.config/alacritty added to PyDot tracker

$ pydot rm ~/.config/alacritty

proceed with removal of alacritty from tracker? [Y/n]

>> y

- ~/.config/alacritty has been removed from PyDot tracker


$ pydot status

 Tracking [2]
+ alacritty
+ polybar

 Removed recently [2]
- pacman.conf
- rc.conf

$ pydot zip

Zipping Files.......................................[ 100 % ]
Creating shell extractor............................[ 100 % ]
Cleaning up.........................................[ 100 % ]

enter path to present package [default: /home/foo/ ]

>> ~/Downloads

Removing duplicate package..........................[ 100 % ]

```

## Steps to install auto-install dotfiles:
<br>

 1. paste .dotfile_pkg in home folder [ eg : `/home/foo/` ]
<br>

 2. Run the following commands :
 ```shell
 $ user@host ~ > chmod u+x ./dotfile_pkg/install.sh

 $ user@host ~ > cd .dotfile_pkg

 $ ./install.sh
 ```
<br>
3.  Enter sudo details for package installations and other config options specified by user or package
<br>
<br>

```
[ Enter Sudo Password ] : *********
```

#
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
#
## License
- [MIT](https:github.com/asy-init/PyDot/blob/stable/LICENSE)