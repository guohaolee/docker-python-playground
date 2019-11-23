import json
from sqlalchemy import create_engine, inspect, MetaData

# from pymongo import connect, disconnect


class Postgres_Connector():
    def __init__(self):
        super().__init__()
        self.client = None
        self.url = None
        self.metadata = None

    def build_url(self):
        """ build the connector url """
        self.url = 'postgresql+psycopg2://master:password@localhost:5433/fulcrum'
        return self.url

    def connect(self):
        self.build_url()
        engine = create_engine(self.url, echo=False)    #set eco=True for debugging
        self.client = engine.connect()

        return self.client

    def get_metadata(self):
        self.metadata = MetaData() 

    def exec_query(self, query):
        schema_name = 'fulcrum'
        with self.client.connect() as conn:
            conn.execute('SET search_path TO {schema}'.format(schema=schema_name))
            result = conn.execute(query)
            for res in result:
                print(res)

    def get_tables(self):
        res = self.client.execute("""SELECT * FROM pg_catalog.pg_tables""")
        return res

    def inspect(self):
        res = inspect(self.client)
        return res

   


    def load_tables(self):
        return self.metadata.reflect(bind=self.client)





# class MongoDB():
#     def __init__(self):
#         super().__init__()
#         self.client = None

#     def connect(self):
#         self.client = connect(host='mongodb://master@master@localhost:27017/productiondb')

if __name__ == "__main__":
    pg = Postgres_Connector()
    engine = pg.connect()
    metadata = MetaData(engine)
    

    # from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

    # students = Table(
    #                 'students', metadata, 
    #                 Column('id', Integer, primary_key = True), 
    #                 Column('name', String), 
    #                 Column('lastname', String),
    #                 )
    # teacher = Table(
    #                 'students', metadata, 
    #                 Column('id', Integer, primary_key = True), 
    #                 Column('name', String), 
    #                 Column('lastname', String),
    #                 )
    # metadata.create_all()   # create all table
    # students.create()       # create single table



    from sqlalchemy.ext.automap import automap_base
    Base = automap_base()
    Base.prepare(engine, reflect=True, schema='fulcrum')
    print(Base.classes.keys())

    Channels = Base.classes.channels
    from sqlalchemy.orm import Session, sessionmaker
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    query = session.query(Channels).filter_by(file_name='channels/responsys.py')
    res = query.first()
    
    query2 = session.query(Channels).all()
    for r in query2:
        print(r.id)

    



    # query = """SELECT  name,type from fulcrum.tables """
    # r = conn.execute(query)
    # for rv in r:
    #     print(r)

    # result = pg.get_tables()
    # for r in result:
    #     print(r)

    # inspector = pg.inspect()
    # print(dir(inspector))
    # print(inspector.default_schema_name)
    # print(inspector.get_table_names())
    # print(inspector.get_schema_names())