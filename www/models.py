from django.db import models
from users.models import CustomUser


class Symptom(models.Model):
    MOOD_CHOICES = (
        ('calm', 'Спокойная'),
        ('happy', 'Радостная'),
        ('energetic', 'Энергичная'),
        ('playful', 'Игривая'),
        ('mood_swings', 'Перепады настроения'),
        ('irritated', 'Раздраженная'),
        ('sad', 'Грустная'),
        ('anxious', 'Встревоженная'),
        ('depressed', 'Подавлена'),
        ('guilty', 'Чувство вины'),
        ('obsessive_thoughts', 'Навязчивые мысли'),
        ('low_energy', 'Мало энергии'),
        ('apathetic', 'Апатичная'),
        ('confused', 'Растерянная'),
        ('self_critical', 'Жесткая самокритика')
    )
    mood = models.CharField(max_length=30, choices=MOOD_CHOICES, null=True, blank=True)

    SYMPTOM_NAME_CHOICES = (
        ('all_ok', 'Все в порядке'),
        ('lower_abdominal_pain', 'Боли внизу живота'),
        ('sensitive_breasts', 'Чувствительная грудь'),
        ('headache', 'Головная боль'),
        ('acne', 'Прыщи'),
        ('back_pain', 'Боль в спине'),
        ('fatigue', 'Усталость'),
        ('increased_appetite', 'Повышенный аппетит'),
        ('insomnia', 'Бессонница'),
        ('abdominal_pain', 'Боль в животе'),
        ('vaginal_dryness', 'Сухость во влагалище')
    )
    symptom_name = models.CharField(max_length=30, choices=SYMPTOM_NAME_CHOICES, null=True, blank=True)

    DISCHARGE_CHOICES = (
        ('none', 'Выделений нет'),
        ('creamy', 'Кремообразные'),
        ('watery', 'Водянистые'),
        ('sticky', 'Липкие'),
        ('mucous', 'Слизистые'),
        ('spotting', 'Кровомажущие'),
        ('atypical', 'Нетипичные')
    )
    discharge = models.CharField(max_length=30, choices=DISCHARGE_CHOICES, null=True, blank=True)

    DIGESTION_CHOICES = (
        ('nausea', 'Тошнота'),
        ('bloating', 'Вздутие живота'),
        ('constipation', 'Запор'),
        ('diarrhea', 'Диарея')
    )
    digestion = models.CharField(max_length=30, choices=DIGESTION_CHOICES, null=True, blank=True)

    OTHER_CHOICES = (
        ('travel', 'Путешествие'),
        ('stress', 'Стресс'),
        ('meditation', 'Медитация'),
        ('journaling', 'Ведение дневника'),
        ('kegel_exercises', 'Упражнения Кегеля'),
        ('breathing_exercises', 'Дыхательные упражнения'),
        ('illness_or_injury', 'Болезнь или травма'),
        ('alcohol', 'Алкоголь')
    )
    other = models.CharField(max_length=30, choices=OTHER_CHOICES, null=True, blank=True)

    PHYSICAL_ACTIVITY_CHOICES = (
        ('none', 'Тренировки не было'),
        ('yoga', 'Йога'),
        ('gym', 'Тренажерный зал'),
        ('aerobics_and_dance', 'Аэробика и танцы'),
        ('swimming', 'Плавание'),
        ('team_sport', 'Командный спорт'),
        ('running', 'Бег'),
        ('cycling', 'Велосипед'),
        ('walking', 'Ходьба')
    )
    physical_activity = models.CharField(max_length=30, choices=PHYSICAL_ACTIVITY_CHOICES, null=True, blank=True)
    water = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class MenstrualDayStatus(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('periods', 'Periods.'),
        ('ordinary_day', 'Ordinary Day.'),
        ('ovulation', 'Ovulation.'),
        ('period_may_start', 'Maybe your period will start today.'),
        ('delay_of_menstruation', 'Delay of menstruation.')
    )
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='ordinary_day')
    date = models.DateField(auto_now_add=True)
    symptoms = models.ForeignKey(Symptom, on_delete=models.SET_NULL, null=True, blank=True, default=None)
