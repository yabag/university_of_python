from Customer import Customer
from Call_Plan import CallPlanSimple, CallPlanFree2ndMinuteAfter10, CallPlanTwiceCheaperFirst5Minutes

if __name__ == "__main__":
    call_plans = (CallPlanSimple(),
                  CallPlanFree2ndMinuteAfter10(),
                  CallPlanTwiceCheaperFirst5Minutes())

    minutes = tuple(range(0, 26, 5))  # 0, 5, 10, 15, 20, 25 мин.

    # Сравним стоимости звонков для тарифов
    for call_type in ("Г", "М"):
        print("{:20}".format(call_type), end="")
        # Заголовок - минуты
        for minute in minutes:
            print("{:>8d} мин".format(minute), end="")
        print()

        # Подсчет стоимости
        for call_plan in call_plans:
            print("{:20}".format(call_plan.name), end="")
            for minute in minutes:
                print("{:>8.2f} руб.".format(call_plan.record_call(call_type, minute)), end="")
            print()

        print()
