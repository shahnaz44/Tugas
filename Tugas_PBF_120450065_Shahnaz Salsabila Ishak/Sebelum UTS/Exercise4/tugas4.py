import random


def skillcalc(S0, E, ka, kb):
    a = random.uniform(0,0.25) * E / 100
    b = random.uniform(0,0.25) * ( ka / ( ka + kb ) )
    S = S0 * ( 1 - ( a + b ))

    return S

def teamskill(parameter):
    SS_GK = parameter['SS_GK']
    TS_D = parameter['TS_D']
    PS_D = parameter['PS_D']
    TS_MD = parameter['TS_MD']
    DS_MD = parameter['DS_MD']
    DS_ATK = parameter['DS_ATK']
    IS_ATK = parameter['IS_ATK']
    SS_ATK = parameter['SS_ATK']
    E_GK = parameter['E_GK']
    E_DF = parameter['E_DF']
    E_MD = parameter['E_MD']
    E_ATK = parameter['E_ATK']
    ka = parameter['ka']
    kb = parameter['kb']

    #SS_GK = Save skill of Goalkeeper
    #TS_D = Tackle skill of Defender
    #PS_D = Passing skill of Defender
    #TS_MD = Tackle skill of Midfielder
    #DS_MD = Dribbling skill of Midfielder
    #DS_ATK = Dribbling skill of Attacker
    #IS_ATK = intercept skill of Attacker
    #SS_ATK = shooting skill of Attacker

    saveskill = skillcalc(SS_GK, E_GK, ka, kb)
    tackleskill_DF = skillcalc(TS_D, E_DF, ka, kb)
    passingskill = skillcalc(PS_D, E_DF, ka, kb)
    tackleskill_MD = skillcalc(TS_MD, E_MD, ka, kb)
    dribble_MD = skillcalc(DS_MD, E_MD, ka, kb)
    dribble_atk = skillcalc(DS_ATK, E_ATK, ka, kb)
    intercept = skillcalc(IS_ATK, E_ATK, ka, kb)
    shoot = skillcalc(SS_ATK, E_ATK, ka, kb)

    role_skill =['GK_Save', 'DF_Tack', 'DF_Pass', 'MD_Tack', 'MD_Drib', 'ATK_Drib', 'ATK_Int', 'ATK_Shoot']
    skill_value =[saveskill, tackleskill_DF, passingskill, tackleskill_MD, dribble_MD, dribble_atk, intercept, shoot]

    return dict(zip(role_skill, skill_value))


def MDAvsMDB(Ateam, Bteam):
    MDA_Drib = Ateam['MD_Drib']
    MDA_Tack = Ateam['MD_Tack']
    MDB_Drib = Bteam['MD_Drib']
    MDB_Tack = Bteam['MD_Tack']

    global ball, t

    print('Bola diterima oleh Midfielder ', ball)
    print('Terjadi pertarungan antara Midfielder A dan Midfielder B')
    if ball == 'A':
        if MDA_Drib > MDB_Tack:
            print('Bola berhasil dipertahankan oleh Midfielder A dan dioper menuju Attacker A')
        else:
            print('Bola gagal dipertahankan oleh Midfielder', ball)
            ball = 'B'
            print('Bola diambil alih oleh Midfielder B dan dioper menuju Attacker B')
    elif ball == 'B':
        if MDB_Drib > MDA_Tack:
            print('Bola berhasil dipertahankan oleh Midfielder B dan dioper menuju Attacker B')
        else:
            print('Bola gagal dipertahankan oleh Midfielder', ball)
            ball = 'A'
            print('Bola diambil alih oleh Midfielder A dan dioper menuju Attacker A')
    t += 3

def ATKvsGK(Ateam, Bteam):
    SS_ATKA = Ateam['ATK_Shoot']
    SS_GKA = Ateam['GK_Save']
    SS_ATKB = Bteam['ATK_Shoot']
    SS_GKB = Bteam['GK_Save']

    global ball, A_score, B_score, t, status

    if ball == 'A':
        if SS_ATKA > SS_GKB:
            A_score += 1
            print('Attacker A berhasil melakukan shoot dan mencetak gol')
            print(f'Score sementara adalah\nTeam A : {A_score}\nTeam B : {B_score}')
            ball = 'B'
            status = 'newmatch'
            print('_' * 90)
        else:
            print('Keeper B berhasil menangkap bola dan bola dioper menuju Defender B')
            ball = 'B'
            status = 'inprogress'


    elif ball == 'B':
        if SS_ATKB > SS_GKA:
            B_score += 1
            print('Attacker B berhasil melakukan shoot dan mencetak gol')
            print(f'Score sementara adalah\nTeam A : {A_score}\nTeam B : {B_score}')
            ball = 'A'
            status = 'newmatch'
            print('_' * 90)
        else:
            print('Keeper A berhasil menangkap bola dan bola dioper menuju Defender A')
            ball = 'B'
            status = 'inprogress'
    t += 5

