import datetime
from enum import Enum
from mongoengine import Document, EmbeddedDocument, EmbeddedDocumentField, fields

# Create your models here.
class SpecialismType(Enum):
    #DIGITAL = 'digital' # ti einai ayto dhladh?
    POLYKATASTHMA = 'Πολυκατάστημα / Mall'
    SUPERMARKET = 'Supermarket'
    A8LHTIKES = 'Αθλητικές Εγκαταστάσεις / Parking / Εκθεσιακό Κέντρο'
    HOTEL = 'Ξενοδοχείο'
    XRHMATAPOSTOLH = 'Χρηματαποστολές'
    DHMOSIO = 'Δημόσιο Κτήριο'
    OIKIA = 'Βίλα / Οικία'
    MUSEUM = 'Μουσείο'
    AIRPORT = 'Αεροδρόμιο'
    PORT = 'Λιμένας'
    APO8HKH = 'Αποθήκη / Εργοστάσιο / Φυλάκιο'
    BEACH = 'Οργανωμένη Παραλία / Πισίνα'
    OTHER = 'Άλλο'

class Specialism(EmbeddedDocument):
    specialism = fields.EnumField(SpecialismType, default=None)
    specialism_time_from = fields.DateField()
    specialism_time_to = fields.DateField(default=datetime.datetime.utcnow())
    specialism_time_diff = fields.FloatField()

class JobType(Enum):
    PROSWPIKO_ASF = 'Προσωπικό Ασφαλείας - Φύλακας(Στατική φύλαξη)'
    PATROL = 'Προσωπικό Ασφαλείας - Patrol'
    ELEGKTHS = 'Ελεγκτής Ασφαλείας Αερομεταφορών(X - Ray Screener)'
    EPOPTHS = 'Επόπτης Ασφαλείας'
    SHMATA = 'Υπάλληλος κέντρου λήψεως σημάτων'
    SYMVANTA = 'Διαχειριστής Συμβάντων Ασφαλείας (SOC–Security Incidents Administrator)'
    XRHMATAPOSTOLES_ODHGOS = 'Οδηγός Χρηματαποστολών'
    XRHMATAPOSTOLES_SYNODHGOS = 'Συνοδός Χρηματαποστολών'
    KATAMETRHTHS = 'Καταμετρητής Χρηματαποστολών'
    RECEPTION = 'Υπάλληλος Υποδοχής(Reception)'
    ASFALEIA_RECEPTION = 'Υπάλληλος Ασφαλείας Υποδοχής(Reception)'
    LIFEGUARD_SEE = 'Ναυαγοσώστης Πισίνας / Θαλάσσης(Lifeguard)'
    LIFEGUARD_POOL = 'Ναυαγοσώστης Πισίνας(Lifeguard)'
    KA8ARISTHS = 'Καθαριστής'
    YPEY8YNOS_KA8ARISTHS = 'Υπεύθυνος τμήματος καθαριότητας'
    TEXNIKOS_EGKATASTASHS = 'Τεχνικός Εγκατάστασης και Συντήρησης Συστημάτων Ασφαλείας'
    SALES_SUPPORT = 'Sales Customer Support Specialist'
    GRAMMATEIA = 'Υπάλληλος γραφείου(Γραμματεία)'
    VOH8OS_GRAFEIOU = 'Βοηθός Γραφείου Ασφαλείας'
    ATM = 'Τεχνικός - Διαχειριστής ΑΤΜ(άδεια security)'
    PRESALES = 'Presales Engineer'
    RISKMANAGEMENT = 'Security Risk Management Specialist'
    PROCUREMENT = 'Procurement Officer'
    APO8HKH = 'Υπάλληλος Αποθήκης'
    APENTOMWSH = 'Τεχνικός Εφαρμογών Απεντομώσεων & Απολυμάνσεων – Γεωπόνος'
    OTHER = 'Άλλο'

class EducationLevel(Enum):
    DHMOTIKO = "Δημοτικό"
    GYMNASIO = "Γυμνάσιο"
    LYKEIO = "Λύκειο"
    IEK = "ΙΕΚ"
    AEI_TEI = "ΑΕΙ/ΤΕΙ"
    MASTER = "Μεταπτυχιακό"

class SecurityLicense(Enum):
    NAI = "Ναι"
    OXI = "Όχι"
    Expired = "Έχει λήξει"
    YpoEkdosh = "Υπό έκδοση"

class Military(Enum):
    NAI = "Ναι"
    OXI = "Όχι"
    MhYpoxreos = "Μη Υπόχρεος"

