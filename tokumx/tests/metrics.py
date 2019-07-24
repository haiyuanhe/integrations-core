# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)


GAUGES = [
    'tokumx.connections.available',
    'tokumx.connections.current',
    'tokumx.cursors.timedOut',
    'tokumx.cursors.totalOpen',
    'tokumx.ft.alerts.checkpointFailures',
    'tokumx.ft.alerts.locktreeRequestsPending',
    'tokumx.ft.cachetable.size.current',
    'tokumx.ft.cachetable.size.limit',
    'tokumx.ft.cachetable.size.writing',
    'tokumx.ft.checkpoint.lastComplete.time',
    'tokumx.ft.compressionRatio.leaf',
    'tokumx.ft.compressionRatio.nonleaf',
    'tokumx.ft.compressionRatio.overall',
    'tokumx.ft.locktree.size.current',
    'tokumx.ft.locktree.size.limit',
    'tokumx.mem.resident',
    'tokumx.mem.virtual',
    'tokumx.metrics.repl.buffer.count',
    'tokumx.metrics.repl.buffer.sizeBytes',
    'tokumx.stats.dataSize',
    'tokumx.stats.indexSize',
    'tokumx.stats.indexes',
    'tokumx.stats.objects',
    'tokumx.stats.storageSize',
    'tokumx.uptime',
]


