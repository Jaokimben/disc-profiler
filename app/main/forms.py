from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

class DISCQuestionnaireForm(FlaskForm):
    """
    Formulaire pour le questionnaire DISC avec 20 questions
    
    Ce formulaire présente 20 questions permettant d'évaluer le profil DISC d'un utilisateur.
    Chaque question propose 4 réponses possibles correspondant aux quatre profils DISC :
    - D (Dominant) : Rouge
    - I (Influent) : Jaune
    - S (Stable) : Vert
    - C (Consciencieux) : Bleu
    
    L'utilisateur doit choisir une réponse pour chaque question, et les résultats
    sont ensuite analysés pour déterminer les deux profils dominants.
    """
    
    q1 = RadioField(
        'Face à un problème à résoudre, vous préférez généralement :',
        choices=[
            ('D', 'Prendre rapidement une décision et passer à l\'action'),
            ('I', 'Discuter du problème avec d\'autres personnes pour trouver des solutions créatives'),
            ('S', 'Prendre le temps de réfléchir et consulter l\'avis de chacun avant de décider'),
            ('C', 'Analyser méthodiquement toutes les données disponibles avant de choisir la meilleure option')
        ],
        validators=[DataRequired()]
    )
    
    q2 = RadioField(
        'Dans une conversation, vous êtes plutôt :',
        choices=[
            ('D', 'Direct et concis, allant droit au but'),
            ('I', 'Expressif et animé, partageant facilement vos émotions'),
            ('S', 'Attentif et patient, écoutant plus que vous ne parlez'),
            ('C', 'Précis et structuré, attentif aux détails dans vos explications')
        ],
        validators=[DataRequired()]
    )
    
    q3 = RadioField(
        'Dans un projet d\'équipe, ce qui vous motive le plus c\'est :',
        choices=[
            ('D', 'Atteindre des objectifs ambitieux et obtenir des résultats concrets'),
            ('I', 'Collaborer avec les autres et créer une ambiance positive'),
            ('S', 'Contribuer à la stabilité du groupe et maintenir l\'harmonie'),
            ('C', 'Garantir la qualité du travail et respecter les normes établies')
        ],
        validators=[DataRequired()]
    )
    
    q4 = RadioField(
        'Face au changement, vous avez tendance à :',
        choices=[
            ('D', 'L\'initier vous-même et encourager les autres à suivre'),
            ('I', 'L\'accueillir avec enthousiasme et y voir de nouvelles opportunités'),
            ('S', 'Prendre le temps de vous y adapter progressivement'),
            ('C', 'L\'analyser en détail pour en comprendre tous les aspects avant de l\'accepter')
        ],
        validators=[DataRequired()]
    )
    
    q5 = RadioField(
        'Quand vous devez prendre une décision importante, vous vous basez principalement sur :',
        choices=[
            ('D', 'Votre instinct et votre capacité à obtenir des résultats rapides'),
            ('I', 'Votre intuition et l\'impact sur les personnes concernées'),
            ('S', 'Les conséquences à long terme et le maintien de la stabilité'),
            ('C', 'Les faits, les données et l\'analyse logique')
        ],
        validators=[DataRequired()]
    )
    
    q6 = RadioField(
        'Dans votre environnement de travail idéal :',
        choices=[
            ('D', 'Vous avez de l\'autonomie et des défis à relever régulièrement'),
            ('I', 'L\'ambiance est conviviale et vous pouvez interagir librement avec les autres'),
            ('S', 'L\'atmosphère est calme, prévisible et collaborative'),
            ('C', 'Tout est bien organisé, structuré et les processus sont clairement définis')
        ],
        validators=[DataRequired()]
    )
    
    q7 = RadioField(
        'Face à un conflit, vous avez tendance à :',
        choices=[
            ('D', 'L\'affronter directement pour trouver une solution rapide'),
            ('I', 'Chercher à négocier et à trouver un compromis qui satisfait tout le monde'),
            ('S', 'Éviter la confrontation et chercher à apaiser les tensions'),
            ('C', 'Analyser objectivement la situation pour identifier la solution la plus logique')
        ],
        validators=[DataRequired()]
    )
    
    q8 = RadioField(
        'Quand vous recevez une critique, vous :',
        choices=[
            ('D', 'Réagissez immédiatement et défendez votre point de vue'),
            ('I', 'Cherchez à maintenir une bonne relation malgré le désaccord'),
            ('S', 'Prenez le temps de réfléchir avant de répondre'),
            ('C', 'Demandez des précisions et des exemples concrets')
        ],
        validators=[DataRequired()]
    )
    
    q9 = RadioField(
        'Dans un projet, ce qui vous stresse le plus c\'est :',
        choices=[
            ('D', 'Le manque de progrès et les délais non respectés'),
            ('I', 'L\'absence de communication et d\'enthousiasme dans l\'équipe'),
            ('S', 'Les changements soudains et les perturbations dans la routine'),
            ('C', 'Le manque de précision et les erreurs dans le travail')
        ],
        validators=[DataRequired()]
    )
    
    q10 = RadioField(
        'Quand vous partagez une idée avec les autres, vous mettez l\'accent sur :',
        choices=[
            ('D', 'Les résultats concrets et les avantages pratiques'),
            ('I', 'L\'aspect novateur et l\'enthousiasme qu\'elle peut générer'),
            ('S', 'La façon dont elle peut bénéficier à tout le monde et maintenir l\'harmonie'),
            ('C', 'La logique, les détails et la faisabilité technique')
        ],
        validators=[DataRequired()]
    )
    
    q11 = RadioField(
        'Comment gérez-vous les délais serrés ?',
        choices=[
            ('D', 'Je prends le contrôle et pousse l\'équipe à accélérer le rythme'),
            ('I', 'Je motive l\'équipe en maintenant une énergie positive et en célébrant les petites victoires'),
            ('S', 'Je planifie soigneusement pour éviter le stress et maintenir un rythme constant'),
            ('C', 'Je vérifie minutieusement chaque détail pour éviter les erreurs malgré la pression')
        ],
        validators=[DataRequired()]
    )
    
    q12 = RadioField(
        'Quel est votre style de leadership préféré ?',
        choices=[
            ('D', 'Direct et orienté vers les résultats, fixant des objectifs clairs'),
            ('I', 'Charismatique et inspirant, motivant les autres par l\'enthousiasme'),
            ('S', 'Supportif et patient, créant un environnement stable et harmonieux'),
            ('C', 'Analytique et méthodique, établissant des processus précis')
        ],
        validators=[DataRequired()]
    )
    
    q13 = RadioField(
        'Comment réagissez-vous face à un échec ?',
        choices=[
            ('D', 'Je rebondis rapidement et cherche immédiatement une autre solution'),
            ('I', 'Je partage mes sentiments et cherche du soutien auprès des autres'),
            ('S', 'Je prends le temps de digérer l\'information et d\'accepter la situation'),
            ('C', 'J\'analyse en détail ce qui s\'est passé pour éviter que cela ne se reproduise')
        ],
        validators=[DataRequired()]
    )
    
    q14 = RadioField(
        'Dans une réunion d\'équipe, vous êtes généralement celui qui :',
        choices=[
            ('D', 'Dirige la discussion et prend les décisions finales'),
            ('I', 'Apporte de l\'énergie et encourage la participation de tous'),
            ('S', 'Écoute attentivement et soutient les idées des autres'),
            ('C', 'Pose des questions précises et vérifie la faisabilité des propositions')
        ],
        validators=[DataRequired()]
    )
    
    q15 = RadioField(
        'Comment organisez-vous votre espace de travail ?',
        choices=[
            ('D', 'Fonctionnel et efficace, axé sur les résultats'),
            ('I', 'Personnalisé et stimulant, reflétant ma personnalité'),
            ('S', 'Confortable et familier, avec une ambiance apaisante'),
            ('C', 'Méthodique et ordonné, où tout a sa place')
        ],
        validators=[DataRequired()]
    )
    
    q16 = RadioField(
        'Quand vous devez présenter un projet :',
        choices=[
            ('D', 'Je vais droit au but en mettant l\'accent sur les résultats et l\'impact'),
            ('I', 'Je crée une présentation dynamique et engageante qui captive l\'audience'),
            ('S', 'Je prépare une présentation équilibrée qui tient compte des besoins de chacun'),
            ('C', 'Je présente une analyse détaillée avec des données précises et vérifiables')
        ],
        validators=[DataRequired()]
    )
    
    q17 = RadioField(
        'Face à une opportunité inattendue, vous :',
        choices=[
            ('D', 'Saisissez rapidement l\'occasion et prenez des risques calculés'),
            ('I', 'Partagez votre enthousiasme et ralliez les autres à cette nouvelle idée'),
            ('S', 'Évaluez comment elle s\'intègre dans vos plans actuels avant de décider'),
            ('C', 'Analysez soigneusement tous les aspects avant de vous engager')
        ],
        validators=[DataRequired()]
    )
    
    q18 = RadioField(
        'Dans votre approche du travail quotidien, vous privilégiez :',
        choices=[
            ('D', 'L\'efficacité et les résultats rapides'),
            ('I', 'La créativité et les interactions sociales'),
            ('S', 'La constance et la fiabilité'),
            ('C', 'La précision et la qualité')
        ],
        validators=[DataRequired()]
    )
    
    q19 = RadioField(
        'Quand vous travaillez en équipe, votre plus grande force est :',
        choices=[
            ('D', 'Votre capacité à prendre des décisions et à diriger le groupe'),
            ('I', 'Votre enthousiasme contagieux et votre talent pour motiver les autres'),
            ('S', 'Votre patience et votre capacité à créer un environnement harmonieux'),
            ('C', 'Votre attention aux détails et votre rigueur dans l\'exécution')
        ],
        validators=[DataRequired()]
    )
    
    q20 = RadioField(
        'Comment réagissez-vous face à une situation ambiguë ?',
        choices=[
            ('D', 'Je prends l\'initiative de clarifier la situation et d\'établir une direction'),
            ('I', 'Je reste optimiste et j\'explore différentes possibilités avec les autres'),
            ('S', 'Je cherche à maintenir la stabilité pendant que la situation se clarifie'),
            ('C', 'Je recherche plus d\'informations pour réduire l\'incertitude')
        ],
        validators=[DataRequired()]
    )
    
    submit = SubmitField('Voir mes résultats')
