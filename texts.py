from settings import Settings


def get_settings_text():
    settings = Settings()
    settings_text = f"""==⚙️  Настройки  ⚙️==
    Качество скришотов: {settings.get_screenshots_quality()}"""
    return settings_text

stickers = [
    'CAACAgIAAxkBAAEJTTdkiICkwsp3K5Eq4CBVpczECuktiQACfRUAAhLriEjIEVNbWfPOxC8E',
    'CAACAgIAAxkBAAEJTTVkiICij31sZQ5ePimInA_B1KYCcgACeBQAAsn_iUgqte0AAT03v50vBA',
    'CAACAgIAAxkBAAEJTTNkiICg5bKmUF5bBQGcrPLg8hyzDwACKBoAAuF3iUhrWUJk51JV6C8E',
     'CAACAgQAAxkBAAEJTTFkiICZLiNKp1WAmXC5yALBeGt52wACqQgAAnQkMVKUD88QoVmqoC8E',
     'CAACAgIAAxkBAAEJTS9kiICVxJH-4iTwrdEQ13k7vsfhBgAChCoAAlM8iEhiQn9o-wnG-S8E',
     'CAACAgIAAxkBAAEJTS1kiICRAs1TW7cb6NI61QnWynwePgACISYAAvGFKEh4iKZWT8-9xi8E',
     'CAACAgIAAxkBAAEJTStkiICPu49to-PBEgx-S1AnSK6YOgACUhYAAteUGEkRJev63HQGNy8E',
     'CAACAgIAAxkBAAEJTSlkiICJm0u-Am6s_Ma95qi4IpFyQwACaBMAAhM6eEv28s2CYUvQqi8E',
    'CAACAgIAAxkBAAEJRx1khW6B3-KP48kviPU2B50d3ObGQgACKBkAAl7YaEi6ID1Kl5l8CC8E',
    'CAACAgIAAxkBAAEJTUNkiIEkHGlqpaEyiWNqsvvRAgRcvQACZRUAAh3kCEn1uRyj6mhnGS8E',
    'CAACAgIAAxkBAAEJTUFkiIEibQoHkXwXZKzjhj2nmCxXowACzRkAAofYEEoyOK71oIa9IS8E',
    'CAACAgIAAxkBAAEJTT9kiIEdKpoUy9-67rjxKPOVkFR_QQACyRQAAnxuGUoIzGxM3YKEHy8E',
    'CAACAgIAAxkBAAEJTT1kiIEagjo1h_CK4ERzxVOgznDTLwACehkAAogEEEodpaDiCZejky8E',
    'CAACAgIAAxkBAAEJTTtkiIEXY4wy93TKpKRqeb36S3W0kwACiRYAAnnZiUg5OWD6C6-61C8E'
]
