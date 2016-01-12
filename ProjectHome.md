CommandLoop provides a base class for writing simple interactive user
environments.  It is designed around sub-classing, has a simple command
parser, and is trivial to initialize.

Here is a trivial little environment written using CommandLoop:

> import cmdloop

> class Hello(cmdloop.CommandLoop):
> > PS1='hello>'


> @cmdloop.aliases('hello', 'hi', 'hola')
> @cmdloop.shorthelp('say hello')
> @cmdloop.usage('hello TARGET')
> def helloCmd(self, flags, args):
> > '''
> > Say hello to TARGET, which defaults to 'world'
> > '''
> > if flags or len(args) > 1:
> > > raise InvalidArguments

> > if args:
> > > target = args[0](0.md)

> > else:
> > > target = self.default\_target

> > print >> self.OUT, 'Hello %s!' % target


> @cmdloop.aliases('quit')
> def quitCmd(self, flags, args):
> > '''
> > Quit the environment.
> > '''
> > raise cmdloop.HaltLoop


> Hello().runLoop()

Here's a more complex example:

> import cmdloop

> class HelloGoodbye(cmdloop.CommandLoop):
> > PS1='hello>'


> def init(self, default\_target = 'world'):
> > self.default\_target = default\_target
> > self.target\_list = [.md](.md)


> @cmdloop.aliases('hello', 'hi', 'hola')
> @cmdloop.shorthelp('say hello')
> @cmdloop.usage('hello [TARGET](TARGET.md)')
> def helloCmd(self, flags, args):
> > '''
> > Say hello to TARGET, which defaults to 'world'
> > '''
> > if flags or len(args) > 1:
> > > raise cmdloop.InvalidArguments

> > if args:
> > > target = args[0](0.md)

> > else:
> > > target = self.default\_target

> > if target not in self.target\_list:
> > > self.target\_list.append(target)

> > print >> self.OUT, 'Hello %s!' % target


> @cmdloop.aliases('goodbye')
> @cmdloop.shorthelp('say goodbye')
> @cmdloop.usage('goodbye TARGET')
> def goodbyeCmd(self, flags, args):
> > '''
> > Say goodbye to TARGET.
> > '''
> > if flags or len(args) != 1:
> > > raise cmdloop.InvalidArguments

> > target = args[0](0.md)
> > if target in self.target\_list:
> > > print >> self.OUT, 'Goodbye %s!' % target
> > > self.target\_list.remove(target)

> > else:
> > > print >> self.OUT, 'I haven't said hello to %s.' % target


> @cmdloop.aliases('quit')
> def quitCmd(self, flags, args):
> > '''
> > Quit the environment.
> > '''
> > raise cmdloop.HaltLoop


> def _onLoopExit(self):
> > if len(self.target\_list):
> > > self.pushCommands(('quit',))
> > > for target in self.target\_list:
> > > > self.pushCommands(('goodbye', target))

> > else:
> > > raise cmdloop.HaltLoop_


> HelloGoodbye().runLoop()
