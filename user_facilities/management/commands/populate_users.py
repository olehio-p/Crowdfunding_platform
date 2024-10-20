from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from user_facilities.models.Language import Language
from user_facilities.models.Location import Location
from user_facilities.models.User import CustomUser
from datetime import date

class Command(BaseCommand):
    help = 'Populate User and CustomUser tables'

    def handle(self, *args, **options):
        users_data = [
            ('John Doe', 'john.doe@gmail.com', 'hash12345', 'creator', '2023-01-15', '123-456-7890', 1, 1),
            ('Maria Lopez', 'maria.lopez@yahoo.com', 'hash54321', 'creator', '2022-10-10', '555-234-5678', 2, 3),
            ('Max Müller', 'max.muller@example.de', 'hash67890', 'creator', '2023-03-22', '491-123-456789', 4, 5),
            ('Emily Johnson', 'emily.johnson@outlook.com', 'hash98765', 'creator', '2023-04-01', '987-654-3210', 1, 2),
            ('Ahmed Hassan', 'ahmed.hassan@gmail.com', 'hash19283', 'backer', '2023-02-20', '555-876-5432', 10, 8),
            ('Sakura Tanaka', 'sakura.tanaka@japanmail.jp', 'hash13579', 'backer', '2022-11-05', '81-90-1234-5678', 6,
             9),
            ('Carlos Pereira', 'carlos.pereira@brasilmail.com', 'hash24680', 'creator', '2023-01-30', '555-123-9876', 9,
             13),
            ('Zara Khan', 'zara.khan@indiaemail.in', 'hash11223', 'backer', '2022-12-10', '91-98765-43210', 11, 12),
            (
            'Liam O\'Connor', 'liam.oconnor@ukmail.co.uk', 'hash44556', 'admin', '2023-01-25', '44-20-7896-1234', 5, 6),
            ('Anna Novak', 'anna.novak@polandmail.pl', 'hash77889', 'creator', '2023-03-10', '48-22-654-7890', 14, 7),
            ('Isabella Rossi', 'isabella.rossi@italia.com', 'hash99887', 'creator', '2023-04-18', '39-06-1234-5678', 12,
             10),
            ('Jin Park', 'jin.park@koreamail.kr', 'hash33221', 'creator', '2023-05-12', '82-10-2345-6789', 7, 17),
            ('Sophie Dupont', 'sophie.dupont@francemail.fr', 'hash66789', 'backer', '2022-09-29', '33-1-234-56789', 3,
             18),
            ('Lucas Martins', 'lucas.martins@portugmail.pt', 'hash44567', 'creator', '2023-02-14', '351-21-234-5678', 9,
             13),
            ('Fatima Al-Salem', 'fatima.salem@arabmail.com', 'hash90876', 'admin', '2023-03-07', '971-50-123-4567', 10,
             11),
            ('Nina Ivanova', 'nina.ivanova@russianmail.ru', 'hash56932', 'creator', '2023-06-02', '7-495-1234567', 8,
             14),
            ('David Svensson', 'david.svensson@swemail.se', 'hash33456', 'backer', '2023-03-15', '46-8-123-4567', 13,
             19),
            ('Oliver Dubois', 'oliver.dubois@francemail.fr', 'hash88653', 'creator', '2023-04-05', '33-1-765-4321', 3,
             15),
            (
            'Ewa Kowalski', 'ewa.kowalski@polandmail.pl', 'hash22334', 'backer', '2023-03-28', '48-22-123-9876', 14, 7),
            ('Juan Gomez', 'juan.gomez@spanishmail.es', 'hash99442', 'creator', '2023-05-20', '34-91-234-5678', 2, 16),
            ('Chloe Brown', 'chloe.brown@usamail.com', 'hash77882', 'creator', '2023-02-10', '123-456-7890', 1, 1),
            (
            'Giuseppe Conti', 'giuseppe.conti@italymail.it', 'hash10293', 'backer', '2023-04-22', '39-02-1234-5678', 12,
            10),
            ('Li Wei', 'li.wei@chinamail.cn', 'hash33412', 'backer', '2022-08-18', '86-10-2345-6789', 5, 9),
            ('Paula Sanchez', 'paula.sanchez@colombiemail.co', 'hash09873', 'admin', '2023-01-18', '57-1-234-5678', 2,
             4),
            ('Samir Patel', 'samir.patel@indiamail.in', 'hash23489', 'backer', '2023-03-21', '91-22-6543-2100', 11, 12),
            ('Hiroshi Yamada', 'hiroshi.yamada@japanmail.jp', 'hash11223', 'creator', '2023-05-10', '81-3-1234-5678', 6,
             9),
            ('Laura White', 'laura.white@ukmail.co.uk', 'hash56932', 'creator', '2023-04-29', '44-20-1234-5678', 5, 6),
            ('Mohammed Ali', 'mohammed.ali@pakmail.pk', 'hash77894', 'backer', '2022-11-13', '92-21-123-4567', 11, 11),
            ('Natalie Kim', 'natalie.kim@koreamail.kr', 'hash99223', 'backer', '2023-06-01', '82-2-2345-6789', 7, 17),
            ('Oliver Thompson', 'oliver.thompson@usamail.com', 'hash22345', 'creator', '2023-02-25', '987-654-3210', 1,
             1),
        ]

        for name, email, password, user_type, join_date, phone_number, language_id, location_id in users_data:
            first_name, last_name = name.split(' ', 1)

            user = User.objects.create_user(
                username=email.split('@')[0],
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            language = Language.objects.get(id=language_id) if language_id else None
            location = Location.objects.get(id=location_id) if location_id else None

            custom_user, created = CustomUser.objects.get_or_create(
                user=user,
                bio=name,
                user_type=user_type,
                join_date=date.fromisoformat(join_date),
                phone_number=phone_number,
                language=language,
                location=location,
            )

            if created:
                self.stdout.write(self.style.SUCCESS(f'User "{name}" created successfully.'))
            else:
                self.stdout.write(self.style.WARNING(f'User "{name}" already exists.'))
