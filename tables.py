from sqlalchemy import create_engine

engine = create_engine('postgresql://usr:pass@localhost:3000/sqlalchemy')


class Product(base):
    __tablename__ = 'possible_solutions'
    id=Column(Integer, primary_key=True)
    title=Column('solutions_for_a_8x8_board', String(32))
