GIT
===

Git is a distributed version control system, created by Linus Thorvalds. It is the most used of it's kind and is the most essential part of every software project whether you are alone or with multiple people.

Commands
--------

Add
^^^

Stages a file. This needs to be done for every file you want to commit. The command for this is: git add filename. Alternatively you can use the pannel in vscode, by click + next to the file.

Commit
^^^^^^

Commits the file, the version of this file is then locally saved. To commit, your staged files, you have to give a clear message to the commit. For example fixed a bug in this file that cause this behaviour. The command is git commit. Again you can use vscode, to accomplish the same behaviour.

Pull
^^^^

You will most likely be working on a remote repository. To get the changes from this repository, use git pull. This gets all the changes and adds them locally. In vscode, you can find this under the commits, with the down arrow as symbol.

Push
^^^^

If you want to make changes and share them with the world, you use git push. This command puts all of your local commits on the remote repository. Similarly as with pull, push can be found under the commits tab, but with an up arrow.

Branch
^^^^^^

To make parallel working easier, branching is used. Branches can be for example when creating a new feature. To not disturb the main branch, you can create a new branch using, git branch branch-name. To see all the local branches, use git branch.

Checkout
^^^^^^^^

Checkout is the command that is used to see the changes in a different version. This can be a commit or a branch. When you have created a new branch, you can switch to it, by using git checkout branch-name.

Exercise
--------

Create and checkout a new branch in your repository. Edit the readme file, so that it contains your name and a fun fact about yourself. Stage and commit the changes. Lastly push them to the remote.