from contextlib import contextmanager

text = {
    'hello_logic': {
        'hello': '<Name>, добрый день! Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами.  Подскажите, вам удобно сейчас говорить?',
        'hello_repeat': 'Это компания X  Подскажите, вам удобно сейчас говорить?',
        'hello_null': 'Извините, вас не слышно. Вы могли бы повторить'
    },
    'main_logic': {
        'recommend_main': 'Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую.',
        'recommend_repeat': 'Как бы вы оценили возможность порекомендовать нашу компанию своим знакомым по шкале от 0 до 10, где 0 - точно не порекомендую, 10 - обязательно порекомендую.',
        'recommend_repeat_2': 'Ну если бы вас попросили порекомендовать нашу компанию друзьям или знакомым, вы бы стали это делать? Если «да» - то оценка «10», если точно нет – «0».',
        'recommend_score_negative': 'Ну а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?',
        'recommend_score_neutral': 'Ну а от 0 до 10 как бы вы оценили ?',
        'recommend_score_positive': 'Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10  ?',
        'recommend_null': 'Извините вас свосем не слышно,  повторите пожалуйста ?',
        'recommend_default': 'повторите пожалуйста '
    },
    'hangup_logic': {
        'hangup_positive': 'Отлично!  Большое спасибо за уделенное время! Всего вам доброго!',
        'hangup_negative': 'Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго. ',
        'hangup_wrong_time': 'Извините пожалуйста за беспокойство. Всего вам доброго',
        'hangup_null': 'Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго'
    },
    'forward_logic': {
        'forward': 'Чтобы разобраться в вашем вопросе, я переключу звонок на моих коллег. Пожалуйста оставайтесь на линии.'
    }
}
Null = None
name = 'vova'
negativ_mark = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
positiv_mark = ['9', '10']


class NeuroLingvo(name, flag):

    def __init__(self):
        self.name = name
        self.flag = flag

    @contextmanager
    def listen(self):
        ...

    def say(self):
        ...

    def synthesize(self):
        ...

    def media_params(self, name):
        self.name = name


nv = NeuroLingvo()
nv.media_params('lang', 'ru_RU')
lang = nv.media_params('lang')
nv.media_params({'asr': 'google', 'tts': 'yandex'})
current_asr = nv.media_params('asr')
currnet_tts = nv.media_params('tts')


def hello_repeat(hello_rep_text):
    nv.synthesize(hello_rep_text, ssml: False)


def hello_null(hello_null_text, rep):
    nv.synthesize(hello_null_text, ssml: False)
    rep += 1
    return rep

def recommend_default(rec_def_text, rep_rec):
    nv.synthesize(rec_def_text, ssml: False)
    rep_rec += 1
    return rep_rec


def recommend_null(rec_null, rep_rec):
    nv.synthesize(rec_null, ssml: False)
    rep_rec += 1
    return rep_rec


def hangup_wrong_time(hung_up_text):
    nv.synthesize(hung_up_text, ssml: False)
    break


def hangup_negative(hang_neg_text):
    nv.synthesize(hang_neg_text, ssml: False)


def hangup_null(hangup_null_text):
    nv.synthesize(hangup_null_text, ssml: False)
    break

def hangup_positive(hang_pos_text):
    nv.synthesize(hang_pos_text, ssml: False)
    break


def hello(name, modul):
    rep = 0
    with nv.listen('Да, Нет, Занят, Ещё раз') as r:
        if r == 'Да':
            recommend_main(text['main_logic']['recommend_main'])
        elif r == 'Нет':
            hangup_wrong_time(text['hangup_logic']['hungup_wrong_time']) #вот тут типо можно наверное закрыть
        elif r == 'Занят':
            hangup_wrong_time(text['hangup_logic']['hangup_wrong_time'])
        elif r == 'Ещё раз':
            hello_repeat(text['hello_logic']['hello_repeat'])
        elif r == None:
            if rep == 0:
                hello_null(text['hello_logic']['hello_null'], rep)
            elif rep == 1:
                hangup_null(text['hangup_logic']['hangup_null'])

        else:
            recommend_main(text['main_logic']['recommend_main'])


def recommend_main(recomend_text):
    rep_rec = 0
    nv.synthesize(recomend_text, ssml: False)
    with nv.listen('0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, нет, возможно, да, ещё раз, не знаю, занят, вопрос') as r:
        if r == Null:
            if rep_rec == 1:
                recommend_null(text['main_logic']['recommend_null'], rep_rec)
            elif rep_rec == 2:
                hangup_null(text['hangup_logic']['hangup_null'])
        elif r == '0' or '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8':
            hangup_negative(text['hangup_logic']['hangup_negative'])
        elif r == '9' or '10':
            hangup_positive(text['main_logic']['hangup_positive'])
        else:
            if rep_rec == 0:
                recommend_default(text['main_logic']['recommend_default'], rep_rec)
            elif rep_rec == 1:
                hangup_null(text['hangup_logic']['hangup_null'])



def hello_main():
    modul = text['hello_logic']
    hello(name, modul)

def main():
    return hello_main()

main()

