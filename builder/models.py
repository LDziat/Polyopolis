from django.db import models
from django.conf import settings
import uuid
from django.contrib.auth.hashers import make_password, check_password
from random import choice

def insta_name():
    themeadjlist = ["abundant", "accurate", "adaptable", "adventurous", "affectionate", "agile", "alert", "amazing", "ambitious", "amiable", "amused", "analytical", "angelic", "animated", "appreciative", "artistic", "assertive", "athletic", "attentive", "attractive", "balanced", "beautiful", "believable", "benevolent", "bold", "brave", "bright", "brilliant", "calm", "capable", "careful", "caring", "cautious", "charming", "cheerful", "clever", "colorful", "compassionate", "competent", "confident", "considerate", "consistent", "content", "cooperative", "courageous", "courteous", "creative", "cultured", "curious", "daring", "decisive", "dedicated", "delicate", "dependable", "determined", "diligent", "discreet", "dynamic", "eager", "earnest", "easygoing", "efficient", "elegant", "empathetic", "energetic", "engaging", "enthusiastic", "ethical", "excited", "experienced", "expressive", "exuberant", "fair", "faithful", "fantastic", "fearless", "flexible", "focused", "forgiving", "friendly", "fun", "generous", "gentle", "genuine", "giving", "graceful", "gracious", "grateful", "happy", "hardworking", "helpful", "honest", "hopeful", "humble", "humorous", "imaginative", "impartial", "independent", "industrious", "innovative", "insightful", "inspiring", "intelligent", "intuitive", "inventive", "joyful", "jubilant", "kind", "knowledgeable", "likable", "lively", "logical", "loyal", "lucky", "magnificent", "mature", "mellow", "meticulous", "modest", "motivated", "natural", "neat", "nice", "optimistic", "organized", "original", "outgoing", "passionate", "patient", "peaceful", "perceptive", "persistent", "playful", "polite", "positive", "practical", "precise", "productive", "professional", "proud", "punctual", "quick", "quiet", "rational", "reliable", "resourceful", "respectful", "responsible", "responsive", "romantic", "sensible", "sensitive", "serene", "sincere", "skillful", "smart", "sociable", "sophisticated", "spirited", "spontaneous", "stable", "strong", "successful", "supportive", "talented", "thoughtful", "tidy", "tolerant", "trusting", "trustworthy", "understanding", "upbeat", "versatile", "vibrant", "warm", "willing", "wise", "witty", "admirable", "adroit", "agreeable", "alluring", "amusing", "appealing", "apprehensive", "ardent", "aspiring", "astute", "attentive", "auspicious", "awesome", "balanced", "benign", "bold", "brainy", "brisk", "buoyant", "calculating", "carefree", "cautious", "cerebral", "charitable", "chivalrous", "civil", "classic", "clever", "compassionate", "competent", "confident", "considerate", "constant", "cool", "cordial", "courteous", "cultured", "dapper", "daring", "debonair", "decent", "decisive", "dedicated", "dignified", "discerning", "disciplined", "distinct", "driven", "dutiful", "earnest", "educated", "efficient", "elegant", "eloquent", "eminent", "energetic", "engaging", "enthusiastic", "exceptional", "exemplary", "fair", "faithful", "fascinating", "fearless", "fervent", "fiery", "focused", "forgiving", "forthright", "frank", "friendly", "gallant", "genial", "genuine", "gifted", "glad", "glorious", "gracious", "grand", "gregarious", "grounded", "gutsy", "handsome", "hardy", "harmonious", "hearty", "helpful", "honest", "honorable", "humorous", "idealistic", "illustrious", "impeccable", "impressive", "independent", "industrious", "innovative", "inspiring", "intrepid", "invaluable", "jovial", "jubilant", "judicious", "keen", "kindhearted", "knowledgeable", "laudable", "levelheaded", "liberal", "likable", "lively", "logical", "lovable", "loyal", "lucid", "lucky", "magnanimous", "magnificent", "marvelous", "masterful", "mature", "methodical", "meticulous", "modest", "motivated", "munificent", "mystical", "neat", "noble", "nurturing", "observant", "open-minded", "optimistic", "orderly", "organized", "outgoing", "outspoken", "passionate", "patient", "peaceful", "perceptive", "persistent", "philanthropic", "philosophical", "placid", "playful", "poised", "polished", "polite", "positive", "practical", "precise", "pristine", "productive", "proficient", "proud", "punctual", "quick", "quiet", "rational", "receptive", "reflective", "reliable", "remarkable", "reserved", "resolute", "respectful", "responsible", "responsive", "reverent", "robust", "romantic", "sage", "savvy", "sensible", "sensitive", "sentimental", "serene", "sharp", "shrewd", "sincere", "skilled", "smart", "sociable", "sophisticated", "spirited", "stable", "steadfast", "steady", "stellar", "stimulating", "strategic", "strong", "studious", "successful", "supportive", "sustainable", "sympathetic", "systematic", "tactful", "talented", "tenacious", "thoughtful", "tidy", "tireless", "tolerant", "tranquil", "trusting", "trustworthy", "unbiased", "understanding", "unique", "upbeat", "upright", "valiant", "versatile", "vibrant", "vigilant", "virtuous", "visionary", "vivacious", "warmhearted", "willing", "wise", "witty", "wondrous", "worthy", "zealous", "zesty"]
    themenounlist = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "part", "child", "eye", "woman", "place", "work", "week", "case", "point", "government", "company", "number", "group", "problem", "fact", "beach", "tree", "family", "area", "story", "month", "right", "study", "book", "night", "home", "water", "room", "mother", "car", "word", "sentence", "school", "father", "friend", "idea", "food", "moment", "air", "city", "office", "door", "team", "personality", "growth", "love", "line", "health", "fire", "forest", "street", "art", "science", "nature", "guitar", "house", "homework", "system", "church", "map", "teacher", "ear", "object", "bank", "lake", "pencil", "village", "garden", "bookstore", "science", "test", "phone", "computer", "network", "author", "grocery", "store", "mountain", "window", "college", "field", "river", "factory", "nail", "coin", "price", "product", "message", "newspaper", "park", "employee", "vacation", "food", "road", "destination", "meeting", "pool", "university", "law", "police", "case", "club", "bathroom", "floor", "island", "department", "square", "mall", "hall", "animal", "concert", "record", "energy", "engine", "relationship", "dream", "doctor", "diet", "editor", "insurance", "profit", "election", "conference", "pen", "piano", "singer", "shop", "art", "literature", "machine", "music", "crowd", "height", "weight", "childhood", "history", "report", "forest", "ocean", "beach", "score", "credit", "holiday", "power", "surgery", "truth", "opinion", "church", "library", "bottle", "cake", "mall", "bread", "problem", "paper", "weekend", "bridge", "river", "machine", "brain", "drawing", "advice", "question", "weather", "photograph", "literature", "forest", "condition", "restaurant", "kingdom", "brother", "bridge", "tradition", "condition", "disease", "mistake", "security", "shoe", "tail", "information", "explanation", "scene", "event", "space", "insect", "kitchen", "concept", "customer", "village", "emotion", "trip", "situation", "weekend", "tower", "destination", "package", "desk", "knife", "hole", "feeling", "factory", "sample", "gift", "company", "reality", "plan", "classroom", "campus", "region", "date", "goal", "rule", "quality", "result", "song", "recipe", "danger", "price", "zone", "weight", "mind", "ability", "dance", "menu", "soil", "bridge", "bike", "planet", "safety", "waterfall", "flower", "parent", "hat", "instrument", "choice", "platform", "ceremony", "science", "technology", "hair", "mission", "document", "month", "nation", "review", "gate", "tool", "condition", "childhood", "crystal", "floor", "universe", "lesson", "education", "tradition", "celebration", "soup", "planet", "sunset", "table", "animal", "fruit", "hour", "wedding", "engine", "camera", "pizza", "project", "dinner", "plant", "clock", "energy", "museum", "cable", "design", "knowledge", "contest", "heaven", "thunder", "category", "region", "bicycle", "strength", "feeling", "crime", "poem", "agency", "history", "diamond", "jewel", "tree", "rose", "feather", "step", "chance", "cave", "jungle", "rose", "arrow", "cloud", "figure", "magazine", "strawberry", "course", "finger", "poet", "society", "market", "quality", "mystery", "bridge", "holiday", "death", "laugh", "hole", "neighbor", "height", "expression", "distance", "danger", "cause", "friendship", "limit", "sign", "agreement", "charity", "advice", "bowl", "continent", "action", "degree", "memory", "stranger", "spider", "ocean", "thought", "fish", "energy", "result", "instrument", "flight", "attempt", "fashion", "furniture", "reality", "revolution", "parade", "accident", "wonder", "medicine", "vase", "opinion", "kingdom", "scent", "horror", "angel", "coast", "youth", "branch", "art", "wind", "movie", "comedy", "danger", "victory", "age", "feather", "passion", "kindness", "scent", "sentence", "staircase", "seashore", "star", "treatment", "wood", "attitude", "lab", "formula", "glacier", "time", "control", "insurance", "range", "library", "carpet", "apple", "emotion", "mission", "cooperation", "holiday", "science", "climb", "hobby", "republic", "existence", "evidence", "ambition", "project", "love", "jungle", "order", "source", "origin", "conclusion", "legend", "gallery", "lock", "planet", "attraction", "lesson", "shape", "mood", "hero", "policy", "surprise", "spirit", "sympathy", "difference", "note", "relation", "adventure", "cloud", "strength", "attention", "energy", "passion", "scream", "air", "art", "muscle", "process", "choice", "company", "goal", "member", "atmosphere", "storm", "desire", "adventure", "ice", "adventure", "friend", "breeze", "event", "center", "growth", "harmony", "time", "ocean", "moon", "height", "skill", "place", "benefit", "opportunity", "past", "climate", "area", "silver", "shade", "factor", "energy", "emotion", "mood", "concept", "smile", "feeling", "storm", "ocean", "space", "height", "glance", "language", "universe", "fiction", "surface", "reality", "history", "fiction", "game", "light", "ice", "story", "cloud", "strength", "shape", "wisdom", "sunlight", "time", "forest", "structure", "angle", "depth", "honor", "glory", "message", "mystery", "secret", "testament", "dimension", "relic", "place", "echo", "wonder", "concept", "vacuum", "voice", "opinion", "sensation", "thought", "idea", "legend", "desire", "dream", "hope", "secret", "obstacle", "vision", "symbol", "expression", "reflection", "energy", "moment", "obstacle", "pattern", "signal", "change", "trend", "movement", "knowledge", "theory", "shadow", "shape", "balance", "pulse", "sound", "aura", "charm", "rhythm", "secret", "clarity", "faith", "enigma", "feather", "revelation", "hope", "phenomenon", "verse"]
    noun = choice(themenounlist)
    adj = choice(themeadjlist)
    name = adj[0].upper() + adj[1:] + " " + noun[0].upper() + noun[1:] 
    return name

