
from utils.dbapi.schemas.user import User, Queue, Game, HistoryGame, Promocode, Promoactive, Check, Withdrawal
from asyncpg import UniqueViolationError
from utils.dbapi.db_gino import db

async def add_user(user_id: int, f_name: str, l_name: str,referral_id: int, username: str, status: str, balance: float, all_game: int, win_game: int, luss_game: int, bonus_actie: int):
    try:
        user = User(user_id=user_id, f_name=f_name, l_name=l_name, referral_id=referral_id, username=username, status=status, balance=balance, all_game=all_game, win_game=win_game, luss_game=luss_game, bonus_actie=bonus_actie)
        await user.create()
    except UniqueViolationError:
        print('Ошибка добавления юзера')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_user():
    coint = await db.func.count(User.user_id).gino.scalar()
    return coint

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

async def upd_user_name(user_id, new_name):
    user = await select_user(user_id)
    await user.update(upd_name= new_name).apply()

async def upd_all_game(user_id):
    user = await select_user(user_id)
    all_game = user.all_game + 1
    await user.update(all_game=all_game).apply()

async def upd_win_game(user_id):
    user = await select_user(user_id)
    win_game = user.win_game + 1
    await user.update(win_game=win_game).apply()

async def upd_luss_game(user_id):
    user = await select_user(user_id)
    luss_game = user.luss_game + 1
    await user.update(luss_game=luss_game).apply()

async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args
    elif not args.isnumeric():
        args = '0'
        return args
    elif args.isnumeric():
        if int(args) == user_id:
            args = '0'
            return args
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args
        else:
            args = str(args)
            return args
    else:
        args = '0'
        return args

async def count_refs(user_id):
    refs = await User.query.where(User.referral_id == user_id).gino.all()
    return len(refs)

async def deposit_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance + amount
    await user.update(balance=new_balance).apply()

async def game_balance(user_id: int, amount):
    user = await select_user(user_id)
    new_balance = user.balance - amount
    await user.update(balance=new_balance).apply()

async def gamewin_balance(user_id: int, amount: int):
    user = await select_user(user_id)
    new_balance = user.balance + ((amount * 2) - (((amount * 2) * 20)/ 100))
    await user.update(balance=new_balance).apply()



async def add_queue(user_id: int, amount: int):
    queue = Queue(user_id=user_id, amount=amount)
    await queue.create()


async def del_queue(user_id: int):
    del_queue = await Queue.query.where(Queue.user_id == user_id).gino.first()
    if del_queue is None:
        pass
    else:
        await del_queue.delete()


async def game_start(user_one: int, user_two: int, amount: int, user_one_res: str, user_two_res: str, winner: int):
    game_start = Game(user_one=user_one, user_two=user_two, amount=amount, user_one_res=user_one_res, user_two_res=user_two_res, winner=winner)

    await game_start.create()

async def get_history(user_id: int, amount:int):
    game_starts = await Game.query.where(Game.user_one == user_id).gino.first()
    if game_starts is None:
        game_starts = await Game.query.where(Game.user_two == user_id).gino.first()
        create_his = HistoryGame(game_id=game_starts.game_id, user_one=game_starts.user_one, user_two=user_id, amount=amount,
                                 user_one_res='0', user_two_res='0', winner=0)
        await create_his.create()
    else:
        create_his = HistoryGame(game_id=game_starts.game_id, user_one=game_starts.user_one, user_two=user_id, amount=amount,
                                 user_one_res='0', user_two_res='0', winner=0)
        await create_his.create()

async def his_res(user_one: int, user_two:int,user_one_res: str):
    game_id = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    if game_id is None:
        game_id = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        game_his = await HistoryGame.query.where(HistoryGame.game_id == game_id.game_id).gino.first()
        await game_his.update(user_two_res=user_one_res).apply()
    else:
        game_his = await HistoryGame.query.where(HistoryGame.game_id == game_id.game_id).gino.first()
        await game_his.update(user_one_res=user_one_res).apply()

async def get_game(user_id: int, amount: int):
    game_starts = await Queue.query.where(Queue.amount == amount).gino.first()
    if game_starts is None:
        return False
    if game_starts.user_id > 0:
        await game_start(user_one=game_starts.user_id, user_two=user_id, amount=amount, user_one_res='0', user_two_res='0', winner=0)
        return game_starts.user_id

async def select_game(user_id: int):
    game_search = await Game.query.where(Game.user_one == user_id).gino.first()
    if game_search is None:
        game_search = await Game.query.where(Game.user_two == user_id).gino.first()
        return game_search.user_one
    else:
        return game_search.user_two

