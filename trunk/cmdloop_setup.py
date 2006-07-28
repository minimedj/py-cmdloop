#!/usr/bin/env python

from distutils.core import setup

setup(name='CmdLoop',
      version='0.1.2',
      description='Command Loop Implementation Environment',
      long_description= \
"""Base class for writing simple interactive command loop environments.

CommandLoop provides a base class for writing simple interactive user
environments.  It is designed around sub-classing, has a simple command
parser, and is trivial to initialize.

Here is a trivial little environment written using CommandLoop:

    import cmdloop

    class Hello(cmdloop.CommandLoop):
        PS1='hello>'

        @cmdloop.aliases('hello', 'hi', 'hola')
        @cmdloop.shorthelp('say hello')
        @cmdloop.usage('hello TARGET')
        def helloCmd(self, flags, args):
            '''
            Say hello to TARGET, which defaults to 'world'
            '''
            if flags or len(args) > 1:
                raise InvalidArguments
            if args:
                target = args[0]
            else:
                target = self.default_target
            print >> self.OUT, 'Hello %s!' % target

        @cmdloop.aliases('quit')
        def quitCmd(self, flags, args):
            '''
            Quit the environment.
            '''
            raise cmdloop.HaltLoop

    Hello().runLoop()

Here's a more complex example:

    import cmdloop

    class HelloGoodbye(cmdloop.CommandLoop):
        PS1='hello>'

        def __init__(self, default_target = 'world'):
            self.default_target = default_target
            self.target_list = []

        @cmdloop.aliases('hello', 'hi', 'hola')
        @cmdloop.shorthelp('say hello')
        @cmdloop.usage('hello [TARGET]')
        def helloCmd(self, flags, args):
            '''
            Say hello to TARGET, which defaults to 'world'
            '''
            if flags or len(args) > 1:
                raise cmdloop.InvalidArguments
            if args:
                target = args[0]
            else:
                target = self.default_target
            if target not in self.target_list:
                self.target_list.append(target)
            print >> self.OUT, 'Hello %s!' % target

        @cmdloop.aliases('goodbye')
        @cmdloop.shorthelp('say goodbye')
        @cmdloop.usage('goodbye TARGET')
        def goodbyeCmd(self, flags, args):
            '''
            Say goodbye to TARGET.
            '''
            if flags or len(args) != 1:
                raise cmdloop.InvalidArguments
            target = args[0]
            if target in self.target_list:
                print >> self.OUT, 'Goodbye %s!' % target
                self.target_list.remove(target)
            else:
                print >> self.OUT, "I haven't said hello to %s." % target

        @cmdloop.aliases('quit')
        def quitCmd(self, flags, args):
            '''
            Quit the environment.
            '''
            raise cmdloop.HaltLoop

        def _onLoopExit(self):
            if len(self.target_list):
                self.pushCommands(('quit',))
                for target in self.target_list:
                    self.pushCommands(('goodbye', target))
            else:
                raise cmdloop.HaltLoop

    HelloGoodbye().runLoop()
""",
      author='Crutcher Dunnavant',
      author_email='crutcher@gmail.com',
      url='http://code.google.com/p/py-cmdloop/',
      download_url='http://py-cmdloop.googlecode.com/svn/trunk/cmdloop.py',
      packages=['cmdloop'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: Python Software Foundation License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: User Interfaces',
          ],

     )


