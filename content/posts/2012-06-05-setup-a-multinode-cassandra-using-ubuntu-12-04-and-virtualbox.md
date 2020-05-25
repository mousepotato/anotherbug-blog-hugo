---
layout: post
title: "Setup a multinode Cassandra using Ubuntu 12.04 and Virtualbox"
description: "本文介绍如何使用Virtualbox搭建具有多个节点的hadoop实例。" 
categories: 
- technique
tags:
- cloud-computing
- hadoop
- ubuntu
- virtualbox
---


Setup a multinode Cassandra using Ubuntu 12.04 and Virtualbox

### 1. Setup virtual machines (3 for exmaple)

- You should first setup one machine using virtualbox, <a href="http://anotherbug.com/blog/2011/10/ubuntu-11-04_install_java/">setup JAVA environment</a>, download the <a href="http://www.apache.org/dyn/closer.cgi?path=/cassandra/1.1.1/apache-cassandra-1.1.1-bin.tar.gz">Cassandra source code</a> 

- Use Virtualbox's virtualmanager function to <a href="http://anotherbug.com/blog/2012/05/virtualbox-%E4%BF%AE%E6%94%B9uuid%E5%AE%9E%E7%8E%B0%E7%A1%AC%E7%9B%98%E5%A4%8D%E5%88%B6/">copy another two ubuntu machines</a>. Make sure to <a href="http://anotherbug.com/blog/2012/04/%E5%A6%82%E4%BD%95%E4%BF%AE%E6%94%B9ubuntu%E7%9A%84hostname/">modify the hostname</a>.
 
- Modify the	`/etc/hosts` file. 
- Machine summary      
	- 192.168.56.101 sjhadoop0
	- 192.168.56.103 sjhadoop1
   - 192.168.56.104 sjhadoop2
   
### 2. Config Cassandra
- Modify `/conf/cassandra-env.sh`file.

		MAX_HEAP_SIZE=&quot;512M&quot;
		HEAP_NEWSIZE=&quot;128M&quot;

- Modify `/conf/cassandra.yaml` file. For each virtual machine, change `listen_address` and `rpc_address`accordingly.

		listen_address: 192.168.1.1
		rpc_address: 192.168.1.1

- Choose one first machine as seed. Then change `seeds` to its ip address, make the rest VM pointing to the same seed.

		seeds: - 192.168.1.1

- Assign initial_token, using the <a href="http://anotherbug.com/blog/nodeToken.py">this python code</a> to generate initial token and modify the `initial_token` in .yaml file.

### 3. Start Cassandra

		sudo ./bin/cassandra -f

That's it!!