async def select_amount(user_id: int):
    game_search = await Game.query.where(Game.user_one == user_id).gino.first()
    if game_search is None:
        game_search = await Game.query.where(Game.user_two == user_id).gino.first()
        return game_search.amount
    else:
        return game_search.amount

async def game_res(user_one: int, user_two:int,user_one_res: str):
    game_edit = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    # his_edit = await HistoryGame.query.where(HistoryGame.user_one == user_one and HistoryGame.user_two == user_two).gino.first()
    if game_edit is None:
        game_edit = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        # his_edit = await HistoryGame.query.where(HistoryGame.user_one == user_two and HistoryGame.user_two == user_one).gino.first()
        # await his_edit.update(user_two_res=user_one_res).apply()
        await game_edit.update(user_two_res=user_one_res).apply()
        return game_edit.user_one_res
    else:
        # await his_edit.update(user_one_res=user_one_res).apply()
        await game_edit.update(user_one_res=user_one_res).apply()
        return game_edit.user_two_res

async def winner_res(user_one: int, user_two:int, winner:int):
    winner_edit = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    if winner_edit is None:
        winner_edit = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        await winner_edit.update(winner=winner).apply()
    else:
        await winner_edit.update(winner=winner).apply()
async def win_hest(user_one: int, user_two:int, winner:int):
    winner_edit = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    if winner_edit is None:
        winner_edit = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        game_his = await HistoryGame.query.where(HistoryGame.game_id == winner_edit.game_id).gino.first()
        await game_his.update(winner=winner).apply()
    else:
        game_his = await HistoryGame.query.where(HistoryGame.game_id == winner_edit.game_id).gino.first()
        await game_his.update(winner=winner).apply()
async def del_game(user_one: int, user_two: int):
    del_game = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    if del_game is None:
        del_game = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        await del_game.delete()
    else:
        await del_game.delete()

async def draw(user_one: int, user_two:int):
    draw = await Game.query.where(Game.user_one == user_one and Game.user_two == user_two).gino.first()
    if draw is None:
        draw = await Game.query.where(Game.user_one == user_two and Game.user_two == user_one).gino.first()
        await draw.update(user_one_res='0', user_two_res='0').apply()
    await draw.update(user_one_res='0', user_two_res='0').apply()

async def promo_check(promo: str):
    promo = await Promocode.query.where(Promocode.promo == promo).gino.first()
    if promo is None:
        return False
    else:
        return True

async def promo_chek_active(user_id: int, promo: str):
    promo_active = await Promoactive.query.where(Promoactive.user_id == user_id).gino.all()
    if promo_active is None:
        return True
    else:
        for prom in promo_active:
            if prom.promo == promo:
                return False

async def promo_active(user_id: int, promo: str):
    promos = await Promocode.query.where(Promocode.promo == promo).gino.first()
    activ_promo = Promoactive(promo=promo, user_id=user_id)
    await activ_promo.create()
    user_id = await User.query.where(User.user_id == user_id).gino.first()
    new_balance = user_id.balance + promos.amount
    await user_id.update(balance=new_balance).apply()

    return promos.amount


async def create_check(user_id: int, amount: int, bill_id: str, url_p: str):
    check = Check(user_id=user_id, amount=amount, bill_id=bill_id, url_p=url_p)
    await check.create()

async def get_check(bill_id: str):
    get_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    if get_check is None:
        return False
    else:
        return get_check
async def del_check(bill_id: str):
    del_check = await Check.query.where(Check.bill_id == bill_id).gino.first()
    await del_check.delete()


async def bonus_check(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    if user.bonus_actie <= 0:
        return True
    else:
        return False

async def bonus_active(user_id: int):
    user = await User.query.where(User.user_id == user_id).gino.first()
    user_bonus = user.balance + 25.0
    user_active = user.bonus_actie + 1
    await user.update(balance=user_bonus, bonus_actie=user_active).apply()


async def create_withdrawal(user_id: int, amount: int, requisites: str):
    user = await User.query.where(User.user_id == user_id).gino.first()
    user_balance = user.balance - float(amount)
    withdrawal = Withdrawal(user_id=user_id, amount=amount, requisites=requisites, res=0)
    await withdrawal.create()
    await user.update(balance=user_balance).apply()

async def faunds_withdrawal(user_id: int):
    user_withdrawal = await Withdrawal.query.where(Withdrawal.user_id == user_id).gino.first()
    if user_withdrawal is None:
        return False
    else:
        return user_withdrawal