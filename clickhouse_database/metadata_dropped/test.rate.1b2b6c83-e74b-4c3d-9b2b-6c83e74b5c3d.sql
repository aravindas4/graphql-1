ATTACH TABLE _ UUID '1b2b6c83-e74b-4c3d-9b2b-6c83e74b5c3d'
(
    `day` Date,
    `value` Int32,
    `other_value` DateTime CODEC(DoubleDelta, ZSTD(1))
)
ENGINE = Memory
