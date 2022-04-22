from importlib_metadata import metadata
from sqlalchemy import create_engine, Column, MetaData, literal


from clickhouse_sqlalchemy import Table, make_session, get_declarative_base, types, engines


uri = "clickhouse://default:@clickhouse_server/test"


engine = create_engine(uri)
session = make_session(engine)
metadata = MetaData(bind=engine)


Base = get_declarative_base(metadata=metadata)


class Rate(Base):
    day = Column(types.Date, primary_key=True)
    value = Column(types.Int32)
    other_value = Column(
        types.DateTime, 
        clickhouse_codec=("DoubleDelta", "ZSTD")
    )

    __table_args__ = (engines.Memory(),)


another_table = Table(
    'another_rate', metadata, 
    Column('day', types.Date, primary_key=True),
    Column('value', types.Int32, server_default=literal(1)),
    engines.Memory()
)