from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Sequence
from sqlalchemy.orm import sessionmaker
import sqlalchemy

Base = declarative_base()


def validate_user(user):
    if len(user) != 5:
        raise ValueError('user must have 5 columns')
    if not user[0].isalpha() or not user[1].isalpha():
        raise ValueError('Only letters in first name and last name')
    if not user[2].isdigit() or not user[3].isdigit():
        raise ValueError('Only numbers in age and PESEL')
    if not 0 <= int(user[2]) <= 120:
        raise ValueError('Invalid age')
    if len(user[3]) != 11:
        raise ValueError('PESEL must have 11 digits')
    if float(user[4]) < 0:
        raise ValueError('salary must be grayter than 0')


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id_seq'), primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    PESEL = Column(String)
    salary = Column(Float)

    def __str__(self):
        print(f'{self.id} {self.first_name} {self.last_name}  {self.age} {self.PESEL} {self.salary}')


def operations_loop(engine):
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    session = Session()
    while True:
        choice = input('type - insert update delete or exit\n')
        if choice == 'insert':
            user = input('Add user f_n, l_n, age, PESEL, salary\n').split(' ')
            validate_user(user)
            new_customer = Users(
                first_name=user[0],
                last_name=user[1],
                age=int(user[2]),
                PESEL=user[3],
                salary=float(user[4]))
            session.add(new_customer)
            session.commit()
            print("User added...")
        elif choice == 'update':
            user = session.query(Users).all()
            list_of_id = [us.id for us in user]
            for cos in user:
                cos.__str__()
            user_id = int(input('What id to update?\n'))
            if user_id not in list_of_id:
                raise ValueError('Invalid id')
            user = session.query(Users).filter_by(id=user_id).first()
            user.__str__()
            print('first_name last_name age PESEL salary')
            values_to_update = input().split(' ')
            validate_user(values_to_update)

            user.first_name = values_to_update[0],
            user.last_name = values_to_update[1],
            user.age = int(values_to_update[2]),
            user.PESEL = values_to_update[3],
            user.salary = float(values_to_update[4])

            session.add(user)
            session.commit()
            print('User updated...')
        elif choice == 'delete':
            user = session.query(Users).all()
            list_of_id = [us.id for us in user]
            delete_id = int(input("which id delete?\n"))
            if delete_id not in list_of_id:
                raise ValueError('invalid id to delete')
            user = session.query(Users).filter_by(id=delete_id).first()
            user.__str__()
            confirm_delete = input("delete? y/n : ")
            if confirm_delete == 'y':
                session.delete(user)
                session.commit()
                print("user deleted...")
        elif choice == 'exit':
            break
        else:
            print('Wrong command')
