#센서 값 랜덤 생성
import random
#보너스 과제 - 로그 타임스탬프
import datetime


#__init__ : 자동 호출 초기화 메소드
#self : 인스턴스 참조, 멤버 변수 접근 시 사용
class DummySensor:
    def __init__(self):
        self.env_values = {
            'mars_base_internal_temperature': 0,
            'mars_base_external_temperature': 0,
            'mars_base_internal_humidity': 0,
            'mars_base_external_illuminance': 0,
            'mars_base_internal_co2': 0,
            'mars_base_internal_oxygen': 0,
        }

    #각 항목의 범위 안에서 랜덤 값 생성
    def set_env(self):
        self.env_values['mars_base_internal_temperature'] = round(random.uniform(18, 30), 2)
        self.env_values['mars_base_external_temperature'] = round(random.uniform(0, 21), 2)
        self.env_values['mars_base_internal_humidity'] = round(random.uniform(50, 60), 2)
        self.env_values['mars_base_external_illuminance'] = round(random.uniform(500, 715), 2)
        self.env_values['mars_base_internal_co2'] = round(random.uniform(0.02, 0.1), 4)
        self.env_values['mars_base_internal_oxygen'] = round(random.uniform(4, 7), 2)

    #env_values 반환 후 현재 날짜/시간과 모든 센서 값 추가
    def get_env(self):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        log_line = (
            f"{timestamp}, "
            f"{self.env_values['mars_base_internal_temperature']}, "
            f"{self.env_values['mars_base_external_temperature']}, "
            f"{self.env_values['mars_base_internal_humidity']}, "
            f"{self.env_values['mars_base_external_illuminance']}, "
            f"{self.env_values['mars_base_internal_co2']}, "
            f"{self.env_values['mars_base_internal_oxygen']}"
        )

        with open('mars_base_log.csv', 'a', encoding='utf-8') as log_file:
            log_file.write(log_line + '\n')

        return self.env_values


ds = DummySensor() #인스턴스 생성
ds.set_env() #랜덤 값 채우기
print(ds.get_env()) # 출력 + 로그 저장
