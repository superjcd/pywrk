# Pywrk

A very small http/https benchmark tool written in python.



## Usage 

You can  download it from pypi:

```shell
pip install pywrk
```

A minium example looks like bewlow: 

```shell
pywrk -n 100 -c 2 https://www.python.org
```

Note flag `n` means total number of request times, and flag `c` means connections at same time(You can think it as how many threads being used simotaniously, though behind the scene pywrk uses a  coroutine other than  threads , but looks simmilar functionally).



## All possible flags

You can check all posiible flags by running :

```
pywrk --help
```

The description for all flags are as following :

```
-n         Total query times
-c         Connetions at same time
-H         Reqeust Headers
-m         Request Method, default 'GET'
-d         Request body 
-p         Request Params
--cookies  Cookies
--user     user for Basic Authentication
--password password for Basic Authentication
```

A little bit sophisticated example looks like:

```
pywrk -n 100 -c 10 -m GET -H '{"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36"}' https://www.python.org
```

Note don't forget the quote mark when using the flags likes `H`, `p` and `d`, otherwise they can not be interpreted properly.

## Outputs

The output  of  pywrk looks like below:  

```
2021-05-02 20:38:07| Elapsed: 0h:0m:2s| Processed: 100| Consumed: 100| Remained: 0| Processing Speed: 33.43| Efficiency: 1.0| Eta: 0h:0m:0s|
😊 Completed! Spydy ran successfully without any excepitons
```

Cuz `pywrk` is written with `spydy`(A lite-weight web-scraping framework), so it share the similar output with `spydy`, and which i think giving good enough statistics about the web performance.  

The meaning of the output above are:

```
Elapsed     Time elapsed
Processed   Processed Times
Consumed    Time of successfull calling, cuz some of them may be failed
Remained    How many request ramained to be calling
Processing Speed    Processing times per second
Efficiency  The ratio of successfull request during whole process
Eta         Expected time to finish whole process
```

If any exceptions occurs during the process, the exceptions and the number of  that kind of  exception happened will be reported as well.
