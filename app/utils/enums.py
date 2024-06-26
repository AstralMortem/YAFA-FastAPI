from enum import Enum


class GenderEnum(Enum):
    male = "male"
    female = "female"


class TrainingAimEnum(Enum):
    flesh = "flesh"
    fit = "fit"
    lose = "lose"


class ExerciseTypeEnum(Enum):
    strenght_weight = "strenght_weight"
    strenght_reps = "strenght_reps"
    strenght_duration = "strenght_duration"
    cardio_duration = "cardio_duration"
    cardio_lenght = "cardio_lenght"
    stretch = "stretch"
