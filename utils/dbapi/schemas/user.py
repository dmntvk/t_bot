from utils.dbapi.db_gino import TimedBaseModel
from sqlalchemy import Column, BigInteger, String, sql, Float, INTEGER

class User(TimedBaseModel):
    __tablename__ = 'user'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    f_name = Column(String(200))
    l_name = Column(String(200))
    referral_id = Column(BigInteger)
    username = Column(String(50))
    status = Column(String(30))
    balance = Column(Float)
    all_game = Column(BigInteger)
    win_game = Column(BigInteger)
    luss_game = Column(BigInteger)
    bonus_actie = Column(BigInteger)

    query: sql.select

class Queue(TimedBaseModel):
    __tablename__ = 'queue_game'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    amount = Column(BigInteger)

    query: sql.select

class Game(TimedBaseModel):
    __tablename__ = 'game'
    game_id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_one = Column(BigInteger, primary_key=True)
    user_two = Column(BigInteger, primary_key=True)
    amount = Column(BigInteger)
    user_one_res = Column(String(50))
    user_two_res = Column(String(50))
    winner = Column(BigInteger)

    query: sql.select

class HistoryGame(TimedBaseModel):
    __tablename__ = 'history_game'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    game_id = Column(BigInteger)
    user_one = Column(BigInteger)
    user_two = Column(BigInteger)
    amount = Column(BigInteger)
    user_one_res = Column(String(50))
    user_two_res = Column(String(50))
    winner = Column(BigInteger)

    query: sql.select


class Promocode(TimedBaseModel):
    __tablename__ = 'promo-code'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50), primary_key=True)
    amount = Column(BigInteger)

    query: sql.select

class Promoactive(TimedBaseModel):
    __tablename__ = 'promo-active'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    promo = Column(String(50))
    user_id = Column(BigInteger)

    query: sql.select

class Check(TimedBaseModel):
    __tablename__ = 'check'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    bill_id = Column(String(255))
    user_id = Column(BigInteger)
    amount = Column(BigInteger)
    url_p = Column(String(500))

    query: sql.select


class Withdrawal(TimedBaseModel):
    __tablename__ = 'withdrawal'
    id = Column(INTEGER, autoincrement=True, primary_key=True)
    user_id = Column(BigInteger, primary_key=True)
    amount = Column(BigInteger)
    requisites = Column(String(500))
    res = Column(BigInteger)

    query: sql.select
