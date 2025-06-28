from datetime import datetime, timedelta, date, time


def math_tutor(start, end):
    start_time = start.time()
    end_time = end.time()

    delta = timedelta(hours=end_time.hour, minutes=end_time.minute) - timedelta(hours=start_time.hour,
                                                                                minutes=start_time.minute)

    if delta.total_seconds() // 60 > 45:
        base_datetime = datetime.combine(datetime.today(), start_time)
        end_datetime = datetime.combine(datetime.today(), end_time)
        while end_datetime - base_datetime >= timedelta(minutes=45):
            print(base_datetime.strftime('%H:%M'), '-', (base_datetime + timedelta(minutes=45)).strftime('%H:%M'))
            base_datetime = base_datetime + timedelta(minutes=55)


start_work_day = datetime.strptime(input(), '%H:%M')
end_work_day = datetime.strptime(input(), '%H:%M')

math_tutor(start_work_day, end_work_day)
