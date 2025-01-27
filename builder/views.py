from django.shortcuts import render, redirect, get_object_or_404
from .models import Page, Section, Element, Theme
from .forms import PageForm, SectionForm, ElementForm, HTMLImportForm, SignUpForm, PageContentForm, SearchForm, ThemeSelectForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden, HttpResponse
from datetime import datetime 
from bs4 import BeautifulSoup
from random import choice
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

def insta_name():
    themeadjlist = ["abundant", "accurate", "adaptable", "adventurous", "affectionate", "agile", "alert", "amazing", "ambitious", "amiable", "amused", "analytical", "angelic", "animated", "appreciative", "artistic", "assertive", "athletic", "attentive", "attractive", "balanced", "beautiful", "believable", "benevolent", "bold", "brave", "bright", "brilliant", "calm", "capable", "careful", "caring", "cautious", "charming", "cheerful", "clever", "colorful", "compassionate", "competent", "confident", "considerate", "consistent", "content", "cooperative", "courageous", "courteous", "creative", "cultured", "curious", "daring", "decisive", "dedicated", "delicate", "dependable", "determined", "diligent", "discreet", "dynamic", "eager", "earnest", "easygoing", "efficient", "elegant", "empathetic", "energetic", "engaging", "enthusiastic", "ethical", "excited", "experienced", "expressive", "exuberant", "fair", "faithful", "fantastic", "fearless", "flexible", "focused", "forgiving", "friendly", "fun", "generous", "gentle", "genuine", "giving", "graceful", "gracious", "grateful", "happy", "hardworking", "helpful", "honest", "hopeful", "humble", "humorous", "imaginative", "impartial", "independent", "industrious", "innovative", "insightful", "inspiring", "intelligent", "intuitive", "inventive", "joyful", "jubilant", "kind", "knowledgeable", "likable", "lively", "logical", "loyal", "lucky", "magnificent", "mature", "mellow", "meticulous", "modest", "motivated", "natural", "neat", "nice", "optimistic", "organized", "original", "outgoing", "passionate", "patient", "peaceful", "perceptive", "persistent", "playful", "polite", "positive", "practical", "precise", "productive", "professional", "proud", "punctual", "quick", "quiet", "rational", "reliable", "resourceful", "respectful", "responsible", "responsive", "romantic", "sensible", "sensitive", "serene", "sincere", "skillful", "smart", "sociable", "sophisticated", "spirited", "spontaneous", "stable", "strong", "successful", "supportive", "talented", "thoughtful", "tidy", "tolerant", "trusting", "trustworthy", "understanding", "upbeat", "versatile", "vibrant", "warm", "willing", "wise", "witty", "admirable", "adroit", "agreeable", "alluring", "amusing", "appealing", "apprehensive", "ardent", "aspiring", "astute", "attentive", "auspicious", "awesome", "balanced", "benign", "bold", "brainy", "brisk", "buoyant", "calculating", "carefree", "cautious", "cerebral", "charitable", "chivalrous", "civil", "classic", "clever", "compassionate", "competent", "confident", "considerate", "constant", "cool", "cordial", "courteous", "cultured", "dapper", "daring", "debonair", "decent", "decisive", "dedicated", "dignified", "discerning", "disciplined", "distinct", "driven", "dutiful", "earnest", "educated", "efficient", "elegant", "eloquent", "eminent", "energetic", "engaging", "enthusiastic", "exceptional", "exemplary", "fair", "faithful", "fascinating", "fearless", "fervent", "fiery", "focused", "forgiving", "forthright", "frank", "friendly", "gallant", "genial", "genuine", "gifted", "glad", "glorious", "gracious", "grand", "gregarious", "grounded", "gutsy", "handsome", "hardy", "harmonious", "hearty", "helpful", "honest", "honorable", "humorous", "idealistic", "illustrious", "impeccable", "impressive", "independent", "industrious", "innovative", "inspiring", "intrepid", "invaluable", "jovial", "jubilant", "judicious", "keen", "kindhearted", "knowledgeable", "laudable", "levelheaded", "liberal", "likable", "lively", "logical", "lovable", "loyal", "lucid", "lucky", "magnanimous", "magnificent", "marvelous", "masterful", "mature", "methodical", "meticulous", "modest", "motivated", "munificent", "mystical", "neat", "noble", "nurturing", "observant", "open-minded", "optimistic", "orderly", "organized", "outgoing", "outspoken", "passionate", "patient", "peaceful", "perceptive", "persistent", "philanthropic", "philosophical", "placid", "playful", "poised", "polished", "polite", "positive", "practical", "precise", "pristine", "productive", "proficient", "proud", "punctual", "quick", "quiet", "rational", "receptive", "reflective", "reliable", "remarkable", "reserved", "resolute", "respectful", "responsible", "responsive", "reverent", "robust", "romantic", "sage", "savvy", "sensible", "sensitive", "sentimental", "serene", "sharp", "shrewd", "sincere", "skilled", "smart", "sociable", "sophisticated", "spirited", "stable", "steadfast", "steady", "stellar", "stimulating", "strategic", "strong", "studious", "successful", "supportive", "sustainable", "sympathetic", "systematic", "tactful", "talented", "tenacious", "thoughtful", "tidy", "tireless", "tolerant", "tranquil", "trusting", "trustworthy", "unbiased", "understanding", "unique", "upbeat", "upright", "valiant", "versatile", "vibrant", "vigilant", "virtuous", "visionary", "vivacious", "warmhearted", "willing", "wise", "witty", "wondrous", "worthy", "zealous", "zesty"]
    themenounlist = ["time", "person", "year", "way", "day", "thing", "man", "world", "life", "hand", "part", "child", "eye", "woman", "place", "work", "week", "case", "point", "government", "company", "number", "group", "problem", "fact", "beach", "tree", "family", "area", "story", "month", "right", "study", "book", "night", "home", "water", "room", "mother", "car", "word", "sentence", "school", "father", "friend", "idea", "food", "moment", "air", "city", "office", "door", "team", "personality", "growth", "love", "line", "health", "fire", "forest", "street", "art", "science", "nature", "guitar", "house", "homework", "system", "church", "map", "teacher", "ear", "object", "bank", "lake", "pencil", "village", "garden", "bookstore", "science", "test", "phone", "computer", "network", "author", "grocery", "store", "mountain", "window", "college", "field", "river", "factory", "nail", "coin", "price", "product", "message", "newspaper", "park", "employee", "vacation", "food", "road", "destination", "meeting", "pool", "university", "law", "police", "case", "club", "bathroom", "floor", "island", "department", "square", "mall", "hall", "animal", "concert", "record", "energy", "engine", "relationship", "dream", "doctor", "diet", "editor", "insurance", "profit", "election", "conference", "pen", "piano", "singer", "shop", "art", "literature", "machine", "music", "crowd", "height", "weight", "childhood", "history", "report", "forest", "ocean", "beach", "score", "credit", "holiday", "power", "surgery", "truth", "opinion", "church", "library", "bottle", "cake", "mall", "bread", "problem", "paper", "weekend", "bridge", "river", "machine", "brain", "drawing", "advice", "question", "weather", "photograph", "literature", "forest", "condition", "restaurant", "kingdom", "brother", "bridge", "tradition", "condition", "disease", "mistake", "security", "shoe", "tail", "information", "explanation", "scene", "event", "space", "insect", "kitchen", "concept", "customer", "village", "emotion", "trip", "situation", "weekend", "tower", "destination", "package", "desk", "knife", "hole", "feeling", "factory", "sample", "gift", "company", "reality", "plan", "classroom", "campus", "region", "date", "goal", "rule", "quality", "result", "song", "recipe", "danger", "price", "zone", "weight", "mind", "ability", "dance", "menu", "soil", "bridge", "bike", "planet", "safety", "waterfall", "flower", "parent", "hat", "instrument", "choice", "platform", "ceremony", "science", "technology", "hair", "mission", "document", "month", "nation", "review", "gate", "tool", "condition", "childhood", "crystal", "floor", "universe", "lesson", "education", "tradition", "celebration", "soup", "planet", "sunset", "table", "animal", "fruit", "hour", "wedding", "engine", "camera", "pizza", "project", "dinner", "plant", "clock", "energy", "museum", "cable", "design", "knowledge", "contest", "heaven", "thunder", "category", "region", "bicycle", "strength", "feeling", "crime", "poem", "agency", "history", "diamond", "jewel", "tree", "rose", "feather", "step", "chance", "cave", "jungle", "rose", "arrow", "cloud", "figure", "magazine", "strawberry", "course", "finger", "poet", "society", "market", "quality", "mystery", "bridge", "holiday", "death", "laugh", "hole", "neighbor", "height", "expression", "distance", "danger", "cause", "friendship", "limit", "sign", "agreement", "charity", "advice", "bowl", "continent", "action", "degree", "memory", "stranger", "spider", "ocean", "thought", "fish", "energy", "result", "instrument", "flight", "attempt", "fashion", "furniture", "reality", "revolution", "parade", "accident", "wonder", "medicine", "vase", "opinion", "kingdom", "scent", "horror", "angel", "coast", "youth", "branch", "art", "wind", "movie", "comedy", "danger", "victory", "age", "feather", "passion", "kindness", "scent", "sentence", "staircase", "seashore", "star", "treatment", "wood", "attitude", "lab", "formula", "glacier", "time", "control", "insurance", "range", "library", "carpet", "apple", "emotion", "mission", "cooperation", "holiday", "science", "climb", "hobby", "republic", "existence", "evidence", "ambition", "project", "love", "jungle", "order", "source", "origin", "conclusion", "legend", "gallery", "lock", "planet", "attraction", "lesson", "shape", "mood", "hero", "policy", "surprise", "spirit", "sympathy", "difference", "note", "relation", "adventure", "cloud", "strength", "attention", "energy", "passion", "scream", "air", "art", "muscle", "process", "choice", "company", "goal", "member", "atmosphere", "storm", "desire", "adventure", "ice", "adventure", "friend", "breeze", "event", "center", "growth", "harmony", "time", "ocean", "moon", "height", "skill", "place", "benefit", "opportunity", "past", "climate", "area", "silver", "shade", "factor", "energy", "emotion", "mood", "concept", "smile", "feeling", "storm", "ocean", "space", "height", "glance", "language", "universe", "fiction", "surface", "reality", "history", "fiction", "game", "light", "ice", "story", "cloud", "strength", "shape", "wisdom", "sunlight", "time", "forest", "structure", "angle", "depth", "honor", "glory", "message", "mystery", "secret", "testament", "dimension", "relic", "place", "echo", "wonder", "concept", "vacuum", "voice", "opinion", "sensation", "thought", "idea", "legend", "desire", "dream", "hope", "secret", "obstacle", "vision", "symbol", "expression", "reflection", "energy", "moment", "obstacle", "pattern", "signal", "change", "trend", "movement", "knowledge", "theory", "shadow", "shape", "balance", "pulse", "sound", "aura", "charm", "rhythm", "secret", "clarity", "faith", "enigma", "feather", "revelation", "hope", "phenomenon", "verse"]
    noun = choice(themenounlist)
    adj = choice(themeadjlist)
    name = adj[0].upper() + adj[1:] + " " + noun[0].upper() + noun[1:] 
    return name


