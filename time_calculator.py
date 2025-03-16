from datetime import timedelta


class TimeCalculator:
    @staticmethod
    def calculate_total_time(todos):
        
        total_time = timedelta(minutes=0)
        for todo in todos:
            if not todo.complete:
                total_time += timedelta(minutes=30)  # Assuming each todo takes 30 minutes to complete
        return total_time