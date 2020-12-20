## Use iperf To Test Performance

We first run `iperf` in server mode on a host designated as server, `u3` for example

```shell
u3 iperf -s &
```

Then we run `iperf` in client mode on a host designated as client, `u1` for example

```shell
u1 iperf -c u3 -d > u1.perf &
```

Option `-d` means it's bidirectional.



Besides, we can specify 

-   stream type: TCP/UDP

-   port

-   bandwidth

-   parallel client threads

-   given file to be transmitted

-   ...

    