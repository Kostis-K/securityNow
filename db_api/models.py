import datetime
from enum import Enum
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, fields, EmbeddedDocumentListField

# Create your models here.
# class SpecialismType(str, Enum):
#     #DIGITAL = 'digital' # ti einai ayto dhladh?
#     POLYKATASTHMA = 'Πολυκατάστημα / Mall'
#     SUPERMARKET = 'Supermarket'
#     A8LHTIKES = 'Αθλητικές Εγκαταστάσεις / Parking / Εκθεσιακό Κέντρο'
#     HOTEL = 'Ξενοδοχείο'
#     XRHMATAPOSTOLH = 'Χρηματαποστολές'
#     DHMOSIO = 'Δημόσιο Κτήριο'
#     OIKIA = 'Βίλα / Οικία'
#     MUSEUM = 'Μουσείο'
#     AIRPORT = 'Αεροδρόμιο'
#     PORT = 'Λιμένας'
#     APO8HKH = 'Αποθήκη / Εργοστάσιο / Φυλάκιο'
#     BEACH = 'Οργανωμένη Παραλία / Πισίνα'
#     OTHER = 'Άλλο'
#
# class Specialism(EmbeddedDocument):
#     specialism = fields.EnumField(SpecialismType, default=None)
#     specialism_time_from = fields.DateField()
#     specialism_time_to = fields.DateField(default=datetime.datetime.utcnow())
#     #specialism_time_diff = fields.FloatField() #auto prokyptei
#
# class JobType(str, Enum):
#     PROSWPIKO_ASF = 'Προσωπικό Ασφαλείας - Φύλακας(Στατική φύλαξη)'
#     PATROL = 'Προσωπικό Ασφαλείας - Patrol'
#     ELEGKTHS = 'Ελεγκτής Ασφαλείας Αερομεταφορών(X - Ray Screener)'
#     EPOPTHS = 'Επόπτης Ασφαλείας'
#     SHMATA = 'Υπάλληλος κέντρου λήψεως σημάτων'
#     SYMVANTA = 'Διαχειριστής Συμβάντων Ασφαλείας (SOC–Security Incidents Administrator)'
#     XRHMATAPOSTOLES_ODHGOS = 'Οδηγός Χρηματαποστολών'
#     XRHMATAPOSTOLES_SYNODHGOS = 'Συνοδός Χρηματαποστολών'
#     KATAMETRHTHS = 'Καταμετρητής Χρηματαποστολών'
#     RECEPTION = 'Υπάλληλος Υποδοχής(Reception)'
#     ASFALEIA_RECEPTION = 'Υπάλληλος Ασφαλείας Υποδοχής(Reception)'
#     LIFEGUARD_SEE = 'Ναυαγοσώστης Πισίνας / Θαλάσσης(Lifeguard)'
#     LIFEGUARD_POOL = 'Ναυαγοσώστης Πισίνας(Lifeguard)'
#     KA8ARISTHS = 'Καθαριστής'
#     YPEY8YNOS_KA8ARISTHS = 'Υπεύθυνος τμήματος καθαριότητας'
#     TEXNIKOS_EGKATASTASHS = 'Τεχνικός Εγκατάστασης και Συντήρησης Συστημάτων Ασφαλείας'
#     SALES_SUPPORT = 'Sales Customer Support Specialist'
#     GRAMMATEIA = 'Υπάλληλος γραφείου(Γραμματεία)'
#     VOH8OS_GRAFEIOU = 'Βοηθός Γραφείου Ασφαλείας'
#     ATM = 'Τεχνικός - Διαχειριστής ΑΤΜ(άδεια security)'
#     PRESALES = 'Presales Engineer'
#     RISKMANAGEMENT = 'Security Risk Management Specialist'
#     PROCUREMENT = 'Procurement Officer'
#     APO8HKH = 'Υπάλληλος Αποθήκης'
#     APENTOMWSH = 'Τεχνικός Εφαρμογών Απεντομώσεων & Απολυμάνσεων – Γεωπόνος'
#     OTHER = 'Άλλο'
#
# class EducationLevel(str, Enum):
#     DHMOTIKO = "Δημοτικό"
#     GYMNASIO = "Γυμνάσιο"
#     LYKEIO = "Λύκειο"
#     IEK = "ΙΕΚ"
#     AEI_TEI = "ΑΕΙ/ΤΕΙ"
#     MASTER = "Μεταπτυχιακό"
#
# class SecurityLicense(str, Enum):
#     NAI = "Ναι"
#     OXI = "Όχι"
#     Expired = "Έχει λήξει"
#     YpoEkdosh = "Υπό έκδοση"
#
# class Military(str, Enum):
#     NAI = "Ναι"
#     OXI = "Όχι"
#     MhYpoxreos = "Μη Υπόχρεος"
#
# class CandidateStatus(str, Enum):
#     NOT_WORKING = "Δεν εργάζομαι – Αναζητώ μία θέση εργασίας."
#     WORKING = "Εργάζομαι, αλλά αναζητώ καλύτερες συνθήκες."
#     NOT_LOOKING = "Δεν αναζητώ μία θέση εργασίας προς το παρών."
#
# class DesirableWorkType(str, Enum):
#     FULL = "Πλήρους απασχόλησης"
#     PARTTIME = "Μερικής απασχόλησης"
#     SEASON = "Εποχιακή θέση"
#     CONTRACTOR = "Ελεύθερος Επαγγελματίας"
#     EVENT = "Έκτακτη θέση (Event)"
#
# class DesirableSchedule(str, Enum):
#     PRWINO = "ΔΕ-ΠΑ (Πρωινό)"
#     KYLIOMENO = "ΔΕ-ΠΑ (Κυλιόμενο)"
#     VRADINO = "ΔΕ-ΠΑ (Βραδινό)"
#     SAVVATO = "Σάββατο (Δυνατότητα εργασίας)"
#     KYRIAKH = "Κυριακή (Δυνατότητα εργασίας)"
#     ADIAFORO = "Αδιάφορο"
#
# class KartaAnergias(str, Enum):
#     ENERGH_MAKRO = "Ενεργή (Μακροχρόνια άνεργος)"
#     ENERGH_LIGO = "Ενεργή (Λιγότερο από 12 μήνες)"
#     OXI = "Όχι"
#
# class AdeiaAsfaleias(str, Enum):
#     NAI = "Ναι"
#     OXI = "Όχι"
#     EXEILH3EI = "Έχει λήξει"
#     YPOEKDOSH = "Υπό έκδοση"
#
# class NaiOxi(str, Enum):
#     NAI = "Ναι"
#     OXI = "Όχι"
#
# class Agglika(str, Enum):
#     KA8OLOU = "Καθόλου"
#     BASIC = "Στοιχειώδης / Βασική"
#     METRIA = "Μέτρια / Καλή"
#     POLY_KALH = "Πολύ καλή / Άριστη"
#
# class Gender(str, Enum):
#     MALE = "Άνδρας"
#     FEMALE = "Γυναίκα"
#     OTHER = "Άλλο"


