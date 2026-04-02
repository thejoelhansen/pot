# pot
Programmable Operations Tool

# General Use

# TODO
- add dryrun flag
- add argument type
- move required runners, commands, files into config
- pot git search is broken

# Runners

Runners take a defined command "body" and execute it through a specific language, version, or with specific environment parameters. Additional runners can be created by copying the runners/shell.py file (EG as runners/go.py) and updating the logic that executes parsed_command

# Commands

Commands are ran by pot through a given runner. The command "body" is written in the language of the runner. Command's are written in a python dictionary as key: value pairs. 

## Name !Required
Command "name" is called after {app_name} to execute the command "body". It is case-sensitive. 

## Body !Required 
Define body of command, placing "{variable_name}" in double quotes

## Help Text !Required
Help text for main app --help as well as missing/ misspelled argument or subcommand

## Runner ! Required
Specify the runner through which the command should be executed through - usually coincides with a language (bash shell or python) or a specific version (python2 or python3)

## Usage
Second line of help text to provide a usage example of the command. Wrap in {'Usage:':<18} to get a nice, right-align

## Arguments 
Define variables as {variable_name} for use in "body"

# Module precedence

Runner and Command modules are loaded at run time and used in preferential order: local .pot/ > $HOME/.pot > /usr/local/lib/pot/
- 1 In your local application folder you can create a .pot/command or ./pot/runner folder, in which modules unique to that application or overrides to the default will be dynamically loaded at run time
- 2 In your user folder you can create a $HOME/.pot/command or $HOME/.pot/runner folder, in which modules customized for the present user will override their global defaults
- 3 In /usr/local/lib/pot live the global modules, accessible to all users. If there is no ./.pot/ or $HOME/.pot folders containing modules the global modules will be loaded

# Installation

To install globally run: 

```
sudo python3 install.py
```

To install locally for the current user: 
```
python3 install.py
```

Note: The dedault app name is 'pot'. If you'd like to change this you'll need to update two things:
- config.ini > app_name = "new-app-name"
- mv pot.py new-app-name

# Updating

Pot gathers all modules from all locations afresh each time it runs, so just run pot <app> to test changes to customized commands or runners.
