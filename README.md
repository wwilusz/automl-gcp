# (Part of) Python Client for Cloud AutoML API adjusted to taste

This branch preserves canonical structure of the upstream repo: [link](https://github.com/googleapis/python-automl),
limited to `samples/tables`. Created as described 
[here](https://stackoverflow.com/questions/24577084/forking-a-sub-directory-of-a-repository-on-github-and-making-it-part-of-my-own-r)
and [here](https://web.archive.org/web/20131123125622/http://blog.charlescy.com/blog/2013/08/17/git-subtree-tutorial/).

### Receiving upstream commits
New commits from the upstream repo can be retrieved in three stages:

I. Update `upstream-master` to the current version of the the 
[python-automl](https://github.com/googleapis/python-automl) repo:
```bash
git checkout upstream-master
git pull
```

II. While still on the `upstream-master` branch (`git subtree` ensures that commit hashes 
are the same):
```bash
git subtree split --prefix=samples/tables --onto upstream-tables -b upstream-tables
```

III. Having `upstream-tables` up to date, allows updating the `master` branch by merging or rebasing
changes, for example:
```bash
git checkout master
git rebase upstream-tables
```