class Employee(Document):
    #username = fields.StringField(primary_key=True, unique=True, required=True),
    # username = fields.StringField(unique=True, required=True),
    # first_name = fields.StringField(required=True),
    # last_name = fields.StringField(required=True),
    username = fields.StringField(),
    first_name = fields.StringField(),
    last_name = fields.StringField(),
    # gender = fields.EnumField(Gender),
    # cs_user_status = fields.EnumField(CandidateStatus),  # Auto einai h Trexousa Katastash 1A
    # job_position = fields.ListField(fields.EnumField(JobType)), #1B
    # desirable_sector = fields.ListField(fields.EnumField(SpecialismType))  #2
    # cs_specialisms = fields.ListField(Specialism),  # 2A & 2B
    # #cs_specialisms = EmbeddedDocumentListField(Specialism)
    # desirable_country = fields.StringField(default='Ελλάδα'),  #3
    # desirable_area_perifereia = fields.StringField(),  #values from lat_long Collection (Perifereia_gr) #4
    # desirable_area_dhmos = fields.StringField(), #values from lat_long Collection (Dhmos_gr) #5
    # desirable_work_type = fields.EnumField(DesirableWorkType, default=DesirableWorkType.FULL), #6
    # desirable_schedule = fields.EnumField(DesirableSchedule, default=DesirableSchedule.ADIAFORO), #7
    # min_wromis8io = fields.FloatField(), #8
    # min_mis8os = fields.FloatField(), #9
    # karta_anergias = fields.EnumField(KartaAnergias, default=KartaAnergias.OXI), #10
    # adeia_asfaleias = fields.EnumField(AdeiaAsfaleias), #11
    # adeiaIX = fields.EnumField(NaiOxi), #12
    # adeiaDikyklo = fields.EnumField(NaiOxi), #13
    # education_level = fields.EnumField(EducationLevel, default=None), #14
    # agglika = fields.EnumField(Agglika), #15
    # allh_glwssa =  fields.ListField(fields.StringField()), #Kamia, mia h kai parapanw alles glwsses #15A
    # cctv =  fields.EnumField(NaiOxi), #16
    # pc = fields.EnumField(NaiOxi), #17
    # mouseia = fields.EnumField(NaiOxi), #18
    # x_ray_screener = fields.EnumField(NaiOxi), #19
    # first_aid = fields.EnumField(NaiOxi), #20
    # lifeguard = fields.EnumField(NaiOxi), #21
    # limenikes_egk = fields.EnumField(NaiOxi), #22
    # epoptes_arxi = fields.EnumField(NaiOxi), #23
    # vip = fields.EnumField(NaiOxi), #24
    # oplokatoxh = fields.EnumField(NaiOxi), #25
    # polemikes_texnes = fields.EnumField(NaiOxi), #26
    # drone = fields.EnumField(NaiOxi), #27
    # military_obligations = fields.EnumField(Military, default=None), #28
    # physic_and_endurance = fields.IntField(min_value=1, max_value=5), #29
    # appearance = fields.IntField(min_value=1, max_value=5), #30
    # supervision_inspection = fields.IntField(min_value=1, max_value=5), #31
    # communications_skills = fields.IntField(min_value=1, max_value=5), #32
    # reflexes_on_danger = fields.IntField(min_value=1, max_value=5), #33
    # professionalism = fields.IntField(min_value=1, max_value=5), #34
    # confidentiality = fields.IntField(min_value=1, max_value=5),  #35

    meta = {'collection': 'employees'}

    def __str__(self):
        return f"Employee(username='{self.username}', " \
               f"first_name='{self.first_name}', " \
               f"last_name='{self.last_name}', " \
               f"gender='{self.gender}', " \
               f"cs_user_status='{self.cs_user_status}', " \
               f"job_position='{self.job_position}', " \
               f"desirable_country='{self.desirable_country}', " \
               f"desirable_area_perifereia='{self.desirable_area_perifereia}', " \
               f"desirable_area_dhmos='{self.desirable_area_dhmos}', " \
               f"desirable_work_type='{self.desirable_work_type}', " \
               f"desirable_schedule='{self.desirable_schedule}', " \
               f"min_wromis8io={self.min_wromis8io}, " \
               f"min_mis8os={self.min_mis8os}, " \
               f"karta_anergias='{self.karta_anergias}', " \
               f"adeia_asfaleias='{self.adeia_asfaleias}', " \
               f"adeiaIX='{self.adeiaIX}', " \
               f"adeiaDikyklo='{self.adeiaDikyklo}', " \
               f"education_level='{self.education_level}', " \
               f"agglika='{self.agglika}', " \
               f"allh_glwssa='{self.allh_glwssa}', " \
               f"cctv='{self.cctv}', " \
               f"pc='{self.pc}', " \
               f"mouseia='{self.mouseia}', " \
               f"x_ray_screener='{self.x_ray_screener}', " \
               f"first_aid='{self.first_aid}', " \
               f"lifeguard='{self.lifeguard}', " \
               f"limenikes_egk='{self.limenikes_egk}', " \
               f"epoptes_arxi='{self.epoptes_arxi}', " \
               f"vip='{self.vip}', " \
               f"oplokatoxh='{self.oplokatoxh}', " \
               f"polemikes_texnes='{self.polemikes_texnes}', " \
               f"drone='{self.drone}', " \
               f"military_obligations='{self.military_obligations}', " \
               f"physic_and_endurance={self.physic_and_endurance}, " \
               f"appearance={self.appearance}, " \
               f"supervision_inspection={self.supervision_inspection}, " \
               f"communications_skills={self.communications_skills}, " \
               f"reflexes_on_danger={self.reflexes_on_danger}, " \
               f"professionalism={self.professionalism}, " \
               f"confidentiality={self.confidentiality})"
'''
class Employee(Document):
    ID = fields.StringField(unique=True, null=False),
    user_login = fields.StringField(unique=True, null=False),
    user_email = fields.EmailField(unique=True, null=False),
    metaaa = EmbeddedDocumentField(Meta, db_field="meta")

    meta = {'collection': 'employees'}
'''