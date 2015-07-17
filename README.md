# GitHub-Processor-Spain

## What is this?
Only one script to process some data from [JJ, GitHub Users Data](https://github.com/JJ/top-github-users-data).

## What does the script?

Now, the script calcules:

* Total contributions in each province
* Contributions between data updated in each pronvice
* Total contributions/population in each province
* Languages used by developers in each province

## Where are the data?

In another repo, [here](https://github.com/iblancasa/GitHub-DataProcessed-Spain)

## What have I to do to run the script?
You will need install some things:
* Python
* PyOpenSSL
* ndg-httpsclient
* pyasn1
* Pip

If you are in Debian/Ubuntu:

```bash
sudo apt-get install python-pip python-dev build-essential
sudo easy_install pip
sudo pip install pyopenssl ndg-httpsclient pyasn1
```

Then, you can run in terminal with ``python start.py``

## License

It is free software :D License is GPLv3s
