from django_djumpstart import utils
import optparse
import os
import sys

import string


# Look for templates in ENV variable, default .djumpstart in $HOME, or project
# default DIR

ENV_DJUMPSTART_DIR = os.path.join(os.getenv('DJUMPSTART_HOME'),'templates')
USER_HOME_DIR      = os.path.join(os.path.expanduser('~'),'.djumpstart/templates')
DEFAULT_DIR        = os.path.join(os.path.dirname(os.path.realpath(utils.__file__)),
                                  'templates')

# Select TEMPLATE_DIR in the right order
# #TODO#: error handling in case DIR exists but not templates, etc... 

if os.path.isdir(ENV_DJUMPSTART_DIR):
    TEMPLATE_DIR = ENV_DJUMPSTART_DIR
elif os.path.isdir(USER_HOME_DIR):
    TEMPLATE_DIR = USER_HOME_DIR
else:
    TEMPLATE_DIR = DEFAULT_DIR


TEMPLATE_LIST = os.listdir(TEMPLATE_DIR)


def start_project():
    """
    Copy a project template, replacing boilerplate variables.
    usage: 
    
    scaffolding using a specific project or app template:
    djumpstart template_name project_or_app_name [base_destination_dir]
           
    list available templates:
    djumpstart -l

    use a specific directory as template:
    djumpstart -t /path/to/template project_or_app_name
 
    """
    usage = "usage: %prog [options] (template_name) project_or_app_name [base_destination_dir]"
    parser = optparse.OptionParser(usage=usage)
    
    parser.add_option('-l', '--list', action="store_true", dest="list_templates", 
                      help='list available templates')


    parser.add_option('-t', '--template', dest='src_dir',
                      help='path to project or app template to use',
                      )

    parser.add_option('-p', '--prompt', action="store_true", dest='prompt',
                      help='Prompt for boilerplate variables',
    )

    options, args = parser.parse_args()
    
    if options.list_templates:
        # TODO: get template descriptions from .djumpstart
        for i in TEMPLATE_LIST:
            print i
        sys.exit(1)

    if len(args) not in (1,2,3):
        parser.print_help()
        sys.exit(1)

    if options.src_dir:
        if len(args) not in (1,2):
            parser.print_help()
            sys.exit(1)

        if os.isdir(options.src_dir):
            template = options.src_dir
            project_or_app_name = args[0]
            try:
                target_dir = args[1]
            except:
                target_dir = (base_dest_dir,project_or_app_name)

    if not options.src_dir:
        if len(args) not in (2,3):
            parser.print_help()
            sys.exit(1)

        template_name = args[0]
        project_or_app_name = args[1]
        try:
            target_dir = args[2]
        except:
            target_dir = os.path.join('',project_or_app_name)

        if template_name in TEMPLATE_LIST:
            template_path = os.path.join(TEMPLATE_DIR,template_name)
            
        else:
            print "Template not found. Available templates:"
            for i in TEMPLATE_LIST:
                print i
                sys.exit(1)


    # Get any boilerplate replacement variables:
    replace = {}

    if options.prompt:
        for key,values in utils.get_template_vars(template_path).items():
            if values is None:
                prompt = '%s: ' % key
                default = None
            elif type(values) is type(()):
                default, help = values
                prompt = '%s [%s]: ' % (help, default)
            else:
                default = values
                prompt = '%s [%s]: ' % (key, default)
            

#       while not value:
            value = raw_input(prompt) or default
            replace[key] = value#
    
    utils.copy_template(template_path, target_dir, replace)    
