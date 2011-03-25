============
Djumpstart
============

Djumpstart installs a script which allows the easy creation of a standard
Django project and apps layout, based on Lincoln Loop start_project .


Script usage
============

After installing Djumpstart, simply run the following command (from within
the directory in where the new project directory should be created) to create
a new project using the default project layout::

	djumpstart.py project [project_name]

or the folling command to create a new app using the default app layout::

    djumpstart.py app [app_name]


The script will prompt for values to replace boilerplate variables with. These
variables allow for both the file contents and path names to be customized to
this specific project.


Using a custom project or app template
======================================

If you would prefer to use a custom template than the one included in
this application, create your custom template and call the
command script like this::


    djumpstart.py --template=/your/custom/template project_or_app_name


You can also keep several custom templates in a folder, and have djumpstart
use that folder as the template repository.

Djumpstart by default looks for a directory $HOME/.djumpstart/templates
You can override the default template directory by setting the 
environment variable DJUMPSTART_HOME.

You can do this by adding the following line to your .bashrc file:

    export DJUMPSTART_HOME=$HOME/.djumpstart

*Note: Djumpstart looks for directory called templates under DJUMPSTART_HOME.
Djumpstart will also look for a file called .defaults.py for default boilerplate 
variables.


Specifying boilerplate variables
--------------------------------

Two optional files in the root of the project template directory are used to
determine the boilerplate variables:

``.startproject_boilerplate``
	Each line should contain the boilerplate variable (and optionally, a
	description of the variable, separated from the variable by white space).

``.startproject_defaults``
	Each line should contain a variable and the default value, separated by
	whitespace. If the default value contains ``PROJECT``, it is replaced with
	the project name.

See the files included in the templates directory of Djumpstart for
an example.
