# CHANGELOG - network

## 1.9.0 / 2019-02-18

* [Added] Add conntrack basic metrics to the network integration.. See [#2981](https://github.com/DataDog/integrations-core/pull/2981). Thanks [aerostitch](https://github.com/aerostitch).
* [Fixed] Resolve flake8 issues. See [#3060](https://github.com/DataDog/integrations-core/pull/3060).
* [Added] Upgrade psutil. See [#3019](https://github.com/DataDog/integrations-core/pull/3019).
* [Added] Support Python 3. See [#3005](https://github.com/DataDog/integrations-core/pull/3005).
* [Fixed] Use `device` tag instead of the deprecated `device_name` parameter. See [#2945](https://github.com/DataDog/integrations-core/pull/2945). Thanks [aerostitch](https://github.com/aerostitch).

## 1.8.0 / 2018-11-30

* [Added] Update psutil. See [#2576][1].
* [Fixed] Use raw string literals when \ is present. See [#2465][2].

## 1.7.0 / 2018-10-12

* [Added] Upgrade psutil. See [#2190][3].

## 1.6.1 / 2018-09-04

* [Fixed] Retrieve no_proxy directly from the Datadog Agent's configuration. See [#2004][4].
* [Fixed] Add data files to the wheel package. See [#1727][5].

## 1.6.0 / 2018-06-07

* [Added] Add monotonic counts for some metrics. See [#1551][6]. Thanks [jalaziz][7].

## 1.5.0 / 2018-03-23

* [FEATURE] Add custom tag support.

## 1.4.0 / 2018-02-13

* [FEATURE] Get some host network stats when the agent is running inside a container and not in the host network namespace. See [#994][8]

## 1.3.0 / 2017-09-01

* [FEATURE] Collects TCPRetransFail metric from /proc/net/netstat, See [#697][9]

## 1.2.2 / 2017-08-28

* [BUGFIX] Fix incorrect `log.error` call in BSD check. See [#698][10]

## 1.2.1 / 2017-07-18

* [BUGFIX] Fix TCP6 metrics overriding TCP4 metrics when monitoring non combines socket states. See [#501][11]

## 1.2.0 / 2017-06-05

* [FEATURE] Adds metrics from `/proc/net/netstat` in addition to the existing ones from `/proc/net/snmp`. See [#299][12] and [#452][13], thanks [@cory-stripe][14]

## 1.1.0 / 2017-05-03

* [BUGFIX] Work around `ss -atun` bug not differentiating tcp and udp. See [#296][15]

## 1.0.0 / 2017-03-22

* [FEATURE] adds network integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2576
[2]: https://github.com/DataDog/integrations-core/pull/2465
[3]: https://github.com/DataDog/integrations-core/pull/2190
[4]: https://github.com/DataDog/integrations-core/pull/2004
[5]: https://github.com/DataDog/integrations-core/pull/1727
[6]: https://github.com/DataDog/integrations-core/pull/1551
[7]: https://github.com/jalaziz
[8]: 
[9]: 
[10]: https://github.com/DataDog/integrations-core/issues/698
[11]: https://github.com/DataDog/integrations-core/issues/501
[12]: https://github.com/DataDog/integrations-core/issues/299
[13]: https://github.com/DataDog/integrations-core/issues/452
[14]: https://github.com/cory-stripe
[15]: https://github.com/DataDog/integrations-core/issues/296