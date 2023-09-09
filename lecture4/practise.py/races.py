from import_this import RACE_DATA
from racer_time import convert_seconds

if __name__ == "__main__":
    human: str = ""
    for place in RACE_DATA.values():
        if place.get('FinishedPlace') == 1:
            human = f"Выиграл - {place.get('RacerName').upper()}!!!Поздравляем!!"
            break
    print(human)
    print('_' * len(human))

    print('Первые три места: ')
    for racer in range(1, 3+1):
        if racer == 1:
            racer_info = f'\tГонщик на первом месте'
        elif racer == 2:
            racer_info = f'\tГонщик на втором месте'
        else:
            racer_info = f'\tГонщик на третьем месте'
        
        for full_desc in RACE_DATA.values():
            if full_desc.get('FinishedPlace') == racer:
                racer_info += f'\tИмя: {full_desc.get("RacerName")}'
                racer_info += f'\tКоманда: {full_desc.get("RacerTeam")}\t'
                racer_info += convert_seconds(full_desc.get('FinishedTimeSeconds'))
        print(racer_info)
