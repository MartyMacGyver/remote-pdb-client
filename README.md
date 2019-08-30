# RemotePDB Client

## A client for debugging code instrumented with the RemotePDB package

The [RemotePDB package](https://pypi.org/project/remote-pdb/) is a useful way to remotely debug code (i.e., code running in Docker). Normally, a user can simply wait for the `set_trace()` command to be executed, then telnet to the appropriate port. However, in applications such as Django, this necessitates manually disconnecting the telnet session before another breakpoint can be processed.

With RemotePDB Client, the user can instantiate the client at any time, and it will pend until a debug connection becomes available. Likewise, after a PDB `c(ontinue)` command the client will disconnect internally and await the next available connection.

You can use `h(elp)` within the debugger to see the usual remote commands. `q(uit)`/`e(xit)` will forward the given command and then exit the Client completely.

A persistent history is available and is saved for re-use between client sessions.

The `cl(ear)` breakpoints command is disallowed if it has no arguments (clearing all breakpoints causes the remote process to pend on y/n input).

If you are debugging code in a Docker container, remember to expose the internal port externally via your `docker-compose` command or file (keeping in mind that the internal and external port numbers should be different).

There is a limit to what you can debug with this - if you call `set_trace()` within code running in multiple threads/processes at the same time, only one will be connected to and the rest will pend or fail.

To avoid problems with `BdbQuit` being raised by RemotePDB 2.0+ on remote disconnect, before exiting via Ctrl-C, `e`xit, or `q`uit we purposely send a "`c`ontinue" command.

## Disclaimer

DO NOT use RemotePDB Client to connect to untrusted hosts!
