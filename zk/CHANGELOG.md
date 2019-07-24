# CHANGELOG - zk

## 2.1.0 / 2019-01-04

* [Added] Support Python 3. See [#2781][1].

## 2.0.0 / 2018-11-30

* [Removed] Removed incorrect metric name 'bytes_outstanding'. See [#2476][2].

## 1.2.1 / 2018-09-04

* [Fixed] Add data files to the wheel package. See [#1727][3].

## 1.2.0 / 2018-01-10

* [IMPROVEMENT] Add `zookeeper.packets.received` and `zookeeper.packets.sent` as `rate` metrics
  for the `stat` command output to correct the incorrect `zookeeper.bytes_received` and
  `zookeeper.bytes_sent` metrics. See [#816][4]

## 1.1.0 / 2017-07-18

* [IMPROVEMENT] Replace usage of deprecated `AgentCheck.set` method with `gauge`. See [#473][5]

## 1.0.1 / 2017-04-24

* [BUGFIX] Fix version parsing causing false positives with `3.4.10`. See [#341][6]

## 1.0.0 / 2017-03-22

* [FEATURE] adds zk integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2781
[2]: https://github.com/DataDog/integrations-core/pull/2476
[3]: https://github.com/DataDog/integrations-core/pull/1727
[4]: https://github.com/DataDog/integrations-core/pull/816
[5]: https://github.com/DataDog/integrations-core/issues/473
[6]: https://github.com/DataDog/integrations-core/issues/341