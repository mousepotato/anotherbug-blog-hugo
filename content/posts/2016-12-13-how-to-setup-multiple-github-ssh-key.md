---
title: how to setup multiple github ssh keys
date: 2016-12-13 15:25:43
categories:
- Technique
tags:
- Git
---


## 1. create multiple ssh key

    ssh-keygen -t rsa -C "your_email@youremail.com"

for example, 2 keys create at:

```
~/.ssh/id_rsa
~/.ssh/id_rsa_sli_racingwithhorse
```

## 2. then, add these two keys as following
```
ssh-add ~/.ssh/id_rsa
ssh-add ~/.ssh/id_rsa_sli_racingwithhorse
```

check your saved keys using:

    ssh-add -l


## 3. modify the ssh config

```
cd ~/.ssh/
touch config

$==> cat config
#gmail.com account
Host github.com
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa

#racingwithhorse account
Host github.com-racingwithhorse
    HostName github.com
    User git
    IdentityFile ~/.ssh/id_rsa_sli_racingwithhorse
```


## 4. clone you repo and modify your git config

```
git config user.name "racingwithhorse"
git config user.email "xxx@xxx.xxx"

```

then inside the cloned git repository

```
cat .git/config
[remote "origin"]
	url = git@github.com-racingwithhorse:racingwithhorse/racingwithhorse.github.io.git
	fetch = +refs/heads/*:refs/remotes/origin/*
```

That's it!


