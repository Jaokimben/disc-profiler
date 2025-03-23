from flask import render_template, redirect, url_for, flash, request, session
from app.main import bp
from app.main.forms import DISCQuestionnaireForm
from app.main.disc_logic import calculate_disc_profile

# Routes principales de l'application d'évaluation DISC
# Ces routes gèrent le flux de l'application : accueil -> questionnaire -> résultats

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
def index():
    """
    Page d'accueil avec introduction au test DISC
    
    Cette route affiche la page d'accueil qui présente le modèle DISC
    et invite l'utilisateur à commencer le questionnaire.
    
    Returns:
        Template HTML: Page d'accueil avec titre personnalisé
    """
    return render_template('index.html', title='Évaluation du Profil DISC')

@bp.route('/questionnaire', methods=['GET', 'POST'])
def questionnaire():
    """
    Page du questionnaire DISC avec formulaire interactif
    
    Cette route gère l'affichage et la soumission du formulaire de questionnaire.
    Lorsque le formulaire est soumis et validé, les réponses sont traitées pour
    calculer le profil DISC de l'utilisateur, puis stockées en session avant
    la redirection vers la page de résultats.
    
    Methods:
        GET: Affiche le formulaire vide
        POST: Traite les réponses soumises
    
    Returns:
        GET: Template HTML avec le formulaire
        POST (valide): Redirection vers la page de résultats
        POST (invalide): Template HTML avec le formulaire et messages d'erreur
    """
    # Initialiser le formulaire avec les 10 questions
    form = DISCQuestionnaireForm()
    
    # Traiter la soumission du formulaire
    if form.validate_on_submit():
        # Récupérer les réponses (chaque question est associée à un profil D, I, S ou C)
        responses = {
            'q1': form.q1.data,  # Réponse à la question 1
            'q2': form.q2.data,  # Réponse à la question 2
            'q3': form.q3.data,  # Réponse à la question 3
            'q4': form.q4.data,  # Réponse à la question 4
            'q5': form.q5.data,  # Réponse à la question 5
            'q6': form.q6.data,  # Réponse à la question 6
            'q7': form.q7.data,  # Réponse à la question 7
            'q8': form.q8.data,  # Réponse à la question 8
            'q9': form.q9.data,  # Réponse à la question 9
            'q10': form.q10.data  # Réponse à la question 10
        }
        
        # Calculer le profil DISC en utilisant l'algorithme d'analyse
        disc_profile = calculate_disc_profile(responses)
        
        # Stocker les résultats dans la session pour les récupérer sur la page de résultats
        session['disc_profile'] = disc_profile
        
        # Rediriger vers la page de résultats
        return redirect(url_for('main.results'))
    
    # Afficher le formulaire (GET ou POST invalide)
    return render_template('questionnaire.html', title='Questionnaire DISC', form=form)

@bp.route('/results')
def results():
    """
    Page des résultats du profil DISC
    
    Cette route affiche les résultats de l'évaluation DISC de l'utilisateur.
    Elle récupère les données du profil stockées en session et les transmet
    au template pour affichage. Si aucun résultat n'est disponible en session,
    l'utilisateur est redirigé vers le questionnaire avec un message d'avertissement.
    
    Returns:
        Template HTML: Page de résultats avec les détails du profil DISC
        ou redirection vers le questionnaire si aucun résultat n'est disponible
    
    Note:
        Cette route doit être accédée après avoir complété le questionnaire
    """
    # Récupérer les résultats de la session
    disc_profile = session.get('disc_profile', None)
    
    # Vérifier si les résultats sont disponibles
    if not disc_profile:
        # Informer l'utilisateur qu'il doit d'abord compléter le questionnaire
        flash('Veuillez d\'abord compléter le questionnaire.', 'warning')
        # Rediriger vers la page du questionnaire
        return redirect(url_for('main.questionnaire'))
    
    # Afficher les résultats avec le profil DISC calculé
    return render_template('results.html', title='Résultats du Profil DISC', profile=disc_profile)
