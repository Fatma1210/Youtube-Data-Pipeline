from sqlmodel import SQLModel, create_engine, Session


class Database:
    def __init__(self, db_path: str = 'youtube_data.db'):
        self.engine = create_engine(f'sqlite:///{db_path}')

    def create_tables(self):
        SQLModel.metadata.create_all(self.engine)

    def get_session(self) -> Session:
        return Session(self.engine)