def ATKvsDF(Ateam, Bteam):
    DS_ATKA = Ateam['ATK_Drib']
    DS_ATKB = Bteam['ATK_Drib']
    TS_DA = Ateam['DF_Tack']
    TS_DB = Bteam['DF_Tack']

    global ball, t
    if ball == 'A':
        if DS_ATKA > TS_DB:
            print('Attacker A berhasil melewati Defender B\nAttacker A akan melakukan shoot')
            ATKvsGK(Ateam, Bteam)
        else:
            print('Attacker A gagal melewati Defender B\nDefender B berhasil merebut bola!')
            ball = 'B'
    elif ball == 'B':
        if DS_ATKB > TS_DA:
            print('Attacker B berhasil melewati Defender A\nAttacker B akan melakukan shoot')
            ATKvsGK(Ateam, Bteam)
        else:
            print('Attacker B gagal melewati Defender A\nDefender A berhasil merebut bola!')
            ball = 'A'

    t += 3

def DFvsATK(Ateam, Bteam):
    IS_ATKA = Ateam['ATK_Int']
    IS_ATKB = Bteam['ATK_Int']
    PS_DA = Ateam['DF_Pass']
    PS_DB = Bteam['DF_Pass']

    global ball, t
    if ball == 'A':
        if PS_DA > IS_ATKB:
            print('Defender A berhasil melakukan pass ke Midfielder A!')
        elif PS_DA < IS_ATKB:
            print('Defender A gagal melakukan pass ke Midfielder A!\nBola direbut Attacker B dan bersiap melakukan shoot')
            ball = 'B'
            ATKvsGK(Ateam, Bteam)
    elif ball == 'B':
        if PS_DB > IS_ATKA:
            print('Defender B berhasil melakukan pass ke Midfielder B!')
        elif PS_DB < IS_ATKA:
            print('Defender B gagal melakukan pass ke Midfielder B!\nBola direbut Attacker A dan bersiap melakukan shoot')
            ball = 'A'
            ATKvsGK(Ateam, Bteam)

    t += 3


team_A = {
    'SS_GK' : 81,
    'TS_D' : 78,
    'PS_D' : 78,
    'TS_MD' : 60,
    'DS_MD' : 76,
    'DS_ATK' : 80,
    'IS_ATK' : 85,
    'SS_ATK' : 92,
    'E_GK' : 80,
    'E_DF' : 79,
    'E_MD' : 78,
    'E_ATK' : 77,
    'ka'    : 100000,
    'kb'    : 115000

}

team_B = {
    'SS_GK' : 86,
    'TS_D' : 80,
    'PS_D' : 81,
    'TS_MD' : 70,
    'DS_MD' : 70,
    'DS_ATK' : 81,
    'IS_ATK' : 86,
    'SS_ATK' : 90,
    'E_GK' : 77,
    'E_DF' : 78,
    'E_MD' : 79,
    'E_ATK' : 80,
    'ka'    : 115000,
    'kb'    : 100000

}



def gamestart(team_A, team_B):
    global t, ball, A_score, B_score, status

    t = 0
    ball = 'A' #Posisi bola pertama

    A_score = 0
    B_score = 0

    status = 'inprogress'

    while t >= 0 and t <= 90:
        Ateam_skill = teamskill(team_A) #Agar skill setiap permain berubah-ubah setiap pertandingan
        Bteam_skill = teamskill(team_B)

        status = 'inprogress'
        MDAvsMDB(Ateam_skill, Bteam_skill)
        ATKvsDF(Ateam_skill, Bteam_skill)
        if status == 'newmatch':
            continue
        elif status == 'inprogress':
            DFvsATK(Ateam_skill, Bteam_skill)

    print('_' * 90)
    print('Pertandingan telah berakhir!')
    print('-' * 90)

    print(f'Score akhir adalah\nTeam A : {A_score}\nTeam B : {B_score}')

    result = (lambda A, B : 'dimenangkan oleh Team A' if A > B else (lambda A, B : 'dimenangkan oleh Team B' if A < B else 'adalah seri')(A_score, B_score))(A_score, B_score)

    print(f'Hasil akhir dari pertandingan kali ini {result}')

gamestart(team_A,team_B)