RATES = [
    'tokumx.asserts.msgps',
    'tokumx.asserts.regularps',
    'tokumx.asserts.rolloversps',
    'tokumx.asserts.userps',
    'tokumx.asserts.warningps',
    'tokumx.ft.alerts.longWaitEvents.cachePressure.countps',
    'tokumx.ft.alerts.longWaitEvents.cachePressure.timeps',
    'tokumx.ft.alerts.longWaitEvents.checkpointBegin.countps',
    'tokumx.ft.alerts.longWaitEvents.checkpointBegin.timeps',
    'tokumx.ft.alerts.longWaitEvents.fsync.countps',
    'tokumx.ft.alerts.longWaitEvents.fsync.timeps',
    'tokumx.ft.alerts.longWaitEvents.locktreeWait.countps',
    'tokumx.ft.alerts.longWaitEvents.locktreeWait.timeps',
    'tokumx.ft.alerts.longWaitEvents.locktreeWaitEscalation.countps',
    'tokumx.ft.alerts.longWaitEvents.locktreeWaitEscalation.timeps',
    'tokumx.ft.alerts.longWaitEvents.logBufferWaitps',
    'tokumx.ft.cachetable.evictions.full.leaf.clean.bytesps',
    'tokumx.ft.cachetable.evictions.full.leaf.clean.countps',
    'tokumx.ft.cachetable.evictions.full.leaf.dirty.bytesps',
    'tokumx.ft.cachetable.evictions.full.leaf.dirty.countps',
    'tokumx.ft.cachetable.evictions.full.leaf.dirty.timeps',
    'tokumx.ft.cachetable.evictions.full.nonleaf.clean.bytesps',
    'tokumx.ft.cachetable.evictions.full.nonleaf.clean.countps',
    'tokumx.ft.cachetable.evictions.full.nonleaf.dirty.bytesps',
    'tokumx.ft.cachetable.evictions.full.nonleaf.dirty.countps',
    'tokumx.ft.cachetable.evictions.full.nonleaf.dirty.timeps',
    'tokumx.ft.cachetable.evictions.partial.leaf.clean.bytesps',
    'tokumx.ft.cachetable.evictions.partial.leaf.clean.countps',
    'tokumx.ft.cachetable.evictions.partial.nonleaf.clean.bytesps',
    'tokumx.ft.cachetable.evictions.partial.nonleaf.clean.countps',
    'tokumx.ft.cachetable.miss.countps',
    'tokumx.ft.cachetable.miss.full.countps',
    'tokumx.ft.cachetable.miss.full.timeps',
    'tokumx.ft.cachetable.miss.partial.countps',
    'tokumx.ft.cachetable.miss.partial.timeps',
    'tokumx.ft.cachetable.miss.timeps',
    'tokumx.ft.checkpoint.begin.timeps',
    'tokumx.ft.checkpoint.countps',
    'tokumx.ft.checkpoint.timeps',
    'tokumx.ft.checkpoint.write.leaf.bytes.compressedps',
    'tokumx.ft.checkpoint.write.leaf.bytes.uncompressedps',
    'tokumx.ft.checkpoint.write.leaf.countps',
    'tokumx.ft.checkpoint.write.leaf.timeps',
    'tokumx.ft.checkpoint.write.nonleaf.bytes.compressedps',
    'tokumx.ft.checkpoint.write.nonleaf.bytes.uncompressedps',
    'tokumx.ft.checkpoint.write.nonleaf.countps',
    'tokumx.ft.checkpoint.write.nonleaf.timeps',
    'tokumx.ft.fsync.countps',
    'tokumx.ft.fsync.timeps',
    'tokumx.ft.log.bytesps',
    'tokumx.ft.log.countps',
    'tokumx.ft.log.timeps',
    'tokumx.ft.serializeTime.leaf.compressps',
    'tokumx.ft.serializeTime.leaf.decompressps',
    'tokumx.ft.serializeTime.leaf.deserializeps',
    'tokumx.ft.serializeTime.leaf.serializeps',
    'tokumx.ft.serializeTime.nonleaf.compressps',
    'tokumx.ft.serializeTime.nonleaf.decompressps',
    'tokumx.ft.serializeTime.nonleaf.deserializeps',
    'tokumx.ft.serializeTime.nonleaf.serializeps',
    'tokumx.metrics.document.deletedps',
    'tokumx.metrics.document.insertedps',
    'tokumx.metrics.document.returnedps',
    'tokumx.metrics.document.updatedps',
    'tokumx.metrics.getLastError.wtime.numps',
    'tokumx.metrics.getLastError.wtime.totalMillisps',
    'tokumx.metrics.getLastError.wtimeoutsps',
    'tokumx.metrics.operation.idhackps',
    'tokumx.metrics.operation.scanAndOrderps',
    'tokumx.metrics.queryExecutor.scannedps',
    'tokumx.metrics.repl.apply.batches.numps',
    'tokumx.metrics.repl.apply.batches.totalMillisps',
    'tokumx.metrics.repl.apply.opsps',
    'tokumx.metrics.repl.network.bytesps',
    'tokumx.metrics.repl.network.getmores.numps',
    'tokumx.metrics.repl.network.getmores.totalMillisps',
    'tokumx.metrics.repl.network.opsps',
    'tokumx.metrics.repl.network.readersCreatedps',
    'tokumx.metrics.repl.oplog.insert.numps',
    'tokumx.metrics.repl.oplog.insert.totalMillisps',
    'tokumx.metrics.repl.oplog.insertBytesps',
    'tokumx.metrics.ttl.deletedDocumentsps',
    'tokumx.metrics.ttl.passesps',
    'tokumx.opcounters.commandps',
    'tokumx.opcounters.deleteps',
    'tokumx.opcounters.getmoreps',
    'tokumx.opcounters.insertps',
    'tokumx.opcounters.queryps',
    'tokumx.opcounters.updateps',
    'tokumx.opcountersRepl.commandps',
    'tokumx.opcountersRepl.deleteps',
    'tokumx.opcountersRepl.getmoreps',
    'tokumx.opcountersRepl.insertps',
    'tokumx.opcountersRepl.queryps',
    'tokumx.opcountersRepl.updateps',
]


IDX_HISTS = [
    'size',
    'count',
    'avgObjSize',
    'storageSize',
]

COLL_HISTS = [
    'totalIndexSize',
    'nindexes',
    'size',
    'count',
    'nindexesbeingbuilt',
    'totalIndexStorageSize',
    'storageSize',
]


DB_STATS = [
    'avgObjSize',
    'collections',
    'dataSize',
    'indexSize',
    'indexStorageSize',
    'indexes',
    'objects',
    'storageSize'
]
