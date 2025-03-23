def calculate_disc_profile(responses):
    """
    Calcule le profil DISC basé sur les réponses au questionnaire et détermine les deux profils dominants.
    
    Le modèle DISC catégorise les comportements en quatre types principaux :
    - D (Dominant/Rouge) : direct, orienté résultats, déterminé
    - I (Influent/Jaune) : sociable, enthousiaste, optimiste
    - S (Stable/Vert) : fiable, patient, coopératif
    - C (Consciencieux/Bleu) : précis, analytique, méthodique
    
    Args:
        responses (dict): Dictionnaire contenant les réponses aux questions
                          Format attendu: {question_id: réponse} où réponse est 'D', 'I', 'S' ou 'C'
        
    Returns:
        dict: Dictionnaire structuré contenant:
            - scores: comptage brut des réponses par profil
            - percentages: pourcentage de chaque profil
            - dominant_profiles: liste des deux profils dominants avec détails
            - all_profiles: informations complètes sur tous les profils
    
    Exemple:
        >>> responses = {'q1': 'D', 'q2': 'I', 'q3': 'D', 'q4': 'S', 'q5': 'C'}
        >>> result = calculate_disc_profile(responses)
        >>> result['dominant_profiles'][0]['color']  # Retourne la couleur du profil dominant
        'Rouge'
    """
    # Initialiser les compteurs pour chaque profil
    profile_counts = {
        'D': 0,  # Dominant (Rouge)
        'I': 0,  # Influent (Jaune)
        'S': 0,  # Stable (Vert)
        'C': 0   # Consciencieux (Bleu)
    }
    
    # Compter les réponses pour chaque profil
    for question, answer in responses.items():
        profile_counts[answer] += 1
    
    # Convertir les compteurs en pourcentages
    total_questions = len(responses)
    profile_percentages = {
        'D': (profile_counts['D'] / total_questions) * 100,
        'I': (profile_counts['I'] / total_questions) * 100,
        'S': (profile_counts['S'] / total_questions) * 100,
        'C': (profile_counts['C'] / total_questions) * 100
    }
    
    # Déterminer les deux profils dominants
    sorted_profiles = sorted(profile_counts.items(), key=lambda x: x[1], reverse=True)
    dominant_profiles = sorted_profiles[:2]
    
    # Créer un dictionnaire pour les couleurs correspondantes
    color_mapping = {
        'D': 'Rouge',
        'I': 'Jaune',
        'S': 'Vert',
        'C': 'Bleu'
    }
    
    # Créer un dictionnaire pour les descriptions des profils
    profile_descriptions = {
        'D': {
            'title': 'Dominant (Rouge)',
            'description': 'Vous êtes déterminé, direct et orienté vers les résultats. Vous aimez relever des défis et prendre des décisions rapides. Vous êtes naturellement compétitif et n\'avez pas peur de prendre des risques pour atteindre vos objectifs.',
            'strengths': 'Leadership, confiance en soi, prise de décision rapide',
            'challenges': 'Peut parfois être perçu comme agressif ou insensible en raison de votre nature directe'
        },
        'I': {
            'title': 'Influent (Jaune)',
            'description': 'Vous êtes sociable, enthousiaste et expressif. Vous aimez interagir avec les autres et avez une capacité naturelle à influencer et persuader. Vous êtes optimiste et créatif dans votre approche des problèmes.',
            'strengths': 'Communication, motivation des autres, créativité',
            'challenges': 'Peut parfois être impulsif et avoir du mal à se concentrer sur une seule tâche à la fois'
        },
        'S': {
            'title': 'Stable (Vert)',
            'description': 'Vous êtes fiable, empathique et patient. Vous êtes attentif aux besoins des autres et excellent pour maintenir l\'harmonie au sein d\'un groupe. Vous préférez la stabilité et la prévisibilité dans votre environnement.',
            'strengths': 'Loyauté, calme, maintien de l\'harmonie dans le groupe',
            'challenges': 'Peut être résistant au changement et prendre des décisions lentement'
        },
        'C': {
            'title': 'Consciencieux (Bleu)',
            'description': 'Vous êtes précis, analytique et méticuleux. Vous aimez analyser les situations et prendre des décisions basées sur des faits et des informations précises. Vous avez un souci du détail et recherchez l\'excellence dans tout ce que vous faites.',
            'strengths': 'Organisation, discipline, réflexion stratégique',
            'challenges': 'Peut être trop critique et manquer de souplesse'
        }
    }
    
    # Préparer les résultats
    results = {
        'scores': profile_counts,
        'percentages': profile_percentages,
        'dominant_profiles': [
            {
                'letter': dominant_profiles[0][0],
                'color': color_mapping[dominant_profiles[0][0]],
                'score': dominant_profiles[0][1],
                'percentage': profile_percentages[dominant_profiles[0][0]],
                'description': profile_descriptions[dominant_profiles[0][0]]
            },
            {
                'letter': dominant_profiles[1][0],
                'color': color_mapping[dominant_profiles[1][0]],
                'score': dominant_profiles[1][1],
                'percentage': profile_percentages[dominant_profiles[1][0]],
                'description': profile_descriptions[dominant_profiles[1][0]]
            }
        ],
        'all_profiles': {
            'D': {
                'letter': 'D',
                'color': color_mapping['D'],
                'score': profile_counts['D'],
                'percentage': profile_percentages['D'],
                'description': profile_descriptions['D']
            },
            'I': {
                'letter': 'I',
                'color': color_mapping['I'],
                'score': profile_counts['I'],
                'percentage': profile_percentages['I'],
                'description': profile_descriptions['I']
            },
            'S': {
                'letter': 'S',
                'color': color_mapping['S'],
                'score': profile_counts['S'],
                'percentage': profile_percentages['S'],
                'description': profile_descriptions['S']
            },
            'C': {
                'letter': 'C',
                'color': color_mapping['C'],
                'score': profile_counts['C'],
                'percentage': profile_percentages['C'],
                'description': profile_descriptions['C']
            }
        }
    }
    
    return results
