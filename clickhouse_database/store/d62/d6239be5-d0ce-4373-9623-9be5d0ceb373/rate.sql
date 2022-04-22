ATTACH TABLE _ UUID 'bbb450c3-5746-4005-bbb4-50c357468005'
(
    `day` Date,
    `value` Int32,
    `other_value` DateTime CODEC(DoubleDelta, ZSTD(1))
)
ENGINE = Memory