class CandidateStatus(Enum):
    NOT_WORKING = "Δεν εργάζομαι – Αναζητώ μία θέση εργασίας."
    WORKING = "Εργάζομαι, αλλά αναζητώ καλύτερες συνθήκες."
    NOT_LOOKING = "Δεν αναζητώ μία θέση εργασίας προς το παρών."

class DesirableWorkType(Enum):
    FULL = "Πλήρους απασχόλησης"
    PARTTIME = "Μερικής απασχόλησης"
    SEASON = "Εποχιακή θέση"
    CONTRACTOR = "Ελεύθερος Επαγγελματίας"
    EVENT = "Έκτακτη θέση (Event)"

class DesirableSchedule(Enum):
    PRWINO = "ΔΕ-ΠΑ (Πρωινό)"
    KYLIOMENO = "ΔΕ-ΠΑ (Κυλιόμενο)"
    VRADINO = "ΔΕ-ΠΑ (Βραδινό)"
    SAVVATO = "Σάββατο (Δυνατότητα εργασίας)"
    KYRIAKH = "Κυριακή (Δυνατότητα εργασίας)"
    ADIAFORO = "Αδιάφορο"

class KartaAnergias(Enum):
    ENERGH_MAKRO = "Ενεργή (Μακροχρόνια άνεργος)"
    ENERGH_LIGO = "Ενεργή (Λιγότερο από 12 μήνες)"
    OXI = "Όχι"

class AdeiaAsfaleias(Enum):
    NAI = "Ναι"
    OXI = "Όχι"
    EXEILH3EI = "Έχει λήξει"
    YPOEKDOSH = "Υπό έκδοση"

class NaiOxi(Enum):
    NAI = "Ναι"
    OXI = "Όχι"

class Agglika(Enum):
    KA8OLOU = "Καθόλου"
    BASIC = "Στοιχειώδης / Βασική"
    METRIA = "Μέτρια / Καλή"
    POLY_KALH = "Πολύ καλή / Άριστη"

class Gender(Enum):
    MALE = "Άνδρας"
    FEMALE = "Γυναίκα"
    OTHER = "Άλλο"


class Employee(EmbeddedDocument):
    username = fields.StringField(primary_key=True, unique=True, required=True),
    first_name = fields.StringField(required=True),
    last_name = fields.StringField(required=True),
    gender = fields.EnumField(Gender),
    cs_user_status = fields.EnumField(CandidateStatus),  # Auto einai h Trexousa Katastash 1A
    job_position = fields.ListField(fields.EnumField(JobType)), #1B
    desirable_sector = fields.ListField(fields.EnumField(SpecialismType))  #2
    cs_specialisms = fields.ListField(Specialism),  # 2A & 2B
    desirable_country = fields.StringField(default='Ελλάδα'),  #3
    desirable_area_perifereia = fields.StringField(),  #values from lat_long Collection (Perifereia_gr) #4
    desirable_area_dhmos = fields.StringField(), #values from lat_long Collection (Dhmos_gr) #5
    desirable_work_type = fields.EnumField(DesirableWorkType, default=DesirableWorkType.FULL), #6
    desirable_schedule = fields.EnumField(DesirableSchedule, default=DesirableSchedule.ADIAFORO), #7
    min_wromis8io = fields.FloatField(), #8
    min_mis8os = fields.FloatField(), #9
    karta_anergias = fields.EnumField(KartaAnergias, default=KartaAnergias.OXI), #10
    adeia_asfaleias = fields.EnumField(AdeiaAsfaleias), #11
    adeiaIX = fields.EnumField(NaiOxi), #12
    adeiaDikyklo = fields.EnumField(NaiOxi), #13
    education_level = fields.EnumField(EducationLevel, default=None), #14
    agglika = fields.EnumField(Agglika), #15
    allh_glwssa =  fields.ListField(fields.StringField()), #Kamia, mia h kai parapanw alles glwsses #15A
    cctv =  fields.EnumField(NaiOxi), #16
    pc = fields.EnumField(NaiOxi), #17
    mouseia = fields.EnumField(NaiOxi), #18
    x_ray_screener = fields.EnumField(NaiOxi), #19
    first_aid = fields.EnumField(NaiOxi), #20
    lifeguard = fields.EnumField(NaiOxi), #21
    limenikes_egk = fields.EnumField(NaiOxi), #22
    epoptes_arxi = fields.EnumField(NaiOxi), #23
    vip = fields.EnumField(NaiOxi), #24
    oplokatoxh = fields.EnumField(NaiOxi), #25
    polemikes_texnes = fields.EnumField(NaiOxi), #26
    drone = fields.EnumField(NaiOxi), #27
    military_obligations = fields.EnumField(Military, default=None), #28
    physic_and_endurance = fields.IntField(min_value=1, max_value=5), #29
    appearance = fields.IntField(min_value=1, max_value=5), #30
    supervision_inspection = fields.IntField(min_value=1, max_value=5), #31
    communications_skills = fields.IntField(min_value=1, max_value=5), #32
    reflexes_on_danger = fields.IntField(min_value=1, max_value=5), #33
    professionalism = fields.IntField(min_value=1, max_value=5), #34
    confidentiality = fields.IntField(min_value=1, max_value=5),  #35

    meta = {'collection': 'employees'}

