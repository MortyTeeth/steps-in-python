from datetime import datetime, timedelta


class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, "%H:%M").time()
        dur_time = datetime.strptime(duration, "%H:%M").time()
        self.duration = timedelta(hours=dur_time.hour, minutes=dur_time.minute)

        start_dt = datetime.combine(datetime.today(), self.start_time)
        end_dt = start_dt + self.duration
        self.end_time = end_dt.time()

    def __str__(self):
        return f"{self.topic}: {self.start_time.strftime('%H:%M')} – {self.end_time.strftime('%H:%M')}"


class Conference:
    def __init__(self):
        self.performances = []

    def add(self, lecture):
        new_start = datetime.combine(datetime.today(), lecture.start_time)
        new_end = datetime.combine(datetime.today(), lecture.end_time)

        for existing in self.performances:
            exist_start = datetime.combine(datetime.today(), existing.start_time)
            exist_end = datetime.combine(datetime.today(), existing.end_time)

            if not (new_end <= exist_start or new_start >= exist_end):
                raise ValueError("Провести выступление в это время невозможно")

        self.performances.append(lecture)

    def total(self):
        total_duration = sum((lecture.duration for lecture in self.performances), timedelta())
        return self._format_timedelta(total_duration)

    def longest_lecture(self):
        if not self.performances:
            return "00:00"
        max_duration = max(lecture.duration for lecture in self.performances)
        return self._format_timedelta(max_duration)

    def longest_break(self):
        if len(self.performances) < 2:
            return "00:00"

        sorted_lectures = sorted(self.performances, key=lambda lec: lec.start_time)
        max_break = timedelta()

        for i in range(1, len(sorted_lectures)):
            prev_end = datetime.combine(datetime.today(), sorted_lectures[i - 1].end_time)
            curr_start = datetime.combine(datetime.today(), sorted_lectures[i].start_time)
            gap = curr_start - prev_end
            if gap > max_break:
                max_break = gap

        return self._format_timedelta(max_break)

    def _format_timedelta(self, td):
        total_minutes = td.total_seconds() // 60
        hours = int(total_minutes // 60)
        minutes = int(total_minutes % 60)
        return f"{hours:02}:{minutes:02}"

    def __str__(self):
        result = "Conference schedule:\n"
        for lecture in self.performances:
            result += f"  {lecture}\n"
        return result.strip()