@login_required
def import_html(request):
    if request.method == 'POST':
        form = HTMLImportForm(request.POST, request.FILES)
        if form.is_valid():
            html_file = request.FILES['html_file']
            title = form.cleaned_data['title']
            soup = BeautifulSoup(html_file, 'html.parser')

            # Strip out all <script> tags and JavaScript inline events
            if form.cleaned_data['strip']:
                for script in soup(["script"]):
                    script.extract()

            cleaned_html = str(soup)

            # Create or update the user's page with the cleaned HTML
            page = Page.objects.create(owner=request.user)
            page.content = cleaned_html
            page.title = title
            page.jscript = form.cleaned_data['strip']
            page.save()

            return redirect('page_viewer', page_id=page.id)
    else:
        form = HTMLImportForm()

    return render(request, 'builder/import_html.html', {'form': form})

@login_required
def export_html(request, page_id):
    page = Page.objects.get(id=page_id, owner=request.user)
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to export this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    if page.content != "":
        response = HttpResponse(page.content, content_type='text/html')
    else:
        sections = page.sections.all()
        pagedat = "<h2>" + page.title + "</h2>" + "\n<h3>Sections</h3>\n<ul>\n"
        for section in sections:
            pagedat += "<h4>" + section.name + "</h4>" + "\n<ul>\n"
            for element in section.elements.all():
                if element.element_type == 'image':
                    pagedat += '<li><img src="' + element.content +'"></li>'
                elif element.element_type == 'link':
                    pagedat += '<li><a href="' + element.content +'"></li>'
                else:
                    pagedat += '<li>' + element.content +'</li>'
            pagedat += "</ul>"
            pagedat += "</li"
        pagedat += "</ul>"
        response = HttpResponse(pagedat, content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="{page.title}.html"'
    return response


# Account Management
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('page_list')
    else:
        form = SignUpForm()
    return render(request, 'builder/signup.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('page_list')
    else:
        form = AuthenticationForm()
    return render(request, 'builder/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('page_list')

# Homepage
def page_list(request):
    pages = Page.objects.filter(unlisted=False)
    return render(request, 'builder/page_list.html', {'pages': pages})

# Page Editor

@xframe_options_exempt
def page_viewer(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    # Check if the page has content
    if page.locked:
        return redirect('locked_page', page_id=page.id)
    if page.content:
        print(page.content)
        return render(request, 'builder/page_view_pro.html', {'page': page, 'html_content': page.content})
    else:
        sections = page.sections.all()
        return render(request, 'builder/page_viewer.html', {'page': page, 'sections': sections})

@login_required
def activate_html(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to edit this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    if page.content == "":
        page.content = "Welcome to HTML mode\nTo return to Quikedit simply delete everything in this box and select 'Save Changes'. Otherwise, feel free to replace this text with your custom HTML code!"
    else:
        page.content = ""
    page.save()
    return page_editor(request, page_id)

@login_required
def page_editor(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to edit this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    sections = page.sections.all()
    page.touch_time = datetime.now()
    page.save()
    if request.method == 'POST':
        form = PageContentForm(request.POST)
        if form.is_valid():
            if request.POST.get('action') == 'preview':
                prev_content = form.cleaned_data['content']
                return HttpResponse(prev_content)
            else:
                if page.jscript:
                    print("STRIP JS HERE UWU")
                page.content = form.cleaned_data['content']
                page.title = form.cleaned_data['title']
                page.save()
                return redirect('page_list')
    else:
        form = PageContentForm(initial={'content': page.content, 'title':page.title})
    if page.content == "":
        return render(request, 'builder/page_editor.html', {'page': page, 'sections': sections, })
    else:
        return render(request, 'builder/page_editor.html', {'page': page, 'sections': sections, 'form': form})

@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.owner = request.user
            page.save()
            return redirect('page_editor', page_id=page.id)
    else:
        form = PageForm()
    return render(request, 'builder/create_page.html', {'form': form})

@login_required
def admin_panel(request, page_id):
    page = get_object_or_404(Page, id=page_id)#, owner=request.user)
    themes = Theme.objects.all()
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to admin this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    if request.method == "POST":
        page.jscript = request.POST.get('jscript', 'off') == 'on'
        page.unlisted = request.POST.get('unlisted', 'off') == 'on'
        page.locked = request.POST.get('locked', 'off') == 'on'
        if request.POST.get('theme') != "None":
            print(request.POST.get('theme'))
            page.theme = get_object_or_404(Theme, id=request.POST.get('theme'))
        else:
            page.theme = None

        # Only hash if a new password is provided
        raw_password = request.POST.get('passwd', '')
        if raw_password:
            page.set_password(raw_password)

        page.save()
    
    return render(request, 'builder/admin_panel.html', {
        'page': page,
        'themes': themes
    })

# Example view checking the password
def locked_page_view(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if not page.locked:  # If the page isn't actually locked, redirect to the main page viewer
        return redirect('page_viewer', page_id=page.id)

    if request.method == "POST":
        entered_password = request.POST.get('password', '')
        if page.check_password(entered_password):
            if page.content:
                return render(request, 'builder/page_view_pro.html', {'page': page, 'html_content': page.content})
            else:
                sections = page.sections.all()
                return render(request, 'builder/page_viewer.html', {'page': page, 'sections': sections})
        else:
            return render(request, 'builder/locked_page.html', {'page': page, 'error': 'Incorrect password'})

    return render(request, 'builder/locked_page.html', {'page': page})


@login_required
def create_section(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to edit this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    page.touch_time = datetime.now()
    page.save()
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.page = page
            section.save()
            return redirect('page_editor', page_id=page.id)
    else:
        form = SectionForm()
    return render(request, 'builder/create_section.html', {'form': form, 'page': page})

@login_required
def create_element(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    page = get_object_or_404(Page, id=section.page.id)
    if page.owner != request.user:
        return HttpResponseForbidden("<h1>You do not have permission to edit this page, "+ choice(["punk", "loser", "jerk", "asshole", "retard", "weiner", "dick", "dumbass"]) +"!</h1>")
    page.touch_time = datetime.now()
    page.save()
    if request.method == 'POST':
        form = ElementForm(request.POST)
        if form.is_valid():
            element = form.save(commit=False)
            element.section = section
            element.save()
            return redirect('page_editor', page_id=section.page.id)
    else:
        form = ElementForm()
    return render(request, 'builder/create_element.html', {'form': form, 'section': section, 'page': page})

def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if request.method == 'POST':
        # If the user confirms, delete the page and redirect to the list of pages or another appropriate location
        page.delete()
        return redirect('page_list')

    # Display the confirmation page
    return render(request, 'builder/delete_page_confirmation.html', {'page': page})

def search(request):
    form = SearchForm()
    results = set()  # Use a set to prevent duplicate pages

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            # Search Page Titles
            title_matches = Page.objects.filter(title__icontains=query, unlisted=False)
            results.update(title_matches)

            # Search Page Owners
            owner_matches = Page.objects.filter(owner__username__icontains=query, unlisted=False)
            results.update(owner_matches)

            # Search Pages for the query in the content field
            page_matches = Page.objects.filter(content__icontains=query, unlisted=False)
            results.update(page_matches)

            # Search Sections for the query in their name and get related pages
            section_matches = Section.objects.filter(name__icontains=query)
            pages_from_sections = Page.objects.filter(sections__in=section_matches, unlisted=False).distinct()
            results.update(pages_from_sections)

            # Search Elements for the query in their content and get related pages through their sections
            element_matches = Element.objects.filter(content__icontains=query)
            pages_from_elements = Page.objects.filter(sections__elements__in=element_matches, unlisted=False).distinct()
            results.update(pages_from_elements)

    return render(request, 'builder/search.html', {'form': form, 'results': list(results)})

def user_page(request):
    form = SearchForm()
    results = set()  # Use a set to prevent duplicate pages
    query = ''

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            # Search Page Owners
            owner_matches = Page.objects.filter(owner__username__icontains=query)
            results.update(owner_matches)

    return render(request, 'builder/user_page.html', {'form': form, 'results': list(results), 'username': query})

def select_theme(request):
    if request.method == 'POST':
        form = ThemeSelectForm(request.POST)
        if form.is_valid():
            selected_theme = form.cleaned_data['theme']
            # Save the selected theme to the user's session or model
            request.session['selected_theme'] = selected_theme.css
            return redirect('theme')  # Redirect to a page with the new theme
    else:
        form = ThemeSelectForm()
    
    return render(request, 'builder/themes.html', {'form': form})

def theme_builder(request):
    # Default color values
    colors = {
        'text': '#acc6e0',
        'accent': '#405f7f',
        'accent_text': '#bbc5cf',
        'accent_hov': '#2f465d',
        'back': '#172533',
        'backimg': 'none',
    }
    #--backimg: none;

    if request.method == 'POST':
        # Update colors with user's selected values
        colors['text'] = request.POST.get('text', colors['text'])
        colors['accent_text'] = request.POST.get('accent_text', colors['accent_text'])
        colors['accent_hov'] = request.POST.get('accent_hov', colors['accent_hov'])
        colors['accent'] = request.POST.get('accent', colors['accent'])
        colors['back'] = request.POST.get('back', colors['back'])
        colors['backimg'] = request.POST.get('backimg', colors['backimg'])

        if 'save_theme' in request.POST:  # Check if the save theme button was clicked
            theme_name = request.POST.get('theme_name', "Unnamed Theme")
            if theme_name == "":
                theme_name = insta_name() + " Theme"
            # Create a new Theme object and save it
            Theme.objects.create(
                name=theme_name,
                backimg=colors['backimg'],
                text=colors['text'],
                accent_text=colors['accent_text'],
                accent_hov=colors['accent_hov'],
                accent=colors['accent'],
                back=colors['back'],
                
            )

            return redirect('theme')  # Redirect to a page showing saved themes (optional)

    return render(request, 'builder/theme_builder.html', {
        **colors,
    })

    return render(request, 'builder/theme_builder.html', colors)

def save_edits(request, page_id):
    if request.method == 'POST':
        page = get_object_or_404(Page, id=page_id)

        # Update page title
        page_title = request.POST.get('page-title')
        print(f"Page Title: {page_title}")
        page.title = page_title if page_title else page.title
        page.save()

        # Update each section
        sections = page.sections.all()
        for section in sections:
            section_name_key = f'section-name-{section.id}'
            section_name = request.POST.get(section_name_key)
            print(f"Section Name for {section.id}: {section_name}")
            if section_name:
                section.name = section_name
                section.save()

            # Update each element within this section
            for element in section.elements.all():
                element_content_key = f'element-content-{element.id}'
                element_content = request.POST.get(element_content_key)
                print(f"Element Content for {element.id}: {element_content}")
                if element_content:
                    element.content = element_content
                    element.save()

        return redirect('page_editor', page_id=page.id)

    return redirect('page_viewer', page_id=page_id)