class Theme(models.Model):
    name = models.CharField(max_length=256, unique=True)
    css = models.CharField(max_length=512, blank=True, null=True)
    text = models.CharField(max_length=16, blank=True, null=True)
    accent = models.CharField(max_length=16, blank=True, null=True)
    accent_text = models.CharField(max_length=16, blank=True, null=True)
    accent_hov = models.CharField(max_length=16, blank=True, null=True)
    back = models.CharField(max_length=16, blank=True, null=True)
    backimg = models.CharField(max_length=256, null=True, default='none')

    def generate_css(self):
        """Generate the CSS content for this theme."""
        return f"""
        :root {{
            --backimg: url(\"{self.backimg}\");
            --text: {self.text};
            --accent_text: {self.accent_text};
            --accent_hov: {self.accent_hov};
            --accent: {self.accent};
            --back: {self.back};
        }}
        """
    def save(self, *args, **kwargs):
        # Generate CSS before saving
        self.css = self.generate_css()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Page(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, default="")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    touch_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()  # This stores the cleaned HTML content of the page
    unlisted = models.BooleanField(default=False)           # Premium Feature - Prevents pages from appearing in master list
    private = models.BooleanField(default=False)            # Premium Feature - Allows users to restrict a page to specific users
    locked = models.BooleanField(default=False)             # Premium Feature - Locks a page behind a password screen.
    passwd = models.CharField(max_length=200,default="")    # This is kinda gross right now. Better make sure this is hashed lol.
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='pages', default=None, null=True)
    jscript = models.BooleanField(default=False)            # Controls if javascript is allowed



    def __str__(self):
        return self.title

    def set_password(self, raw_password):
        self.passwd = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.passwd)

class Section(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name='sections')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.page.title}"

class Element(models.Model):
    ELEMENT_TYPES = [
        ('text', 'Text'),
        ('image', 'Image'),
        ('link', 'Link'),
        #('youtube', 'Youtube'),
        #('tweet', 'Tweet'),
        #('audio', 'Audio'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='elements')
    element_type = models.CharField(default='text', max_length=50, choices=ELEMENT_TYPES)
    content = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return f"{self.element_type} - {self.section.name} ({self.order})"