'''
    description = fields.StringField(),
    rich_editing = fields.BooleanField(), #? XXX
    syntax_highlighting = fields.BooleanField(), #? XXX
    comment_shortcuts = fields.BooleanField(), #? XXX
    admin_color = fields.BooleanField(), #? XXX
    use_ssl = fields.BooleanField(), #? XXX
    show_admin_bar_front = fields.BooleanField(), #? XXX
    locale = fields.StringField(), #? XXX
    xaOGsRJF0_capabilities = fields.StringField(), #? XXX
    xaOGsRJF0_user_level = fields.StringField(), #? XXX
    _yoast_wpseo_profile_updated = fields.StringField(), #? XXX
    dismissed_wp_pointers = fields.StringField(), #? XXX
    cs_allow_search = fields.BooleanField(), #? XXX
    last_update = fields.StringField(), #? is this a date? XXX
    session_tokens = fields.StringField(), #? XXX
    user_last_login = fields.StringField(), #? is this a date? XXX
    wc_last_active =  fields.StringField(), #? is this a date? XXX
    cs_user_last_activity_date = fields.StringField(), #? is this a date? XXX
    cs_phone_number = fields.StringField(), #?
    _woocommerce_persistent_cart_1 = fields.StringField(), #? XXX
    cs_employer_img = fields.StringField(), #? XXX
    cs_cover_employer_img = fields.StringField(), #? XXX
    cs_new_bull = fields.StringField(), #? XXX
    cs_facebook = fields.URLField(), #? XXX
    cs_twitter = fields.URLField(), #? XXX
    cs_linkedin = fields.URLField(), #? XXX
    cs_post_loc_country = fields.StringField(), #?
    cs_post_loc_city = fields.StringField(), #?
    cs_post_comp_address = fields.StringField(), #?
    cs_post_loc_address = fields.StringField(), #?
    cs_post_loc_latitude = fields.StringField(), #?
    cs_post_loc_longitude = fields.StringField(), #?
    cs_add_new_loc = fields.StringField(), #? XXX
    cs_post_loc_zoom = fields.StringField(), #? XXX
    established = fields.StringField(), #??? XXX
    team_size = fields.StringField(), #? XXX
    type = fields.StringField(), #? XXX
    cs_user = fields.StringField(), #? XXX
    cs_array_data = fields.StringField(), #????? XXX
    user_img = fields.StringField(), #? XXX
    cover_user_img = fields.StringField(), #? XXX
    facebook = fields.URLField(), #??? PALI? XXX
    instagram = fields.URLField(), #???? XXX
    linkedin = fields.URLField(), #??? PALI XXX
    myspace = fields.URLField(), #........... XXX
    pinterest = fields.URLField(), # ?? XXX
    soundcloud = fields.URLField(), # ?? oxi spotify? XXX
    tumblr = fields.URLField(), #?? XXX
    twitter = fields.URLField(), #?? PALI XXX
    youtube = fields.URLField(), #?? XXX
    wikipedia = fields.URLField(), #?? XXX
    cs_job_title = fields.StringField(),
    cs_minimum_salary = fields.FloatField(),
    cs_trans_id = fields.StringField(), #?
    cs_award_name_pop = fields.StringField(), #?
    cs_award_year_pop = fields.DateTimeField(), #?
    cs_award_desc_pop = fields.StringField(), #?
    cs_image_title = fields.StringField(), #?
    cs_skill_title = fields.StringField(), #?
    cs_skill_percentage = fields.StringField(), #?
    cs_edu_title = fields.StringField(), #?
    cs_edu_from_date = fields.DateField(), #?
    cs_edu_to_date = fields.DateField(), #?
    cs_edu_institute = fields.StringField(), #?
    cs_edu_desc = fields.StringField(), #?
    cs_exp_title = fields.StringField(), #?
    cs_exp_from_date = fields.DateField(), #?
    cs_exp_to_date = fields.DateField(), #?
    cs_exp_company = fields.StringField(), #?
    cs_exp_desc = fields.StringField(), #?
    cs_cover_letter = fields.StringField(), #?
    cs_candidate_cv = fields.StringField(), #?
    show_experience = fields.BooleanField(), #?
    show_age = fields.BooleanField(), #?
    wpseo_title = fields.StringField(), #?
    wpseo_metadesc = fields.StringField(), #?
    wpseo_noindex_author = fields.StringField(), #?
    wpseo_content_analysis_disable = fields.StringField(), #?
    wpseo_keyword_analysis_disable = fields.StringField(), #?
    wpseo_inclusive_language_analysis_disable = fields.StringField(),
    billing_first_name = fields.StringField(), #?
    billing_last_name = fields.StringField(), #?
    billing_company = fields.StringField(), #?
    billing_address_1 = fields.StringField(), #?
    billing_address_2 = fields.StringField(), #?
    billing_city = fields.StringField(), #?
    billing_postcode = fields.StringField(), #?
    billing_country = fields.StringField(), #?
    billing_state = fields.StringField(), #?
    billing_phone = fields.StringField(), #?
    billing_email = fields.StringField(), #?
    shipping_first_name = fields.StringField(), #?
    shipping_last_name = fields.StringField(), #?
    shipping_company = fields.StringField(), #?
    shipping_address_1 = fields.StringField(), #?
    shipping_address_2 = fields.StringField(), #?
    shipping_city = fields.StringField(), #?
    shipping_postcode = fields.StringField(), #?
    shipping_country = fields.StringField(), #?
    shipping_state = fields.StringField(), #?
    shipping_phone = fields.StringField(), #?
    cs_candidate_search_flag = fields.BooleanField(), #?
    cs_candidate_search_data = fields.StringField(), #?
    cs_candidate_skills_percentage = fields.FloatField(), #???
    cs_cover_candidate_img = fields.StringField(), #?
    cs_video_url = fields.StringField(), #?
    #cs_get_last_job = fields.ListField(fields.EnumField(JobType)), # 2 --> auto egine desirable_sector... h oxi..? oxi, allo to ena allo to allo...
    cs_minimum_workingtime = fields.FloatField(), #???
    cs_minimum_workingtimemonth = fields.FloatField, #???
    cs_post_loc_zip = fields.StringField(), #???
    cs_post_loc_birth = fields.StringField(), #?
    cs_get_hours_week = fields.FloatField(), #???
    cs_get_wanted_hours = fields.FloatField(), #???
    cs_skills_list_array = fields.StringField(), #???
    cs_skill_title_array = fields.StringField(), #???
    cs_skill_percentage_array = fields.StringField(), #???
    cs_ = fields.StringField(), #?
    cs_likio__ = fields.BooleanField(), #?
    action = fields.StringField(), #?
    security_license_expiry = fields.DateField(),
    driving_license_car_expiry = fields.DateField(),
    driving_license_motorcycle_expiry = fields.DateField(),
    lifeguard_expiry = fields.DateField(),
    lifeguard = fields.BooleanField(),
    high_school = fields.BooleanField(), # XXX
    university = fields.BooleanField(), # XXX
    security_license = fields.EnumField(SecurityLicense, default=None),
    driving_license_car = fields.BooleanField(),
    driving_license_motorcycle = fields.BooleanField(),
    cctv = fields.BooleanField(),
    x_ray_screener =  fields.BooleanField(),
    computer_usage = fields.BooleanField(),
    first_aid = fields.BooleanField(),
    port_security = fields.BooleanField(),
    security_supervisor = fields.BooleanField(),
    vip = fields.BooleanField(),
    gun_license = fields.BooleanField(),
    martial_arts = fields.BooleanField(),
    drone_operator = fields.BooleanField(),
    cs_specialisms2 = fields.ListField(Specialism), # XXX
    cs_specialisms3 = fields.ListField(Specialism), # XXX
    cs_specialisms4 = fields.ListField(Specialism), # XXX
    cs_cs_specialisms_time = fields.FloatField(),
    cs_cs_specialisms_time2 = fields.FloatField(), # XXX
    cs_cs_specialisms_time3 = fields.FloatField(), # XXX
    cs_cs_specialisms_time4 = fields.FloatField(), # XXX
    cs_specialisms_time = fields.FloatField(), # XXX
    cs_specialisms_time2 = fields.FloatField(), # XXX
    cs_specialisms_time3 = fields.FloatField(), # XXX
    cs_specialisms_time4 = fields.FloatField(), # XXX
    cs_work_type = fields.StringField() # XXX
'''
'''
class Employee(Document):
    ID = fields.StringField(unique=True, null=False),
    user_login = fields.StringField(unique=True, null=False),
    user_email = fields.EmailField(unique=True, null=False),
    metaaa = EmbeddedDocumentField(Meta, db_field="meta")

    meta = {'collection': 'employees'}
'''